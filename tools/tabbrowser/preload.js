const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('browser', {
  newTab: () => ipcRenderer.send('new-tab'),
  closeTab: id => ipcRenderer.send('close-tab', id),
  switchTab: id => ipcRenderer.send('switch-tab', id),
  navigate: url => ipcRenderer.send('navigate', url),
  back: () => ipcRenderer.send('back'),
  forward: () => ipcRenderer.send('forward'),
  reload: () => ipcRenderer.send('reload'),
  onState: cb => ipcRenderer.on('state', (_e, s) => cb(s)),
});
