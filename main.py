from modules.get_screen import capture
import cv2
import numpy as np
from modules.template_match import match
#import win32api, win32con, time
import pyautogui


if __name__ == "__main__":
    im,window_rect = capture()
    print(window_rect)

    if im !=None:
        print(match('templates/sadovod.png',im))
        print(match('templates/btn_cross.png',im))
        #print(match('templates/btn_close.png',im,True))

        out = match('templates/btn_close.png',im)
        if out[0] > 0.85:
            pyautogui.moveTo(window_rect[0]+out[1][0]+int(out[2][0]/2), window_rect[1]+out[1][1]+int(out[2][1]/2))
            pyautogui.leftClick()
  
    else:
        print("Bluestacks window not found")
    

    #time.sleep(10)