import os
import cv2
import imutils
import dlib
import serial, time

arduino = serial.Serial('/dev/ttyACM0', 9600)

#abrir webcam
cap = cv2.VideoCapture(0)

#cargar los archivos svm entrenados
detector1 = dlib.fhog_object_detector("dataset_abierto.svm")
detector2 = dlib.fhog_object_detector("dataset_cerrado.svm")
detector3 = dlib.fhog_object_detector("dataset_derecho.svm")
detector4 = dlib.fhog_object_detector("dataset_izquierdo.svm")

detectors = [detector1, detector2, detector3, detector4]

#se muestran en pantalla las caracteristicas de HOG para cada detector
win_det = dlib.image_window()
win_det.set_image(detectors[0])

win_det2 = dlib.image_window()
win_det2.set_image(detectors[1])

win_det3 = dlib.image_window()
win_det3.set_image(detectors[2])

win_det4 = dlib.image_window()
win_det4.set_image(detectors[3])

win = dlib.image_window()
action = "nada"
font_color = (0,0,0)

#incio de ciclo para examinar cada frame de la webcam 
while True:
	action = "nada"
	ret, image = cap.read()
	image = imutils.resize(image, width = 400)


	#deteccion multiple de la imagen actual
	[boxes, confidences, detector_idxs] = dlib.fhog_object_detector.run_multiple(detectors, image, upsample_num_times= 0, adjust_threshold = 0.5)

	#enviar mensajes en pantalla de acuerdo al objeto encontrado
	for i in range(len(boxes)):
		if (detector_idxs[0] == 0):
			action = "abierto"
			arduino.write(('Q').encode('utf-8'))
			print(confidences)
		elif (detector_idxs[0] == 1):
			action = "cerrado"
			arduino.write(('B').encode('utf-8'))
		elif (detector_idxs[0] == 2):
			action = "derecha"
			arduino.write(('H').encode('utf-8'))
		elif (detector_idxs[0] == 3):
			action = "izquierda" 
			arduino.write(('H').encode('utf-8'))
	print (action)

	win.clear_overlay()
	cv2.putText(image, action, (10,40), cv2.FONT_HERSHEY_SIMPLEX,1,font_color, 2)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	win.set_image(image)
	win.add_overlay(boxes)
