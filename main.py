from modules.get_screen import capture
import cv2
import numpy as np
#import win32api, win32con, time


if __name__ == "__main__":
    im = capture()
    if im !=None:
        #template = cv2.imread('btn_close.png', cv2.IMREAD_COLOR)
        template = cv2.imread('sadovod.png', cv2.IMREAD_COLOR)
        tc,tw,th = template.shape[::-1]

        #template = cv2.cvtColor(template, cv2.COLOR_)
        #cv2.imshow("array",np.array(template))
        #cv2.waitKey()


        #cv2.imshow("array",np.asarray(im))
        #cv2.waitKey()
        #cv2.destroyAllWindows()

        

        img = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGBA2RGB)
        
        res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where( res >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + tw, pt[1] + th), (0,0,255), 2)
        
        cv2.imshow("array",np.asarray(img))
        cv2.waitKey()
        cv2.destroyAllWindows()
            



    else:
        print("Bluestacks window not found")
    

    #time.sleep(10)