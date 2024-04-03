def capture():
    import win32ui, win32con, win32gui
    from PIL import Image
    import numpy as np
    import cv2

    hwnd = win32gui.FindWindow(None, "Bluestacks App Player")

    if hwnd == 0:
        return None
    
    isiconic = False
    if win32gui.IsIconic(hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWNOACTIVATE)
        isiconic = True

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

    bmpinfo = dataBitMap.GetInfo()
    bmpstr = dataBitMap.GetBitmapBits(True)
    im = Image.frombuffer('RGBA', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'RGBA', 0, 1)

#    cv2.imshow("array",np.asarray(im))
#    cv2.waitKey()
#    cv2.destroyAllWindows()


    if isiconic:
        win32gui.ShowWindow(hwnd,win32con.SW_SHOWMINIMIZED)
    return im,rect

if __name__ == "__main__":
    for i in range(10):
        capture()