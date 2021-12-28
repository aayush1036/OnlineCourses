import cv2
img = cv2.imread('../Resources/Photos/park.jpg')
# Convert image to grayscale
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur an image 
blur = cv2.GaussianBlur(
    img,
    ksize=(7,7), # ksize should be odd number
    sigmaX=cv2.BORDER_DEFAULT)

# Create an edge cascade (find edges)
# Apply canny edge detection formula on the image
# # We can reduce the number of edges by applying blur 
canny = cv2.Canny(blur, 125,175)

# Dialate image using specific structuring element (edges)
dialated = cv2.dilate(canny, kernel=(7,7), iterations=3)

# Eroding the dialations 
eroded = cv2.erode(dialated, kernel=(7,7), iterations=3)

# Resize images (ignoring aspect ratio)
resized = cv2.resize(img, dsize=(500,500),interpolation=cv2.INTER_CUBIC)
# Crop images 
cropped = img[50:200, 200:400]
cv2.imshow('Cropped', cropped)
cv2.waitKey(0)