import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("C:\python.d\python.d\output_images\original_image.png")
img = cv2.resize(img,(600,600))
cv2.imshow("image",img)
cv2.waitKey(0)
