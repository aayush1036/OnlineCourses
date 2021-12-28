import cv2
import numpy as np 

blank = np.zeros(shape=(400,400), dtype='uint8')
rectangle = cv2.rectangle(
    blank.copy(), 
    pt1=(30,30), 
    pt2=(370,370),
    color=255, 
    thickness=-1)

circle = cv2.circle(
    blank.copy(),
    center=(200,200),
    radius=200,
    color=255,
    thickness=-1
)
# cv2.imshow('Rectangle',rectangle)
# cv2.imshow('Circle',circle)

# Bitwise AND (intersection - present in both only)
bitwise_and = cv2.bitwise_and(
    src1=rectangle, 
    src2=circle)

# Bitwise OR (either present in 1 image)
bitwise_or = cv2.bitwise_or(
    src1=rectangle,
    src2 = circle
)
# Bitwise XOR (non intersecting regions, 
# either present in one but not in both)
bitwise_xor = cv2.bitwise_xor(
    src1 = rectangle,
    src2 = circle
)
# Bitwise NOT (inverts the color) 
rectangle_not = cv2.bitwise_not(
    src=rectangle
)

circle_not = cv2.bitwise_not(
    src=circle
)
cv2.imshow('Bitwise NOT',circle_not)
cv2.waitKey(0)