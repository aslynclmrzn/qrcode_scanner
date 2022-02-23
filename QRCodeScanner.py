import cv2
from pyzbar.pyzbar import decode
import datetime
import numpy as np
cam = cv2.VideoCapture(0)
while True:
    _, img = cam.read()
    global data
    for qrcode in decode(img):
        data = qrcode.data.decode("utf-8")
        print(data) # printing detected qrcode text
        line = np.array([qrcode.polygon], np.int32) 
        line = line.reshape((-1,1,2))
        cv2.polylines (img,[line],True,(255, 0, 0),5) # lines on qrcode
        text = qrcode.rect
        cv2.putText(img,data,(text[0],text[1]),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.9,(0,255,0),2) # text on qrcode that will appear in webcam
        now = datetime.datetime.now() # date and time for the session
        date = (now.strftime("%m/%d/%Y %H:%M:%S"))
        file = open("datafile.txt",'w') # writing contents to txt file
        file.write("Session contents restored from: " + date + (f"\n\n\n\nQR Code Contents:\n{data}\n"))
        file.close()
    cv2.imshow('QRCodeScanner App', img)
    cv2.waitKey(1)