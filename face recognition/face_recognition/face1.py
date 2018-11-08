import face_recognition
import cv2
from imutils.object_detection import non_max_suppression
from imutils import paths
import imutils
import time

# This is a super simple (but slow) example of running face recognition on live video from your webcam.
# There's a second example that's a little more complicated but runs faster.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.


#out = cv2.VideoWriter('debate_output.mp4', cv2.VideoWriter_fourcc('D','I','V','X'), 30, (1280,718),True)
video_src = 'debate.mp4'
# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
yo_image = face_recognition.load_image_file("yo.png")
yo_face_encoding = face_recognition.face_encodings(yo_image)[0]

# Load a second sample picture and learn how to recognize it.
peje_image = face_recognition.load_image_file("peje.jpeg")
peje_face_encoding = face_recognition.face_encodings(peje_image)[0]

#load a third image
meade_image = face_recognition.load_image_file("meade.jpeg")
meade_face_encoding = face_recognition.face_encodings(meade_image)[0]

anaya_image = face_recognition.load_image_file("anaya.jpg")
anaya_face_encoding = face_recognition.face_encodings(anaya_image)[0]

bronco_image = face_recognition.load_image_file("bronco.jpg")
bronco_face_encoding = face_recognition.face_encodings(bronco_image)[0]

margarita_image = face_recognition.load_image_file("margarinflas.jpg")
margarita_face_encoding = face_recognition.face_encodings(margarita_image)[0]
# Create arrays of known face encodings and their names
known_face_encodings = [
    yo_face_encoding,
    peje_face_encoding,
	meade_face_encoding,
	anaya_face_encoding,
	bronco_face_encoding,
	margarita_face_encoding
]
known_face_names = [
    "Yo",
    "Peje",
	"Meade",
	"Anaya",
	"Bronco",
	"Margarita"
]

while True:
    start = time.time()
    print ("hello")
    # Grab a single frame of video
    ret, frame = video_capture.read()
    frame = imutils.resize(frame, width=720)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Desconocido"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    #out.write(frame) #guarda video
    print (time.time() - start)
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        out.release()
        break

# Release handle to the webcam
out.release()
video_capture.release()
cv2.destroyAllWindows()
