import cv2
img=cv2.imread("brainly.jpg")
gaussian_blur=cv2.GaussianBlur(img,(11,11),0)
cv2.imshow("GAUSSIAN BLUR",gaussian_blur)
cv2.imwrite("gaussian.png", gaussian_blur)
cv2.waitKey(0)
