import cv2
img = cv2.imread('../Resources/Photos/cats.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Simple thresholding 
# if pixel val>150, set it to 255 else set it to 0
#thresh = image 
#thresh = 150
threshold, thresh = cv2.threshold(
    src=gray,
    thresh=150,
    maxval=255,
    type=cv2.THRESH_BINARY
)

# Inverse thresholded image (inverse of the previous image)
threshold, thresh_inv = cv2.threshold(
    src=gray,
    thresh=150,
    maxval=255,
    type=cv2.THRESH_BINARY_INV
)
# Adaptive thresholding 
adaptive_thresh = cv2.adaptiveThreshold(
    src=gray,
    maxValue=255,
    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    thresholdType=cv2.THRESH_BINARY_INV,
    blockSize=11,
    C=9
)

cv2.imshow('Adaptive Thresholded',adaptive_thresh)
cv2.waitKey(0)