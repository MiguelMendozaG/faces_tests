import cv2
import numpy as np
import glob

face_folder = "/home/miguel/Documents/sr/face recognition/lbph/yo.png"
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("/home/miguel/opencv-3.3.0/data/haarcascades_cuda/haarcascade_frontalface_default.xml");

faces = cv2.imread(face_folder)
faces = cv2.cvtColor(faces, cv2.COLOR_RGB2GRAY)
faces = [faces]
ids = [1]

recognizer.train(faces, np.array(ids))
recognizer.save('trainer.yml')
