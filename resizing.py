import cv2

img = cv2.imread('BackgroundImages/4.jpg')
img = cv2.resize(img, (640,480))
# cv2.imshow("img", img)
# cv2.waitKey(0)
cv2.imwrite("5.jpg", img)