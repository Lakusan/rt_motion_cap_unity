# media pipe
import mediapipe as mp

# from media pipe import python bindings
from mediapipe.tasks import python

# import vision module from media pipe
from mediapipe.tasks.python import vision

# Opencv
import cv2

# Threading Lib from Python
import threading
import time

# own config params
import config_params

import struct

from settings import Settings


class Pose_Estimation(threading.Thread):
    data: str = ""
    pipe = None
    timeSinceCheckedConnection: int = 0
    timeSincePostStatistics: int = 0
    settings = Settings()
    frame: cv2.Mat = None
    ret: bool = False

    def run(self):
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose

        self.settings.pose_estimation_is_running = True

        while not self.settings.kill_all_threads and not self.ret:
            print("pose etimation: waiting for frames")
            time.sleep(0.5)
            print("pose estimation: start processing frames")

        with mp_pose.Pose(
            min_detection_confidence=self.settings.get_detection_confidence(),
            min_tracking_confidence=self.settings.get_tracking_confidence(),
            model_complexity=self.settings.get_model_config_complexity(),
            static_image_mode=self.settings.get_image_mode(),
            enable_segmentation=self.settings.get_segmentation(),
        ) as pose:
            
            while not self.settings.kill_all_threads:
                if self.ret:
                    t_i = time.time()

                    # image transformation
                    frame = cv2.flip(self.frame, 1)

                    # detect
                    results = pose.process(frame)

                    t_f = time.time()

                    if self.settings.get_debug_mode():
                        if time.time() - self.timeSincePostStatistics >= 1:
                            print("approx max FPS pose estimation: %f" % (1 / (t_f - t_i)))
                            self.timeSincePostStatistics = time.time()

                        if results.pose_landmarks:
                            mp_drawing.draw_landmarks(
                                frame,
                                results.pose_landmarks,
                                mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(
                                    color=(255, 100, 0), thickness=2, circle_radius=4
                                ),
                                mp_drawing.DrawingSpec(
                                    color=(255, 255, 255), thickness=2, circle_radius=2
                                ),
                            )
                        cv2.imshow("Results pose_estimation", frame)
                        cv2.waitKey(1)

                    if (self.pipe == None and time.time() - self.timeSinceCheckedConnection >= 1):
                        try:
                            self.pipe = open(r'\\.\pipe\UnityMediaPipeBody', 'r+b', 0)
                        except FileNotFoundError:
                            print("pipe: Wait for Unity")
                            self.pipe = None
                        
                    self.timeSinceCheckedConnection = time.time()

                    if self.pipe != None:
                        print("send pose")
                        self.data = ""
                        i = 0
                        if results.pose_world_landmarks:
                            hand_world_landmarks = results.pose_world_landmarks
                            for i in range(0, 33):
                                self.data += "{}|{}|{}|{}\n".format(
                                    i,
                                    hand_world_landmarks.landmark[i].x,
                                    hand_world_landmarks.landmark[i].y,
                                    hand_world_landmarks.landmark[i].z,
                                )
                        print(s)
                        s = self.data.encode("ascii")
                        try:
                            self.pipe.write(struct.pack("I", len(s)) + s)
                            self.pipe.seek(0)
                        except Exception as e:
                            print("Failed to write to pipe. Unity not reachable")
                            self.pipe = None

        self.pipe.close()
        self.capture.cap.release()
        cv2.destroyAllWindows()
