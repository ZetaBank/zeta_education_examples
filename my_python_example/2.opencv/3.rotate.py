import cv2

image = cv2.imread('image.jpg')
rows, cols = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 180, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()