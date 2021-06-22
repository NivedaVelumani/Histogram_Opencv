import cv2
i=cv2.imread("girl1.jpg")
bblur=cv2.bilateralFilter(i,30,60,5)
cv2.imshow("BILATERAL FILTER", bblur)
cv2.imwrite("girl_bilated.png", bblur)
cv2.waitKey(0)
