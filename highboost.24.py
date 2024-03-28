import cv2
import numpy as np

def sharpen_image(image, boost_factor=1.0):
    # Define a 3x3 Laplacian kernel for edge detection
    laplacian_kernel = np.array([[0, -1, 0],
                                 [-1, 4, -1],
                                 [0, -1, 0]])

    # Apply the Laplacian kernel to the image
    laplacian = cv2.filter2D(image, -1, laplacian_kernel)

    # Create a high-boost mask
    high_boost_mask = np.array([[-1, -1, -1],
                                [-1, boost_factor + 8, -1],
                                [-1, -1, -1]])

    # Apply the high-boost mask to the Laplacian image
    sharpened_image = cv2.filter2D(laplacian, -1, high_boost_mask)

    return sharpened_image

# Read the input image
image = cv2.imread("C:\python.d\python.d\output_images\original_image.png")

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform sharpening with a boost factor of 1.5
sharpened_image = sharpen_image(gray_image, boost_factor=1.5)

# Display the original and sharpened images
cv2.imshow('Original Image', gray_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

