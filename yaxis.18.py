import cv2
import numpy as np

def sobel_edge_detection_y(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    
    # Calculate the Sobel gradient along the Y axis
    sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
    
    # Convert back to uint8
    sobel_y = np.uint8(np.absolute(sobel_y))
    
    return sobel_y

# Read the input image
image = cv2.imread("C:\python.d\python.d\output_images\original_image.png")

# Perform Sobel edge detection along Y axis
edges_y = sobel_edge_detection_y(image)

# Display the result
cv2.imshow('Original Image', image)
cv2.imshow('Sobel Edge Detection (Y-axis)', edges_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
