const { app, BrowserWindow, WebContentsView, ipcMain, session } = require('electron');
const path = require('path');

const BAR_HEIGHT = 76;
const HOME = 'https://www.google.com';
let win;
let tabs = [];
let activeId = null;
let counter = 0;

function normalizeUrl(input) {
  const s = input.trim();
  if (!s) return HOME;
  if (/^[a-z]+:\/\//i.test(s)) return s;
  if (/^[^\s]+\.[^\s]{2,}$/.test(s)) return 'https://' + s;
  return 'https://www.google.com/search?q=' + encodeURIComponent(s);
}

function layout() {
  if (!win) return;
  const [w, h] = win.getContentSize();
  for (const t of tabs) {
    t.view.setBounds({ x: 0, y: BAR_HEIGHT, width: w, height: Math.max(0, h - BAR_HEIGHT) });
    t.view.setVisible(t.id === activeId);
  }
}

function sendState() {
  if (!win) return;
  win.webContents.send('state', {
    activeId,
    tabs: tabs.map(t => {
      const wc = t.view.webContents;
      return {
        id: t.id,
        title: wc.getTitle() || 'Tab baru',
        url: wc.getURL(),
        loading: wc.isLoading(),
        canBack: wc.navigationHistory.canGoBack(),
        canForward: wc.navigationHistory.canGoForward(),
      };
    }),
  });
}

function createTab(url) {
  const id = ++counter;
  // Partition tanpa "persist:" = sesi di memori, cookies terpisah per tab,
  // hilang saat tab ditutup (seperti browser baru).
  const ses = session.fromPartition('tab-' + id + '-' + Date.now());
  const view = new WebContentsView({ webPreferences: { session: ses, contextIsolation: true, sandbox: true } });
  const tab = { id, view };
  tabs.push(tab);
  win.contentView.addChildView(view);

  const wc = view.webContents;
  ['did-start-loading', 'did-stop-loading', 'page-title-updated', 'did-navigate', 'did-navigate-in-page']
    .forEach(ev => wc.on(ev, sendState));
  // Link yang membuka jendela baru dibuka di tab yang sama (tetap memakai cookies tab ini).
  wc.setWindowOpenHandler(({ url }) => { wc.loadURL(url); return { action: 'deny' }; });

  wc.loadURL(normalizeUrl(url || HOME));
  activeId = id;
  layout();
  sendState();
}

function closeTab(id) {
  const i = tabs.findIndex(t => t.id === id);
  if (i < 0) return;
  const [tab] = tabs.splice(i, 1);
  win.contentView.removeChildView(tab.view);
  tab.view.webContents.session.clearStorageData().catch(() => {});
  tab.view.webContents.close();
  if (tabs.length === 0) { createTab(); return; }
  if (activeId === id) activeId = tabs[Math.min(i, tabs.length - 1)].id;
  layout();
  sendState();
}

function activeWc() {
  const t = tabs.find(t => t.id === activeId);
  return t && t.view.webContents;
}

ipcMain.on('new-tab', () => createTab());
ipcMain.on('close-tab', (_e, id) => closeTab(id));
ipcMain.on('switch-tab', (_e, id) => { activeId = id; layout(); sendState(); });
ipcMain.on('navigate', (_e, url) => { const wc = activeWc(); if (wc) wc.loadURL(normalizeUrl(url)); });
ipcMain.on('back', () => { const wc = activeWc(); if (wc) wc.navigationHistory.goBack(); });
ipcMain.on('forward', () => { const wc = activeWc(); if (wc) wc.navigationHistory.goForward(); });
ipcMain.on('reload', () => { const wc = activeWc(); if (wc) wc.reload(); });

// Tampil sebagai Chrome biasa (tanpa "Electron") supaya situs seperti Facebook tidak menolak.
app.userAgentFallback = app.userAgentFallback.replace(/ (TabBrowser|tab-browser)\/\S+| Electron\/\S+/g, '');

app.whenReady().then(() => {
  win = new BrowserWindow({
    width: 1280,
    height: 800,
    title: 'TabBrowser',
    autoHideMenuBar: true,
    webPreferences: { preload: path.join(__dirname, 'preload.js'), contextIsolation: true },
  });
  win.loadFile('ui.html');
  win.on('resize', layout);
  win.webContents.once('did-finish-load', () => createTab());
  win.webContents.on('before-input-event', (e, input) => {
    if (input.type !== 'keyDown' || !input.control) return;
    const k = input.key.toLowerCase();
    if (k === 't') { createTab(); e.preventDefault(); }
    if (k === 'w') { closeTab(activeId); e.preventDefault(); }
  });
});

app.on('window-all-closed', () => app.quit());
