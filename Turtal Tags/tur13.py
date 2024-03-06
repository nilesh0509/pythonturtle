import pyautogui
import time
time.sleep(3)
count=0
while count <=100:
    
    pyautogui.typewrite('''Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.''')
    pyautogui.press("enter")
    count=count+1