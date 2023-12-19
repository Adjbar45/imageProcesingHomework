import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the input image
image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the Sobel operator kernels
sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

sobel_y = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]])

# Apply the Sobel operator to the image
gradient_x = cv2.filter2D(image, -1, sobel_x)
gradient_y = cv2.filter2D(image, -1, sobel_y)

# Compute the magnitude of the gradients
gradient_magnitude = np.sqrt(np.square(gradient_x) + np.square(gradient_y))

# Normalize the gradient magnitude to the range [0, 255]
gradient_magnitude = gradient_magnitude * (255.0 / np.max(gradient_magnitude))

# Convert the gradient magnitude to the uint8 data type
gradient_magnitude = gradient_magnitude.astype(np.uint8)

# Display the original image and the gradient magnitude
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(gradient_magnitude, cmap='gray')
plt.title('Gradient Magnitude')
plt.show()