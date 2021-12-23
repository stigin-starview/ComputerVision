import cv2

# Reading the xml file which contain face detection functions.
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Enter the image file location.
img = cv2.imread("resources/photo.jpg")

#converting the file to grey scale for better accuracy
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Using the functions in the xml file.

faces = face_cascade.detectMultiScale(gray_img,
scaleFactor = 1.2800,
minNeighbors = 5)

for x, y, w, h in faces:

    ''' cv2 rectangle argument take 4 arguments
    1.height and width from where the rectangle to begin (x,y).
    2. the height and weidth of the face (w, h).
    3. color of the rectangle.
    4. width of the rectangle. '''

    img =  cv2.rectangle(img, (x,y),(x+w, y+h),(0, 255, 0), 3)
print(type(faces))
print(faces)

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Faces", resized)
cv2.waitKey(0)
cv2.destryAllWindows()
