import cv2

print (cv2.__version__)



color_image = cv2.imread("/Users/islomovic_j/PyCharmMiscProject/fruit basket.jpg")
shape = color_image.shape
print(shape)
grayscale_image = cv2.imread('/Users/islomovic_j/PyCharmMiscProject/fruit basket.jpg', cv2.IMREAD_GRAYSCALE)
binary= cv2.threshold(grayscale_image,50,255,cv2.THRESH_BINARY)[1]
cv2.imshow("fruit basket",binary)

cv2.waitKey(0)
