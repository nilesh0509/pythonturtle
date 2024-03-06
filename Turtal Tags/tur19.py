import pyautogui
import time
time.sleep(3)
count=1
while count<=100:
    pyautogui.typewrite('0'+str(count))
    pyautogui.press('enter')
    count= count+1