# dataclass support
from dataclasses import dataclass

# list type
from typing import List

# app configuration file
import config_params

import time


@dataclass
class Settings:
    """_summary_
    Dataclass as singleton to have one source of truth for
    app settings and config.
    Reads params of config-file: config_params.py
    """

    # config params mapping
    debug_mode: bool = config_params.DEBUG
    current_cam_index: int = config_params.WEBCAM_INDEX
    available_cams_index: List[int] = None
    custom_config: bool = config_params.USE_CUSTOM_CAM_SETTINGS
    cam_config_fps: int = config_params.FPS
    cam_config_width: int = config_params.WIDTH
    cam_config_height: int = config_params.HEIGHT
    model_config_complexity: int = config_params.MODEL_COMPLEXITY
    capuring_is_running: bool = False
    pose_estimation_is_running: bool = False
    kill_all_threads: bool = config_params.KILL_THREADS
    min_detection_confidence = config_params.MIN_DETECTION_CONFIDENCE
    min_tracking_confidence = config_params.MIN_TRACKING_CONFIDENCE
    static_image_mode = config_params.STATIC_IMAGE_MODE
    enable_segmentation = config_params.ENABLE_SEGMENTATION
    frame = None
    ret: bool = None

    instance = None

    def __new__(cls):
        """_summary_
            checks if Settings class is instanciated
            If not create Instance
        Returns:
            class_object: instance of dataclass
        """
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def get_debug_mode(self) -> bool:
        """_summary_
            getter for debug_mode on/off
        Returns:
            bool: Debug mode state
        """
        return self.debug_mode

    def get_current_cam_index(self) -> int:
        """_summary_
                getter current cam index for opencv
        Returns:
            int: current cam indexy
        """
        return self.current_cam_index

    def set_current_cam_index(self, index) -> None:
        """_summary_
            set current cam index for opencv
            If dont want to use index = 0 (systems default cam)
            then set USE_CUSTOM_SETTINGS = True and WEBCAM_INDEX
            to desired index val as int
        Args:
            index (int): cam index
        """
        self.current_cam_index = index

    def get_available_cams_index(self) -> List[int]:
        """_summary_
            get list of all attached usb cams
            available via opencv
        Returns:
            List[int]: list of found cam indexes
        """
        return self.available_cams_index

    def is_custom_config(self) -> bool:
        """_summary_
            checks if custom settings are true
        Returns:
            bool: custom config on/off
        """
        return self.custom_config

    def get_cam_config_fps(self) -> int:
        """_summary_
            gets configured fps from config
        Returns:
            int: FPS configured in config_params
        """
        return self.cam_config_fps

    def get_cam_config_width(self) -> int:
        """_summary_
            gets configured width from config
        Returns:
            int: FPS configured in config_params
        """
        return self.cam_config_width

    def get_cam_config_height(self) -> int:
        """_summary_
            gets configured height from config
        Returns:
            int: FPS configured in config_params
        """
        return self.cam_config_height

    def set_cams(self, cameras) -> None:
        """_summary_
            internal method to set found cams in dataclass
        Args:
            cameras (List[int]): List of cam indexes
        """
        self.available_cams_index = cameras.copy()

    def toggle_thread_capturing_state(self) -> None:
        if self.capuring_is_running:
            self.capuring_is_running = False
            self.kill_all_threads = True
        else:
            self.capuring_is_running = True

    def toggle_thread_pose_estimation_state(self) -> None:
        if self.pose_estimation_is_running:
            self.pose_estimation_is_running = False
            self.kill_all_threads = True
        else:
            self.pose_estimation_is_running = True

    def get_model_config_complexity(self):
        return self.model_config_complexity

    def kill_all(self) -> None:
        self.kill_all_threads = True
        time.sleep(2)
        exit()

    def get_detection_confidence(self) -> float:
        return self.min_detection_confidence

    def get_tracking_confidence(self) -> float:
        return self.min_tracking_confidence

    def get_image_mode(self) -> bool:
        return self.static_image_mode

    def get_segmentation(self) -> bool:
        return self.enable_segmentation
