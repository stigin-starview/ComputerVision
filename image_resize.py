import cv2
import glob 

# Reading image file.
img = cv2.imread("resources/drum.jpg",0)

print(img.shape)

resized_image = cv2.resize(img, (int(img.shape[1]/3),int(img.shape[0]/3)))
cv2.imshow("drums",resized_image)
cv2.imwrite("drums_resized.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


def ImgResize(images):
    for image in images:
        img = cv2.imread(image,1)
        resized_image = cv2.resize(img, (400,400))
        cv2.imshow("hello", resized_image)
        cv2.waitKey(200)
        cv2.destroyAllWindows()
        cv2.imwrite("resources/resized/resized_" + image[10:] , resized_image)   
        print(image[10:])

images = glob.glob("resources/*.jpg")

ImgResize(images)
