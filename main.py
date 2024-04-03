from modules.get_screen import capture
import cv2
import numpy as np
#import win32api, win32con, time


if __name__ == "__main__":
    im = capture()
    if im !=None:
        #template = cv2.imread('templates/btn_close.png', cv2.IMREAD_COLOR)
        template = cv2.imread('templates/sadovod.png', cv2.IMREAD_COLOR)
        tc,tw,th = template.shape[::-1]

        #template = cv2.cvtColor(template, cv2.COLOR_)
        #cv2.imshow("array",np.array(template))
        #cv2.waitKey()


        #cv2.imshow("array",np.asarray(im))
        #cv2.waitKey()
        #cv2.destroyAllWindows()

        

        img = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGBA2RGB)
        #cv2.imshow("img",img)
        


        #https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html
        res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        print("min="+str(min_loc)+"("+str(min_val)+");max="+str(max_loc)+"("+str(max_val)+");")

        cv2.rectangle(img, max_loc, (max_loc[0] + tw, max_loc[1] + th), (255,0,0), 3)

        threshold = 0.9
        loc = np.where( res >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + tw, pt[1] + th), (255,255,255), 1)
            print(pt)
        
        cv2.imshow("array",np.asarray(img))
        cv2.waitKey()
        cv2.destroyAllWindows()
            



    else:
        print("Bluestacks window not found")
    

    #time.sleep(10)