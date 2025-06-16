const { contextBridge, ipcRenderer } = require("electron")
contextBridge.exposeInMainWorld("python", {
    run: (cmd) => {
        ipcRenderer.send("run", {
            cmd
        })
    },
    output: (cb) => {
        ipcRenderer.on("output", (event, data) => {
            cb(data)
        })
    }
})