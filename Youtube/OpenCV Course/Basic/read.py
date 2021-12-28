import cv2
"""
img = cv2.imread('Resources/Photos/cat_large.jpg')
cv2.imshow('Cat',img)
# cv2.waitkey(0) - Waits for an infinite amount of time for a key to be pressed 
cv2.waitKey(0) 
"""

# The image goes off screen 
# We can resize the image to support the monitor 

# Reading videos 
capture = cv2.VideoCapture('../Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    # Show the video frame by frame 
    cv2.imshow('Video',frame)
    # if d is pressed, break out of the loop
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()
