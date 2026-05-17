import cv2
import numpy as np
from PIL import ImageGrab
import time
import win32gui

def find_bluestacks_window():
    windows = []
    
    def callback(hwnd, extra):
        if "BlueStacks" in win32gui.GetWindowText(hwnd):
            extra.append(hwnd)
    
    win32gui.EnumWindows(callback, windows)
    
    if windows:
        return windows[0]  # Return the first BlueStacks window found
    return None


print("Looking for BlueStacks window...")
window_handle = find_bluestacks_window()

if window_handle:
    print("Found BlueStacks window!")
    print("Window handle:", window_handle)
else:
    print("Could not find BlueStacks. Make sure it's running.")
