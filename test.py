import cv2
import numpy as np

# Load the image
image_path = 'C:\pic.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Threshold the image to create a binary image
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# Calculate the number of white pixels (assumed as "1")
number_of_ones = np.count_nonzero(binary_image == 255)

print(f"Number of '1's in the image: {number_of_ones}")
