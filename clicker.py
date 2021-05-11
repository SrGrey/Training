''' App preventing sleep mode '''
import pyautogui
import time
from datetime import datetime


print('you main display resolution is: ', pyautogui.size())
timelapse = int(input("how long you will out in minuts?")) * 60 // 12
print('script staring on: ', datetime.now())
for i in range(timelapse):
    total_sec = (timelapse - i) * 12
    minute = total_sec // 60
    secunds = total_sec - minute * 60
    print(f'{minute}:{secunds} left.')
    if (timelapse - i) % 5 == 0:
        print('For quit go to script window and press "Ctrl" + "C"') 
    pyautogui.moveTo(200, 800, duration=0.2)
    pyautogui.rightClick(200, 800, duration=0.2)
    pyautogui.press ('esc')
    time.sleep(5)    
    pyautogui.moveTo(800, 200, duration=0.2)
    pyautogui.rightClick(800, 200, duration=0.2)
    pyautogui.press ('esc')
    time.sleep(5) 
print('script stopped on: ', datetime.now())

# App created for prevent Sleep Mode when Power settings restricted by group policy.
# It possible create .exe version using pyinstaller (if you don't have it you need install it (http://www.pyinstaller.org/):
# - create C:\TEMP\Clicker\
# - add the icon file you want
# - add clicker.py file
# - pyinstaller -F -i "C:\TEMP\Clicker\click.ico" clicker.py
# Enjoy!
