import cv2
import numpy as np

def sharpen_image(image, alpha=1.0):
    # Define a 3x3 kernel for gradient calculation
    kernel_x = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])

    kernel_y = np.array([[-1, -2, -1],
                         [0, 0, 0],
                         [1, 2, 1]])

    # Apply Sobel filters to calculate gradients in x and y directions
    gradient_x = cv2.filter2D(image, -1, kernel_x)
    gradient_y = cv2.filter2D(image, -1, kernel_y)

    # Combine gradients to obtain magnitude and direction
    gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
    gradient_direction = np.arctan2(gradient_y, gradient_x)

    # Calculate the sharpened image using gradient masking
    sharpened_image = image + alpha * gradient_magnitude

    # Ensure pixel values are within the valid range [0, 255]
    sharpened_image = np.clip(sharpened_image, 0, 255)

    # Convert back to uint8
    sharpened_image = np.uint8(sharpened_image)

    return sharpened_image

# Read the input image
image = cv2.imread("C:\python.d\python.d\output_images\original_image.png")

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform sharpening with an alpha value of 1.5
sharpened_image = sharpen_image(gray_image, alpha=1.5)

# Display the original and sharpened images
cv2.imshow('Original Image', gray_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
