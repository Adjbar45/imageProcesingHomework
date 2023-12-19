import cv2
import numpy as np

# Load the image
image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Laplacian filter
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Convert the result to uint8
laplacian = np.uint8(np.absolute(laplacian))

# Display the original and Laplacian filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Laplacian Filtered Image', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()