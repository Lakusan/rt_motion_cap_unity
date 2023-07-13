import threading
import cv2
import time
from settings import Settings
from pose_estimation import Pose_Estimation


class CaptureThread(threading.Thread):
    settings = Settings()

    cap: cv2.VideoCapture = None
    ret: bool = False
    counter: int = 0
    timer: float = 0.0
    cam_index: int = 0
    frame: cv2.Mat = None

    pose_estimation = Pose_Estimation()

    def run(self) -> None:
        self.settings.capuring_is_running = True
        self.pose_estimation.start()
        while (
            not self.settings.kill_all_threads
            and not self.settings.pose_estimation_is_running
        ):
            print("Waiting for pose estimation thread")
            time.sleep(0.5)
            print("Processing Thread ready")

        self.cam_index = self.settings.get_current_cam_index()
        print(f"cam_index: {self.cam_index}")
        self.cap = cv2.VideoCapture(self.cam_index)

        if self.settings.custom_config:
            self.cap.set(cv2.CAP_PROP_FPS, self.settings.get_cam_config_fps())
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.settings.get_cam_config_width())
            self.cap.set(
                cv2.CAP_PROP_FRAME_HEIGHT, self.settings.get_cam_config_height()
            )
            print(f"{self}: cam custom config loaded")

        while not self.settings.kill_all_threads and not self.cap.isOpened():
            print("Initialize Capturing Thread")
            time.sleep(0.5)
        print("Starting capturing sequence")
        print("Opened Capture @ %s fps" % str(self.cap.get(cv2.CAP_PROP_FPS)))
        # thread is running
        self.settings.capuring_is_running = True
        while not self.settings.kill_all_threads and self.cap.isOpened():
            self.ret, self.frame = self.cap.read()
            if self.ret:
                self.pose_estimation.frame = self.frame.copy()
                self.pose_estimation.ret = self.ret
                if self.settings.debug_mode:
                    self.counter = self.counter + 1
                    if time.time() - self.timer >= 3:
                        print(
                            "Capturing FPS: ", self.counter / (time.time() - self.timer)
                        )
                    self.counter = 0
                    self.timer = time.time()
                    cv2.imshow("cap", self.frame)
                    cv2.waitKey(1)
