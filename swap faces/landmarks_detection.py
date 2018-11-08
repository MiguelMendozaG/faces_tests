import cv2
import dlib
import numpy
import time
import sys

PREDICTOR_PATH = "/home/miguel/Documents/sr/drowsiness detection/shape_predictor_68_face_landmarks.dat"
SCALE_FACTOR = 0.9
FEATHER_AMOUNT = 11

FACE_POINTS = list(range(17, 68))
MOUTH_POINTS = list(range(48, 61))
RIGHT_BROW_POINTS = list(range(17, 22))
LEFT_BROW_POINTS = list(range(22, 27))
RIGHT_EYE_POINTS = list(range(36, 42))
LEFT_EYE_POINTS = list(range(42, 48))
NOSE_POINTS = list(range(27, 35))
JAW_POINTS = list(range(0, 17))

# Points used to line up the images.
ALIGN_POINTS = (LEFT_BROW_POINTS + RIGHT_EYE_POINTS + LEFT_EYE_POINTS +
                               RIGHT_BROW_POINTS + NOSE_POINTS + MOUTH_POINTS)

# Points from the second image to overlay on the first. The convex hull of each
# element will be overlaid.
OVERLAY_POINTS = [
    LEFT_EYE_POINTS + RIGHT_EYE_POINTS + LEFT_BROW_POINTS + RIGHT_BROW_POINTS,
    NOSE_POINTS + MOUTH_POINTS,
]

# Amount of blur to use during colour correction, as a fraction of the
# pupillary distance.
COLOUR_CORRECT_BLUR_FRAC = 0.6

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(PREDICTOR_PATH)

def get_landmarks(im):
    rects = detector(im, 1)
    #mat = numpy.matrix([[p.x, p.y] for p in predictor(im, rects[0]).parts()])

    return len(rects)

def webcam_image(fname):
    im = cv2.resize(fname, (int(fname.shape[1] * SCALE_FACTOR), int(fname.shape[0] * SCALE_FACTOR)))
    s = get_landmarks(im)

    return im, s


cap = cv2.VideoCapture(0)

while True:

	ret, im2 = cap.read()
	im_out, landmarks = webcam_image(im2)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		out.release()
		break
	print(landmarks)
	cv2.imshow('output.jpg', im_out)
