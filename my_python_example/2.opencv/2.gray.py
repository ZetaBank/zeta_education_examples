import cv2

image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()