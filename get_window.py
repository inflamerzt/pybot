#require pywin32

import win32gui
import win32ui
import win32con

w = 1920 # set this
h = 1080 # set this
bmpfilenamename = "out.bmp" #set this

# must define vindow name
windowname = "Bluestacks App Player"



hwnd = win32gui.FindWindow(None, windowname)

rect = win32gui.GetWindowRect(hwnd)
w = rect[2] - rect[0]
h = rect[3] - rect[1]

wDC = win32gui.GetWindowDC(hwnd)
dcObj=win32ui.CreateDCFromHandle(wDC)
cDC=dcObj.CreateCompatibleDC()
dataBitMap = win32ui.CreateBitmap()
dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
cDC.SelectObject(dataBitMap)
cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
dataBitMap.Paint(cDC,)

# Free Resources
dcObj.DeleteDC()
cDC.DeleteDC()
win32gui.ReleaseDC(hwnd, wDC)
win32gui.DeleteObject(dataBitMap.GetHandle())




# alt version copy to numpy array


import win32gui
import win32ui
import win32con
import numpy as np
from PIL import Image
import cv2  # Used for showing the NumPy array as image

w = 1920
h = 1080
hwnd = win32gui.FindWindow(None, "Bluestacks App Player")

rect = win32gui.GetWindowRect(hwnd)
w = rect[2] - rect[0]
h = rect[3] - rect[1]

wDC = win32gui.GetWindowDC(hwnd)
dcObj = win32ui.CreateDCFromHandle(wDC)
cDC = dcObj.CreateCompatibleDC()
dataBitMap = win32ui.CreateBitmap()
dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
cDC.SelectObject(dataBitMap)
cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)

# https://stackoverflow.com/questions/6951557/pil-and-bitmap-from-winapi
bmpinfo = dataBitMap.GetInfo()
bmpstr = dataBitMap.GetBitmapBits(True)
im = Image.frombuffer('RGBA', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'RGBA', 0, 1)

array = np.asarray(im) # Convet to NumPy array



# Show image for testing
cv2.imshow('array', array)
cv2.waitKey()
cv2.destroyAllWindows()