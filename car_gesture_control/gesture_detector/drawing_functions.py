import cv2
import numpy as np


class DrawingFunctions:
    def __init__(self):
        self.img_forward = cv2.imread('car_gesture_control/gesture_detector/resources/images/forward.png')
        #self.img_reverse = cv2.imread('gesture_detector/resources/images/reverse.png')
        self.img_left = cv2.imread('car_gesture_control/gesture_detector/resources/images/left.png')
        self.img_right = cv2.imread('car_gesture_control/gesture_detector/resources/images/right.png')
        self.img_stop = cv2.imread('car_gesture_control/gesture_detector/resources/images/stop.png')
        #car_gesture_control/gesture_detector/resources/images

    def draw_image(self, original_frame: np.ndarray, action_image: np.ndarray):
        print("action_image:", action_image)
        if action_image is None:
            raise FileNotFoundError("La imagen de acción no se cargó correctamente. Verifica la ruta.")

        al, an, c = action_image.shape  
        #alto y ancho de la imagen para poner la imagen de ref
        #original_frame[600:600 + al, 50:50 + an] = action_image
        frame_height, frame_width, _ = original_frame.shape  # Dimensiones del frame original

        # Ajustar alto y ancho de la imagen de acción para que coincida con el espacio en original_frame
        target_height = 120  # El alto esperado en original_frame
        target_width = an  # Mantener el ancho original

        if al != target_height:
            action_image = cv2.resize(action_image, (target_width, target_height))  # Redimensionar

        # Insertar la imagen redimensionada en el frame
        original_frame[600:600 + target_height, 50:50 + target_width] = action_image
        
        return original_frame

    def draw_actions(self, action: str, original_frame: np.ndarray) -> np.ndarray:

        actions_dict = {
            'F': self.img_forward,
            'S': self.img_stop,
            'L': self.img_left,
            'R': self.img_right,
            #'R': self.img_reverse,
        }
        if action in actions_dict:
            movement_image = actions_dict[action]
            original_frame = self.draw_image(original_frame, movement_image)
        return original_frame