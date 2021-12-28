import cv2 
import numpy as np 

# Creating a blank image 
blank = np.zeros((500,500,3), dtype='uint8')
# cv2.imshow('Blank',blank)

# Paint the image a certain color 
# blank[:] = 0,255,0 # Painting it green
# blank[200:300, 300:400] = 0,0,255 # Painting it red
# Draw a rectangle 
cv2.rectangle(
    blank, 
    pt1=(0,0),
    pt2=(blank.shape[0]//2,blank.shape[1]//2), 
    color=(0,255,0),thickness=-1)
# thickness = -1 for filling the circle 

# Draw a circle 
cv2.circle(
    blank, 
    center=(blank.shape[0]//2, blank.shape[1]//2),
    radius=40,
    color=(0,0,255),
    thickness=-1)

# Draw a line 
cv2.line(
    blank, 
    pt1 = (100,250),
    pt2 = (300, 400),
    color = (255,255,255),
    thickness=3
)
# Write text 
cv2.putText(
    img=blank,
    text = 'Hello, my name is Aayushmaan',
    org=(0,225),
    fontFace=cv2.FONT_HERSHEY_TRIPLEX,
    fontScale=0.75, 
    color=(0,255,255),
    thickness=2
)

# img = cv2.imread('Resources/Photos/cat.jpg')
cv2.imshow('Text',blank)
cv2.waitKey(0)