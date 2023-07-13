import cv2
from typing import List
from settings import Settings
import cv2


class CameraManager:
    _instance = None

    settings = Settings()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CameraManager, cls).__new__(cls)
        return cls._instance

    def find_available_cameras(self) -> bool:
        self.cameras = []
        index = 0
        while True:
            cap = cv2.VideoCapture(index)
            if not cap.read()[0]:
                break
            self.cameras.append(index)
            cap.release()
            index += 1
        if len(self.cameras) != 0:
            self.settings.set_cams(self.cameras)
            return True
        else:
            raise Exception("No cameras found")
