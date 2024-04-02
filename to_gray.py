import matplotlib.pyplot as plt
import numpy as np
import cv2

# x = np.linspace(0,20,100)
# plt.plot(x, np.sin(x))
# plt.show()

def loading_displaying_saving():
    img = cv2.imread('girl.jpg', cv2.IMREAD_GRAYSCALE)
    
    print("Высота:"+str(img.shape[0]))
    print("Ширина:" + str(img.shape[1]))
    #print("Количество каналов:" + str(img.shape[2]))
    print(str(len(img.shape)))

    cv2.imshow('girl', img)
    cv2.waitKey(0)
    cv2.imwrite('graygirl.jpg', img)




loading_displaying_saving()