# Toogle DEBUG Mode
DEBUG = True

# Webcam Config
# index of usb webcam device -> 0 = internal default cam; 1 -> additional via usb connected cam
WEBCAM_INDEX = 0
# Activate custom cam settings
USE_CUSTOM_CAM_SETTINGS = True
# desired fps -> most cams support 30 FPS
# if set to 0 device defaults are used
FPS = 60
# force image resolution
WIDTH = 640
HEIGHT = 480

# media pipe config params
# [0, 2] Model selection - the higher the better the results but with lesser fps

MODEL_COMPLEXITY = 0
MIN_DETECTION_CONFIDENCE = 0.80
MIN_TRACKING_CONFIDENCE = 0.5
STATIC_IMAGE_MODE = False
ENABLE_SEGMENTATION = True

# Interals
# used to kill all threads before app exits
# gets used automaically -> change to stopf running threads
KILL_THREADS = False
