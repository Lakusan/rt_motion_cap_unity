from sys import exit
from settings import Settings
from cam_manager import CameraManager
from cam_capturerer import CaptureThread
import time
import cv2


if __name__ == "__main__":
    print("Load Settings")
    settings = Settings()
    print("---> Settings Loaded")

    print("Init Camera Manager")
    cam_manager = CameraManager()
    print("---> Camera Manager initialized")

    print("find cams")
    cam_manager.find_available_cameras()
    if settings.available_cams_index != None:
        print(f"len cams: {len(settings.available_cams_index)}")
        print(settings.available_cams_index)
    else:
        print("cams = NONE")
        print(f"len cams: {len(settings.available_cams_index)}")
    print("Init Capturing")
    print("---> Capturing init")
    capture = CaptureThread()
    capture.start()
