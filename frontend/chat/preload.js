const { contextBridge, ipcRenderer } = require("electron")
contextBridge.exposeInMainWorld("python", {
    run: (scriptPath) => {
        ipcRenderer.send("run", {
            scriptPath
        })
    },
    output: (cb) => {
        ipcRenderer.on("output", (event, data) => {
            cb(data)
        })
    }
})