import cv2 

def rescaleFrame(frame, scale=0.75):
    """Works for anything"""
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

def changeRes(width, height):
    """Works for live videos only by using capture.set()
    3 references the width 
    4 references the height 
    read documentation to find out more properties that we can change 
    """
    capture.set(3,width)
    capture.set(4, height)

capture = cv2.VideoCapture('../Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame,scale=0.2)
    # Show the video frame by frame 
    cv2.imshow('Video Resized',frame_resized)
    # if d is pressed, break out of the loop
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()