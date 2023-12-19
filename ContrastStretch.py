import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the input image
image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Set the desired minimum and maximum intensity values
desired_min = 0
desired_max = 255

# Calculate the current minimum and maximum intensity values
current_min = np.min(image)
current_max = np.max(image)

# Perform contrast stretching
stretched_image = (image - current_min) * ((desired_max - desired_min) / (current_max - current_min)) + desired_min

# Clip the intensity values to ensure they fall within the desired range
stretched_image = np.clip(stretched_image, desired_min, desired_max)

# Convert the image to uint8 data type
stretched_image = stretched_image.astype(np.uint8)

# Display the original and stretched images
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(stretched_image, cmap='gray')
plt.title('Stretched Image')
plt.show()