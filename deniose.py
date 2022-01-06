import cv2, time, numpy
from datetime import datetime
from matplotlib import pyplot

# Press Q to close the window / break the script

# more work and integration is needed in here.

''' (cv2.CAP_DSHOW) is added because there is a bug in MSMF 
    backend of opencv while accessing the camera '''
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

first_frame = None
status_list = [None, None]

while True:

    check, frame = video.read()
    for_dn = [video.read()[1] for i in range(5)]
    for_dn_grey = [cv2.cvtColor(i, cv2.COLOR_BGR2GRAY) for i in for_dn]
    for_dn_grey =[numpy.float64(i) for i in for_dn_grey]
    noise = numpy.random.randn(*for_dn_grey[1].shape)*10
    noisy = [i+noise for i in for_dn_grey]
    noisy = [numpy.uint8(numpy.clip(i,0,255)) for i in noisy]
    dst = cv2.fastNlMeansDenoisingMulti(noisy, 2, 5, None, 4, 7, 35)

    pyplot.subplot(131),pyplot.imshow(for_dn_grey[2], 'gray')
    pyplot.subplot(132),pyplot.imshow(noisy[2], 'gray')
    pyplot.subplot(133),pyplot.imshow(dst, 'gray')
    pyplot.show()
    cv2.imshow("Color Frame", frame)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = cv2.GaussianBlur(gray,(21,21),0)

    # if first_frame is None:
    #     first_frame = gray
    #     continue
    # #comparing absdiff and making delta images
    # delta_frame = cv2.absdiff(first_frame, gray)
    # #using cv2.threshold method to create threshold frames
    # thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    # #smoothening the thereshold images.
    # thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
    
    # (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # for contour in cnts:
    #     if cv2.contourArea(contour) < 1000:
    #         continue
    #     status = 1
            
    #     (x, y, w, h) = cv2.boundingRect(contour)
    #     cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    # cv2.imshow("Color Frame", frame)
    # cv2.imshow("Gray Frame", gray)
    
          
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    
video.release()

cv2.destroyAllWindows()