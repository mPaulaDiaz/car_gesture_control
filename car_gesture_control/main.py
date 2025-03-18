import cv2
from gesture_detector.main import GestureDetector
from control_interface.serial_communication import SerialCommunication

#The code works with the right hand


class CarGestureControl:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1280) #camera dimentions 1280x720
        self.cap.set(4, 720)
        self.hand_gesture = GestureDetector()
        self.communication = SerialCommunication()

    def frame_processing(self):
        while True:
            t = cv2.waitKey(5)
            ret, frame = self.cap.read()
            command, draw_frame = self.hand_gesture.gesture_interpretation(frame)
            self.communication.sending_data(command)  #dibujamos los keypoints de la mano y en base a los puntos deetectados se devuelve un comando

            cv2.imshow('Car gesture control', draw_frame)
            if t == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()

detector = CarGestureControl()
detector.frame_processing()

