import cv2
import matplotlib.pyplot as plt 
# OpenCV reads image in BGR whereas we use RBG
boston = cv2.imread('../Resources/Photos/park.jpg')
# Converting BGR to grayscale - shows distribution of pixel intensity 
# in the image
grayscale = cv2.cvtColor(boston, cv2.COLOR_BGR2GRAY)
# Converting BGR to HSV (hue saturation value)
hsv = cv2.cvtColor(boston, cv2.COLOR_BGR2HSV)
# Converting BGR to LAB
lab = cv2.cvtColor(boston, cv2.COLOR_BGR2LAB)
# Convert bgr to rgb for libraries outside OpenCV
# plt.axis('off')
# plt.imshow(cv2.cvtColor(boston, cv2.COLOR_BGR2RGB))
# plt.show()
rgb = cv2.cvtColor(boston, cv2.COLOR_BGR2RGB)
# We cannot convert grayscale to hsv directly 
# HSV to BGR 
# Then BGR to HSV 
cv2.imshow('RGB',rgb)

cv2.waitKey(0)