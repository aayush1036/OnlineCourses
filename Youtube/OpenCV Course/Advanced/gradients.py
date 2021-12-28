import cv2
import numpy as np
img = cv2.imread('../Resources/Photos/park.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Laplacian edge detection 
lap = cv2.Laplacian(src=gray,ddepth=cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
# Sobel
sobelx = cv2.Sobel(
    src=gray,
    ddepth=cv2.CV_64F,
    dx=1,
    dy=0
) 

sobely = cv2.Sobel(
    src=gray,
    ddepth=cv2.CV_64F,
    dx=0,
    dy=1
) 

combined_sobel = cv2.bitwise_or(
    src1=sobelx,
    src2=sobely
)

# Canny edge detection 
canny = cv2.Canny(
    image=gray,
    threshold1=150,
    threshold2=175
)
cv2.imshow('Laplacian',lap)
cv2.imshow('Sobel', combined_sobel)
cv2.imshow('Canny',canny)
cv2.waitKey(0)