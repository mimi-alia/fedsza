from PIL import ImageGrab
from pynput import mouse
import pyautogui as gui
import time

'''
1.) return mouse coordinates
    a.) tone down to only report every so often
2.) return hex of mouse coordinates
'''

def getMouseLoc():
    return gui.position()

def getColor(x,y):
    return false

def delayPrint(stuff):
    time.sleep(1)
    print(stuff)


if __name__ == "__main__":
    print("SCRIPT IS RUNNING!!")
    while True:
        delayPrint(getMouseLoc())
        
    
