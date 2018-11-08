import cv2

face_cascade = cv2.CascadeClassifier('/home/miguel/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

	cv2.imshow('img',img)
	if cv2.waitKey(33) == 27:
		break
cv2.destroyAllWindows()
	




