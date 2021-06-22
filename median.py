import cv2
i=cv2.imread("noise image.png")
median=cv2.medianBlur(i,5)      
cv2.imshow("MEDIAN BLUR",median)
cv2.imwrite("MEDIUM BLUR.png",median)
cv2.waitKey(0)
