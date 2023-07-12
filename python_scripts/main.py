from sys import exit
from settings import Settings
from cam_manager import CameraManager


if __name__ == "__main__":
    print("Settings")
    settings = Settings()
    print("Camera Manager")
    cam_manager = CameraManager()
    print("find cams")
    cam_manager.find_available_cameras()
    if settings.available_cams_index != None:
        print("WORKS")
        print(f"len cams: {len(settings.available_cams_index)}")
        print(settings.available_cams_index)
    else:
        print("cams = NONE")
        print(f"len cams: {len(settings.available_cams_index)}")
    exit()
