import cv2

img=cv2.imread("brainly.jpg")
avg_blur=cv2.blur(img,(11,11))
cv2.imshow("AVERAGING",avg_blur)

#cv2.imwrite("Averaing_img",avg_blur)
cv2.waitKey(0)
