import cv2
import numpy as np

def bit_plane_slice(image, planeNumber):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Extract the binary representation of the gray image
    binary_image = np.unpackbits(gray_image, axis=1)
    binary_image = binary_image.reshape(gray_image.shape[0], gray_image.shape[1], 8)
    
    # Extract the specified bit plane
    bit_plane = binary_image[:, :, planeNumber]
    
    # Convert the bit plane back to a grayscale image
    bit_plane_image = np.packbits(bit_plane, axis=1)
    
    return bit_plane_image

# Load the image
image = cv2.imread('image.jpg')

# Specify the bit plane number to extract (0-7 for an 8-bit image)
plane_number = 7

# Perform bit plane slicing
bit_plane_image = bit_plane_slice(image, plane_number)

# Display the original and bit plane sliced images
cv2.imshow('Original Image', image)
cv2.imshow('Bit Plane Sliced Image', bit_plane_image)
cv2.waitKey(0)
cv2.destroyAllWindows()