import cv2
import numpy as np
img = cv2.imread('../Resources/Photos/park.jpg')

# Translation (shifting along x or y axis or any combination)
def translate(img, x,y):
    transMat = np.float32([
        [1,0,x],
        [0,1,y]
    ])
    dimensions = (
        img.shape[1],
        img.shape[0]
    )
    return cv2.warpAffine(
        img,
        transMat,
        dimensions
    )

# negative x - left 
# negative y - up
# positive x - right 
# positive y - down 

translated = translate(img, -100,100)

def rotate(img, angle, rotPoint=None):
    (height, width)=img.shape[:2]
    if rotPoint == None: 
        rotPoint = (width//2, height//2)
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, scale=1.0)
    dimensions = (width,height)
    return cv2.warpAffine(img, rotMat, dimensions)
# positive - counter clockwise 
# negative - clockwise 
rotated = rotate(img, 45)
# Resizing 
resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)

# Shrinking - INTER_AREA or default
# Enlarging -  INTER_LINEAR, INTER_CUBIC
# INTER_CUBIC is preferred (slower but great quality)

# Flipping 
flipped = cv2.flip(img, flipCode=-1) 
# 0 - vertically
# 1 - horizontally 
# -1 - vertically and horizontally
# Croppig 
cropped = img[200:400, 300:400]
cv2.imshow('Cropped',cropped)
cv2.waitKey(0)