# 🍏 macpy

## 📝 Description

### ❓ Why?

macpy was created to simplify interaction with Apple Silicon Macs through Python.  
It addresses the need for a **clean automation layer** that allows developers, power users, and productivity enthusiasts to script everyday macOS actions—without manually navigating system menus or relying on GUI tools.  
From closing apps to toggling system settings, macpy makes automation **predictable, scriptable, and reusable.**

### ⚙️ How?

macpy exposes Python-based controllers that interact with macOS services, **leveraging third-party modules** under the hood to execute system-level commands safely.  
Some capabilities **may require user-created Apple Shortcuts**, which macpy can trigger programmatically when needed, allowing deeper macOS integration while staying user-controlled.

By composing controllers into scripts, users can:
- open and close applications
- adjust system preferences (Wi-Fi, Bluetooth, volume, airdrop, low power mode, etc.)
- set wallpapers and visual accessibility options
- automate repetitive workflows
- define modes like *work*, *gaming*, or *focus* with a single command

### 👥 For Who?

This project is designed for:
- ⚡ Developers who want fast, scriptable macOS control
- 🧠 Productivity enthusiasts switching between presets like *work*, *gaming*, *travel*, or *focus*
- 🧪 Beginners learning Python who want **practical automation** examples
- 🤖 Anyone tired of manually clicking settings and launching apps every day

## 🎥 See in Action

Curious how macpy feels in real workflows?  
Watch a short demo showing mode switching, system changes, and app management:

👉 **YouTube:** <link_here>


## 📦 Requirements

Before using macpy, make sure the following are set up:

### ✔️ Software Requirements
- macOS on **Apple Silicon**
- **Homebrew**
- **Python 3.11+**
- **pip** package manager
- **Shortcuts** app (preinstalled on macOS)
- **Full Disk Access** granted to the terminal(recommended for stability)

### 🔌 Third-party Dependencies (installed via Homebrew)
macpy relies on several system tools to control display settings, Bluetooth, and system services.  
These are checked automatically by the helper script `dependencies.py`, but can also be installed manually:

| Name | Type | Purpose | Install Command |
|------|------|---------|----------------|
| `displayplacer` | formula | manage display resolution / HZ | `brew install displayplacer` |
| `blueutil` | formula | control Bluetooth from terminal | `brew install blueutil` |
| `cloudflare-warp` | cask | networking tool used by default scripts | `brew install --cask cloudflare-warp` |

### 🧩 Apple Shortcuts Required

Some macpy features rely on user-defined **Shortcuts** for deeper macOS integration.  
If they're missing, the helper script `dependencies.py` will warn you.

| Shortcut Name | Description |
|---------------|-------------|
| **Motion-on** | Turns motion on |
| **Motion-off** | Turns motion off |
| **Transparency-on** | Turns transparency on |
| **Transparency-off** | Turns transparency off |

> ⚠️ **Important:**  
> You must create these Shortcuts **manually** in the Shortcuts app using the *exact names* above.  
> The script will detect them automatically.

### 🧰 Automated Check

To verify that everything is installed correctly, run the helper script (in project root): 
```
python3 main.py dependencies
```

### ⚙️ System Tweaks
To improve reliability:
- allow your shell (Terminal / iTerm / Ghostty) **Full Disk Access**
- ensure **Shortcuts** can be executed from the command line
- disable "Ask to run shortcuts" confirmation prompts
- **configure sudo to run without password** for commands used by macpy  
  > You can do this by adding a line at the end of your sudoers file (`sudo visudo`) like:
  > ```
  > your_username ALL=(ALL) NOPASSWD: ALL
  > ```
  > Replace `your_username` with your actual macOS username.

## 💻 Installation
1. Clone the Git repository into your Mac home folder:
```
cd ~
git clone https://github.com/Anton-Blyzniuk/macpy.git
```
This will create the directory:
```
/Users/your_username/macpy
```

2. Set an alias in your terminal:
```
alias macpy="python3 /Users/your_username/macpy/main.py"
```
To make this alias persistent, add it to your ~/.zshrc or ~/.bashrc.

3. Run the dependencies check:
```
macpy dependencies
```
If everything was done correctly, you will see:

**✅ ready to operate ✅**

Otherwise, follow the instructions shown in the output.

4.	View the list of default scripts:
```
macpy list
```
This will display the list of available default scripts.

## 🛠️ Creating Custom Scripts with macpy

In this video, you’ll learn how to create and run your own custom scripts using **macpy**.
It covers the basic structure of a script, how macpy discovers it, and how to execute it from the terminal.

📺 **Watch the tutorial on YouTube:**  
https://youtu.be/nX5U1NlPPhE
## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📬 Contact

- **Author**: Anton Blyzniuk
- **Email**: bliznukantonmain@gmail.com
- **GitHub**: https://github.com/Anton-Blyzniuk
- **LinkedIn**: https://www.linkedin.com/in/anton-blyzniuk-python-dev/
