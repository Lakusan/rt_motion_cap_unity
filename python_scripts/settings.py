# dataclass support
from dataclasses import dataclass

# list type
from typing import List

# app configuration file
import config_params


@dataclass
class Settings:
    """_summary_
        Dataclass as singleton to have one source of truth for
        app settings and config.
        Reads params of config-file: config_params.py
    Returns:
        _type_: _description_
    """

    debug_mode: bool = config_params.DEBUG
    current_cam_index: int = config_params.WEBCAM_INDEX
    available_cams_index: List[int] = None
    custom_config: bool = config_params.USE_CUSTOM_CAM_SETTINGS
    cam_config_fps: int = config_params.FPS
    cam_config_width: int = config_params.WIDTH
    cam_config_heigt: int = config_params.HEIGHT
    model_config_complexity: int = config_params.MODEL_COMPLEXITY

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
        return self.cam_fps

    def set_cams(self, cameras) -> None:
        """_summary_
            internal method to set found cams in dataclass
        Args:
            cameras (List[int]): List of cam indexes
        """
        self.available_cams_index = cameras.copy()
