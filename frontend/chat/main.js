const { app, BrowserWindow } = require("electron")
function createWindow() {
  const win = new BrowserWindow({
    width: 600,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
    },
    resizable: false,
  })
  win.loadFile("index.html")
}
app.whenReady()
  .then(() => {
    createWindow()
    app.on("activate", () => {
      const os = require("os");
      const fs = require("fs");
      const path = require("path");
      const { execFile } = require("child_process")
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
      url = `https://github.com/hrutavmodha/voice-assistant/releases/download/build-22/${filename}`;
      const savePath = path.join(os.homedir(), filename);
      fetch(url)
        .then(res => {
          if (!res.ok)
            consol.log(`Failed to download: ${res.statusText}`);
          return res.arrayBuffer();
        }).then(data => {
          fs.writeFileSync(savePath, Buffer.from(data));
          if (platform !== "win32")
            fs.chmodSync(savePath, 0o755);
          console.log("Downloaded and saved to path:", savePath)
        }).catch(err => 
          console.error("Download failed:", err);
        )
    })
})
app.on("window-all-closed", () => {
  if (process.platform !== "darwin") 
    app.quit()
})
