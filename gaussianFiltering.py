import cv2

def gaussian_filter(image):
    # Apply Gaussian filtering to the image
    filtered_image = cv2.GaussianBlur(image, (0, 0), 1)
    
    return filtered_image

# Load the image
image = cv2.imread('image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform Gaussian filtering
filtered_image = gaussian_filter(gray_image)

# Display the original and filtered images
cv2.imshow('Original Image', gray_image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()