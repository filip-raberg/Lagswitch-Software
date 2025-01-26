import tkinter as tk
import os
import keyboard
import time

command = 'ctrl+l' # the command that activates the force paste

def commandpressed(): # function for when command is pressed
    os.system("ipconfig /release")
    time.sleep(4)
    os.system("ipconfig /renew")

keyboard.add_hotkey(command, commandpressed)

keyboard.wait() # make sure application does not close