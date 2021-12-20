import cv2
img = cv2.imread("resources/drum.jpg",1)

cv2.imshow("drums",img)
cv2.waitKey(10000)
cv2.destroyAllWindows()

