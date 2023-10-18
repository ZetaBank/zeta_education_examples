import cv2
import numpy as np

# Load an image
image = cv2.imread('image.jpg')

# Apply Gaussian blur using OpenCV
blurred_image_cv2 = cv2.GaussianBlur(image, (5, 5), 0)

# Create a Gaussian kernel using NumPy
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]]) / 16.0

# Apply convolution using NumPy
blurred_image_numpy = cv2.filter2D(image, -1, kernel)

# Add text labels to the images
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'Original', (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(blurred_image_cv2, 'OpenCV', (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(blurred_image_numpy, 'NumPy', (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Combine the original image, OpenCV blurred image, and NumPy blurred image horizontally
combined_image = np.hstack((image, blurred_image_cv2, blurred_image_numpy))

# Display the combined images
cv2.imshow('Image Blurring', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
