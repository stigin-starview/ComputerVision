import cv2, time

# 2 second wait for me to move away from the camera.
time.sleep(2)
# study the cv2 documentation and impliment more fuction to the script------!!!!!

# Press Q to close the window / break the script

''' (cv2.CAP_DSHOW) is added because there is a bug in MSMF 
    backend of opencv while accessing the camera '''
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

first_frame = None

while True:

    check, frame = video.read()
    status = 0 
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
    
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status = 1
            
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    cv2.imshow("Color Frame", frame)
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    

    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break

video.release()


cv2.destroyAllWindows()
