# camera.py 
# 
import cv2
import dlib

import imutils
from imutils import face_utils

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        detector = dlib.get_frontal_face_detector()
        # https://github.com/MortezaNedaei/Facial-Landmarks-Detection/blob/master/shape_predictor_68_face_landmarks.dat
        predictor = dlib.shape_predictor(r'shape_predictor_68_face_landmarks.dat')
        success, image = self.video.read()
        image = imutils.resize(image, width=150)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 1)
        for (i, rect) in enumerate(rects):
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)
            (x, y, w, h) = face_utils.rect_to_bb(rect)
            #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, "Mate".format(i + 1), (x - 5, y - 5),
                cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)
            for (x, y) in shape:
                cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
        # for (x,y,w,h) in face_rects:
        #     cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        #     break
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()