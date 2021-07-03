import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
# cap.set(cv2.CAP_PROP_FPS, 60)

segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()

# imgBG = cv2.imread("BackgroundImages/3.jpg")

listImg = os.listdir("BackgroundImages")
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'BackgroundImages/{imgPath}')
    imgList.append(img)

indexImg = 0

while True:
    success, img = cap.read()
    # imgOut = segmentor.removeBG(img, (255,0,255), threshold=0.83)
    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.8)

    imgStack = cvzone.stackImages([img, imgOut], 2,1)
    _, imgStack = fpsReader.update(imgStack)
    print(indexImg)
    cv2.imshow("image", imgStack)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg>0:
            indexImg -=1
    elif key == ord('d'):
        if indexImg<len(imgList)-1:
            indexImg +=1
    elif key == ord('q'):
        break

