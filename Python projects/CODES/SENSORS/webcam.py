import cv2

webCam = cv2.VideoCapture(0)

camx = 100
camy = 50
camw = 250
camh = 550

while True :
    _, frame = webCam.read()
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    resize = cv2.resize(frame, (176, 204)) 
    cv2.rectangle(frame,(camx,camy),(camx+camw,camy+camh),(0,255,0),2)
    cv2.imshow("cam", frame)
    cv2.imshow("cam2", resize)
    #cv2.imwrite('test.jpg', frame)
    #break;
    cv2.waitKey(1)

