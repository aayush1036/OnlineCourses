import cv2
import matplotlib.pyplot as plt 
import numpy as np

img = cv2.imread('../Resources/Photos/cats.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mask = cv2.circle(
    img = blank,
    center=(img.shape[1]//2, img.shape[0]//2),
    radius=100,
    color=255,
    thickness=-1
)
masked = cv2.bitwise_and(
    src1=img,
    src2 = img,
    mask=mask
)
# Grayscale histogram 
# gray_hist = cv2.calcHist(
#     images=[gray],
#     channels=[0], # specifies the index of the channel
#     mask=mask, 
#     histSize=[255], # number of bins in the histogram 
#     ranges=[0,256], # ranges of pixel values 
# )

# fig, ax = plt.subplots()
# ax.set_title('Grayscale Histogram')
# ax.set_xlabel('Bins')
# ax.set_ylabel('Number of Pixles')
# ax.plot(gray_hist)
# ax.set_xlim([0,256])
# plt.show()

# Color Histogram 
colors = ('b','g','r')
fig, ax = plt.subplots()
for i,col in enumerate(colors):
    hist = cv2.calcHist(
        images=[img],
        channels=[i],
        mask=mask,
        histSize=[256],
        ranges=[0,256]
    )
    ax.plot(hist,color=col)
    
ax.set_xlim([0,256])
ax.set_title('Color Histogram')
ax.set_xlabel('Bins')
ax.set_ylabel('Number of Pixles')
plt.show()
cv2.imshow('Masked',masked)
cv2.waitKey(0)