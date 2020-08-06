import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

while True:
    _, img = capture.read()
    #converting rbc image to gray scale image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #to detect faces in the captured image we use detectMultiScale()
    faces = face_cascade.detectMultiScale(gray_img, 1.3, 4) #for this gray scale image is given as parameter
    #after detecting the faces 
    #to identify image in the video capture rectangle is formed around the image
    for (x, y, w, h) in faces:
        cv2.rectangle(img,(x,y) ,(x + w, y + h), (0, 0, 255), 3)
        #cv2.circle(img, (120, 210), 63, (0, 0, 255), -1) 
    #displaying 
    cv2.imshow('img', img)
    k = cv2.waitKey(27) & 0xff
    if k == 27:
        break
capture.release()
cv2.destroyAllWindows()
        
    
