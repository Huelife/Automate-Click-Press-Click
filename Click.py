#Click.py: Automate 950 entry deletions

import pyautogui
import time

#Declare variables
target_1 = pyautogui.locateCenterOnScreen("Capture_1.png",confidence=0.85)
target_2 = pyautogui.locateCenterOnScreen("Capture_2.png",confidence=0.85)

#Automate 950 deletion instances
time.sleep(5)          #Sleep for 5 seconds
for x in range(950):
    time.sleep(0.5)          #Sleep for 0.5 second
    pyautogui.click(target_1)     #Move the mouse to target_1 coordinates and click
    time.sleep(0.5)          #Sleep for 0.5 second
    pyautogui.press("enter")     #Press the Enter key
    time.sleep(2)          #Sleep for 2 seconds
    pyautogui.click(target_2)     #Move the mouse to target_2 coordinates and click
    time.sleep(1)          #Sleep for 1 second
