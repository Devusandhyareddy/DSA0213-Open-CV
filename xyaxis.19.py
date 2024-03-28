import cv2
import numpy as np

def sobel_edge_detection(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    
    # Calculate Sobel gradients along X and Y axis
    sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
    
    # Compute the gradient magnitude
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    gradient_magnitude = np.uint8(gradient_magnitude)
    
    return gradient_magnitude

# Read the input image
image = cv2.imread("C:\python.d\python.d\output_images\original_image.png")

# Perform Sobel edge detection
edges = sobel_edge_detection(image)

# Display the result
cv2.imshow('Original Image', image)
cv2.imshow('Sobel Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
