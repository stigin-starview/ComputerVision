import cv2 

# Reading image file.
img = cv2.imread("resources/drum.jpg",0)

print(img.shape)

resized_image = cv2.resize(img, (int(img.shape[1]/3),int(img.shape[0]/3)))
cv2.imshow("drums",resized_image)
cv2.imwrite("drums_resized.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()