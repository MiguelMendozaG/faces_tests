import cv2
import imutils
import dlib
import os
import serial, time

arduino = serial.Serial('/dev/ttyACM0', 9600)

#definicion de la direccion del archivo
svm_file = "dataset_abierto.svm"

#se carga el archivo svm entrenado
detector = dlib.simple_object_detector(svm_file)

#capturamos video
cap = cv2.VideoCapture(0)


#se despliega detector hog en escala de grises
win_det =dlib.image_window()
win_det.set_image(detector)

win = dlib.image_window()


#ciclo, donde se analizan cada una de las imagenes capturadas por la webcam y se enmarca el objeto encontrado
while True:
	ret, image = cap.read()
	image = imutils.resize(image, width = 400)

	rects = detector(image)
	if (rects):
		arduino.write(('Q').encode('utf-8'))
	else:
		arduino.write(('W').encode('utf-8'))

	for k, d in enumerate(rects):
		print("Objeto de interes {}: Izq: {}, Sup: {}, Der: {}, Inf: {}". format(k,d.left(), d.top(), d.right(), d.bottom()))


	win.clear_overlay()
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	win.set_image(image)
	win.add_overlay(rects)

