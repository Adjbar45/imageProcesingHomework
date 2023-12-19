import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the input image
image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the gamma value
gamma = 1.5

# Apply gamma correction
corrected_image = np.power(image/255.0, gamma)
corrected_image = (corrected_image * 255).astype(np.uint8)

# Display the original and corrected images
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(corrected_image, cmap='gray')
plt.title('Corrected Image')
plt.show()