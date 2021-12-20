import cv2 

# Reading image file.
img = cv2.imread("resources/drum.jpg",0)

cv2.imshow("drums",img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
