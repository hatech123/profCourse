import  cv2
cap=cv2.VideoCapture("mouse.mp4")
first_frame=cap.read()[1]
hmin=(0,71,110)
hmax=(141,255,255)
cv2.imwrite("mouse.jpg",first_frame)
while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
    thresh=cv2.inRange(hsv,hmin,hmax)
    cv2.imshow("frame",frame)
    cv2.imshow("HSV",hsv)
    cv2.imshow("thresh",thresh)
    cv2.waitKey(1)
