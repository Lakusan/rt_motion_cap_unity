from dataclasses import dataclass
from typing import List


@dataclass
class Settings:
    debug_mode: bool
    current_cam_index: int = 0
    available_cams_index: List[int] = None

    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Settings()
        return cls._instance
