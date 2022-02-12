import cv2
import numpy as np
from pathlib import Path


path = Path(__file__).resolve().parent
face_detection = cv2.CascadeClassifier(str(Path(path, 'face_detection.xml')))

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    faces = face_detection.detectMultiScale(frame, 1.3, 5)
    if len(faces) > 0:
        x, y, w, h = faces[0]
        # frame = frame[y:y+h, x:x+w]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    cv2.imshow('dev/video0', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()