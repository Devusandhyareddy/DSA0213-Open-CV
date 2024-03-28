import cv2

# Load the main image
main_image = cv2.imread("C:\python.d\python.d\output_images\original_image.png")

# Load the image from which we want to crop a region
crop_image = cv2.imread("C:\python.d\python.d\output_images\original_image.png")

# Check if images are loaded successfully
if main_image is None or crop_image is None:
    print("Error: Unable to load images.")
    exit()

# Define the region of interest (ROI) in the main image
start_row, end_row = 100, 300
start_col, end_col = 200, 400
roi = main_image[start_row:end_row, start_col:end_col]

# Copy the ROI from the crop image
crop_height, crop_width = roi.shape[:2]
crop_image_resized = cv2.resize(crop_image, (crop_width, crop_height))

# Paste the copied region into the main image
main_image[start_row:end_row, start_col:end_col] = crop_image_resized

# Save the result
cv2.imwrite('result_image.jpg', main_image)

# Display the result
cv2.imshow('Result Image', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
