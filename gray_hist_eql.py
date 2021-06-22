import cv2
import matplotlib.pyplot as plt


image1 = cv2.imread('dark1.jpg')
image2 = cv2.imread('mid1.jpg')
image3 = cv2.imread('light1.jpg')

gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray_image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)

eql_grayscale_image1 = cv2.equalizeHist(gray_image1)
eql_grayscale_image2 = cv2.equalizeHist(gray_image2)
eql_grayscale_image3 = cv2.equalizeHist(gray_image3)

plt.imshow(eql_grayscale_image1, cmap='gray')
plt.show() #equalized_image
plt.imshow(eql_grayscale_image2, cmap='gray')
plt.show() #equalized_image
plt.imshow(eql_grayscale_image3, cmap='gray')
plt.show() #equalized_image



#graph of the equalized image
histogram1 = cv2.calcHist([eql_grayscale_image1], [0], None, [256], [0, 256])
plt.plot(histogram1, color='k')
plt.xlim([0, 256])
plt.show()

histogram2 = cv2.calcHist([eql_grayscale_image2], [0], None, [256], [0, 256])
plt.plot(histogram2, color='k')
plt.xlim([0, 256])
plt.show()

histogram3 = cv2.calcHist([eql_grayscale_image3], [0], None, [256], [0, 256])
plt.plot(histogram3, color='k')
plt.xlim([0, 256])
plt.show()
