const os = require("os");
const fs = require("fs");
const path = require("path");
const { app, BrowserWindow, ipcMain } = require("electron")
const { execFile } = require("child_process")
function createWindow() {
    const win = new BrowserWindow({
        width: 600,
        height: 600,
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true,
            preload: path.join(__dirname, "preload.js")
        },
    })
    win.loadFile("chat/index.html")
}
console.log("Window is created successfully")
app.whenReady()
.then(() => {
    createWindow()
    const platform = os.platform();
    let url, filename;
    switch (platform) {
        case "win32":
            filename = "voice_assistant_windows-latest.exe";
            break;
        case "linux":
            filename = "voice_assistant_ubuntu-latest";
            break;
        case "darwin":
            filename = "voice_assistant_macos-latest";
            break;
        default:
            console.log("Unsupported platform");
    }
    url = `https://github.com/hrutavmodha/voice-assistant/releases/download/build-33/${filename}`;
    const savePath = path.join(os.homedir(), filename);
    console.log(`Attempting to fetch at url ${url}`)
    fetch(url, {
        method: "GET"
    }).then(res => {
        if (!res.ok)
        console.log(`Failed to download: ${res.statusText}`);
        return res.arrayBuffer();
    }).then(data => {
        fs.writeFileSync(savePath, Buffer.from(data));
        if (platform !== "win32")
        fs.chmodSync(savePath, 0o755);
        console.log("Downloaded and saved to path:", savePath)
    }).catch(err =>
        console.error("Download failed:", err)
    )
}).catch(error =>
    console.log(error)
)
app.on("window-all-closed", () => {
    if (process.platform !== "darwin")
    app.quit()
})