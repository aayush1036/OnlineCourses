import cv2 

img = cv2.imread('../Resources/Photos/group 1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haar_cascade = cv2.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=1)

print(f'Number of faces found -> {len(faces_rect)}')
# Haar cascade is sensitive to noise
# Minimizing scaleFactor and minNeighbors makes opencv 
# more prone to noise 
for (x,y,w,h) in faces_rect:
    cv2.rectangle(
        img,
        pt1 = (x,y),
        pt2 = (x+w, y+h),
        color = (0,255,0),
        thickness=2
    )

cv2.imshow('Detected Faces',img)
cv2.waitKey(0)