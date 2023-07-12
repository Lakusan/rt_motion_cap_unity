from dataclasses import dataclass
from typing import List
import config_params


@dataclass
class Settings:
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
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def get_debug_mode(self) -> bool:
        return self.debug_mode

    def get_current_cam_index(self) -> int:
        return self.current_cam_index

    def set_current_cam_index(self, index) -> None:
        self.current_cam_index = index

    def get_available_cams_index(self) -> List[int]:
        return self.available_cams_index

    def is_custom_config(self) -> bool:
        return self.custom_config

    def get_cam_config_fps(self) -> int:
        return self.cam_fps

    def set_cams(self, cameras) -> None:
        self.available_cams_index = cameras.copy()
