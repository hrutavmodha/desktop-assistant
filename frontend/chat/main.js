const os = require("os");
const fs = require("fs");
const path = require("path");
const { app, BrowserWindow, ipcMain, Notification } = require("electron")
const { spawn } = require("child_process");
let filename;
function createWindow() {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true,
            preload: path.join(__dirname, "preload.js")
        },
    })
    win.loadFile("chat/index.html")
}
app.whenReady()
.then(() => {
    createWindow()
    const platform = os.platform();
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
    const url = `https://github.com/hrutavmodha/voice-assistant/releases/download/build-36/${filename}`;
    const savePath = path.join(os.homedir(), filename);
    new Notification({
        title: "Installing!",
        body: "Installing executable file for your OS. Please wait a while..."
    }).show()
    fetch(url, {
        method: "GET"
    }).then(res => {
        if (!res.ok)
        new Notification({
            title: "Error!",
            body: "There is some network issue. Please try again later"
        }).show()
        return res.arrayBuffer();
    }).then(data => {
        fs.writeFileSync(savePath, Buffer.from(data));
        if (platform !== "win32")
        fs.chmodSync(savePath, 0o755);
        new Notification({
            title: "Success!",
            body: "The exeutable file of voice-assistant has been installed on your system successfully."
        }).show()
    }).catch(err =>
        new Notification({
            title: "Error!",
            body: "An error occured while installing the executable file for your OS. Please try again later"
        }).show()
    )
}).catch(error =>
    new Notification({
        title: "Error!",
        body: "An error occured while launching the application. Please try again later."
    }).show()
)
ipcMain.on("run", (e, args) => {
    const { cmd } = args
    const exeProcess = spawn(filename, [cmd])
    output = ""
    exeProcess.stdout.on("data", (data) => {
        output = output + data.toString()
    })
    exeProcess.stderr.on("data", (error) => {
        output = output + error.toString()
    })
    exeProcess.on("close", (event) => {
        event.sender.on("output", output)
    })
})
app.on("window-all-closed", () => {
    if (process.platform !== "darwin")
    app.quit()
})