import cv2

# Load the original image
original_image = cv2.imread("C:\python.d\python.d\output_images\original_image.png"
)

# Check if the original image is loaded successfully
if original_image is None or original_image.size == 0:
    print("Error: Unable to load original image.")
    exit()

# Load the watermark image
watermark = cv2.imread("C:\python.d\python.d\output_images\original_image.png"
, cv2.IMREAD_UNCHANGED)

# Check if the watermark image is loaded successfully
if watermark is None or watermark.size == 0:
    print("Error: Unable to load watermark image.")
    exit()

# Resize the watermark to match the size of the original image
watermark_resized = cv2.resize(watermark, (original_image.shape[1], original_image.shape[0]))

# Blend the images
alpha = 0.7  # Opacity of the watermark
beta = (1.0 - alpha)
watermarked_image = cv2.addWeighted(original_image, 1.0, watermark_resized, alpha, 0.0)

# Save the watermarked image
cv2.imwrite('watermarked_image.jpg', watermarked_image)

# Display the watermarked image
cv2.imshow('Watermarked Image', watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

