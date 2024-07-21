#Click.py: Automate 950 entry deletions

import pyautogui
import time

#Declare variables
target_1 = pyautogui.locateCenterOnScreen("Screenshot_1.png",confidence=0.85)
target_2 = pyautogui.locateCenterOnScreen("Screenshot_2.png",confidence=0.85)

#Automate 950 deletion instances
for x in range(950):
    pyautogui.click(target_1)     #Move the mouse to target_1 coordinates and click
    pyautogui.press("enter")     #Press the Enter key
    time.sleep(1)          #Sleep for 1 second
    pyautogui.click(target_2)     #Move the mouse to target_2 coordinates and click
