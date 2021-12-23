import cv2, time
# study the cv2 documentation and impliment more fuction to the script------!!!!!

# Press Q to close the window / break the script

''' (cv2.CAP_DSHOW) is added because there is a bug in MSMF 
    backend of opencv while accessing the camera '''
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

first_frame = None

while True:

    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue
    #comparing absdiff and making delta images
    delta_frame = cv2.absdiff(first_frame, gray)
    #using cv2.threshold method to create threshold frames
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    #smoothening the thereshold images.
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)


    cv2.imshow("captures", frame)
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    

    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break

video.release()


cv2.destroyAllWindows()

