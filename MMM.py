''' Move mouse, move..'''
import pyautogui
import time
from datetime import datetime

#pyautogui.moveTo (x, y, duration = num_seconds)
now = datetime.now()
#print(pyautogui.size())
timelapse = int(input("how long you will out in minuts?")) * 60 // 12
print(f'{timelapse} cycles')
print(now)
#while key != "s":
for i in range(timelapse):
#    time.sleep(1)
    print(f'{timelapse - i} cycles left. For quit move/'
    'the mouse to the top-left corner quickly')
#    pyautogui.moveTo(300, 300, duration=3)
    pyautogui.moveTo(300, 600, duration=5.5)
    pyautogui.rightClick(300, 600, duration=0.5)
    pyautogui.press ('esc')
#    pyautogui.moveTo(600, 600, duration=3)
    pyautogui.moveTo(600, 300, duration=5.5)
    pyautogui.rightClick(600, 300, duration=0.5)
    pyautogui.press ('esc')
