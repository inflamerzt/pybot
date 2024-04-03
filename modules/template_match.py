import cv2
import numpy as np


def showsection(image,section):
    precision, max_loc, dimensions = section
    tw,th = dimensions

    if precision > 0.8:
        cv2.rectangle(image, max_loc, (max_loc[0] + tw, max_loc[1] + th), (255,0,0), 3)
    cv2.rectangle(image, max_loc, (max_loc[0] + tw, max_loc[1] + th), (0,0,255), 1)

    cv2.imshow("array",np.asarray(image))
    cv2.waitKey()
    cv2.destroyAllWindows()

def match(mtemplate,mimage,display = None):
    template = cv2.imread(mtemplate, cv2.IMREAD_COLOR)
    tc,tw,th = template.shape[::-1]
    img = cv2.cvtColor(np.asarray(mimage), cv2.COLOR_RGBA2RGB)
            
    res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    print("min="+str(min_loc)+"("+str(min_val)+");max="+str(max_loc)+"("+str(max_val)+");")

    #if max_val > 0.8:
    #    cv2.rectangle(img, max_loc, (max_loc[0] + tw, max_loc[1] + th), (255,0,0), 3)
    
    #cv2.rectangle(img, max_loc, (max_loc[0] + tw, max_loc[1] + th), (0,0,255), 1)
    if display:
        showsection(img,(max_val,max_loc,(tw,th)))
    #cv2.imshow("array",np.asarray(img))
    #cv2.waitKey()
    #cv2.destroyAllWindows()

    return (max_val,max_loc,(tw,th))

def match_reference():
    if False:#im !=None:
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

        if max_val > 0.8:
            cv2.rectangle(img, max_loc, (max_loc[0] + tw, max_loc[1] + th), (255,0,0), 3)

        threshold = 0.9
        loc = np.where( res >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + tw, pt[1] + th), (255,255,255), 1)
            print(pt)
        
        cv2.imshow("array",np.asarray(img))
        cv2.waitKey()
        cv2.destroyAllWindows()