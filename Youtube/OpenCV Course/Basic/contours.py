import cv2 
import numpy as np
img = cv2.imread('../Resources/Photos/cats.jpg')

blank = np.zeros(img.shape, dtype='uint8')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(img, (5,5), cv2.BORDER_DEFAULT)
# canny = cv2.Canny(blur, 125,175)

ret, thresh = cv2.threshold(gray, 125,255,type=cv2.THRESH_BINARY)
# below 125 - black, above 255 - white, 
# THRESH_BINARY - binarizig the image


contours, heirarchies = cv2.findContours(
    thresh, 
    cv2.RETR_LIST, 
    cv2.CHAIN_APPROX_SIMPLE) # returns all the contours, 
    #CHAIN_APPROX_SIMPLE - compresses it into 2 points
# RETR_TREE - heirarchy
# RETR_EXTRENAL - only the external contours 
# RETR_LIST - all the contours in the image

print(f'The number of contours found is {len(contours)}')
cv2.drawContours(
    blank, 
    contours, 
    contourIdx=-1,
    color=(0,0,255), 
    thickness=1)
# contourIdx=-1 displays all contours
cv2.imshow('ContoursDrawn',blank)
cv2.waitKey(0)