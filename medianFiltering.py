import cv2
import numpy as np

def median_filter(image, kernelSize):
    # Apply median filtering to the image
    filtered_image = cv2.medianBlur(image, kernelSize)
    
    return filtered_image

# Load the image
img = cv2.imread('image.jpg')

# Convert the image to grayscale
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Specify the kernel size for median filtering
kernel_size = 5

# Perform median filtering
filtered_image = median_filter(grayImage, kernel_size)

# Display the original and filtered images
cv2.imshow('Original Image', grayImage)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()