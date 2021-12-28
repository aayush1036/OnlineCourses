import cv2
img = cv2.imread('../Resources/Photos/cats.jpg')

# Blurring, kernel size should be odd numbers 
# Averaging (computes the average of all the pixels in the window)
# Better than gaussian blur 
average = cv2.blur(
    src=img, 
    ksize=(3,3)
)

# Gaussian Blur - uses Gaussian formula, not the best 
# Computes some weights and then average of products of the weight 
gauss = cv2.GaussianBlur(
    src=img,
    ksize=(3,3),
    sigmaX=0
)
# Median Blur - Computes the median of all pixels in the window 
# Good in removing noise in image 
# Better than gaussian and average blur, 
# not meant for higher kernel sizes
median = cv2.medianBlur(
    src=img,
    ksize=3
)
# Bilateral blurring - most effective 
# applies blurring but retains the edges in the image 
# sigmaColor - retains the colors in the image, larger value retain more color
# sigmaSpace  pixels farther out will influence the blurring 
# larger value of sigmaSpace means pixels from farther away will 
# influence the blurring 
bilateral = cv2.bilateralFilter(
    src=img,
    d=5,
    sigmaColor=15,
    sigmaSpace=15
)
cv2.imshow('Bilarteral Blur',bilateral)
cv2.waitKey(0)