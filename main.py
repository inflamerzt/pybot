from modules.get_screen import capture
import cv2
import numpy as np
#import win32api, win32con, time


if __name__ == "__main__":
    im = capture()
    if im !=None:
        cv2.imshow("array",np.asarray(im))
        cv2.waitKey()
        cv2.destroyAllWindows()
    else:
        print("Bluestacks window not found")
    

    #time.sleep(10)