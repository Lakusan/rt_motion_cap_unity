# Toogle DEBUG Mode
DEBUG = True

# Webcam Config
# index of usb webcam device -> 0 = internal default cam; 1 -> additional via usb connected cam
WEBCAM_INDEX = 0
# Activate custom cam settings
USE_CUSTOM_CAM_SETTINGS = False
# desired fps -> most cams support 30 FPS <- Default
# if set to 0 device defaults are used
FPS = 0
# force image resolution
WIDTH = 0
HEIGHT = 0

# media pipe config params
# [0, 2] Higher numbers are more precise, but also cost more performance. The demo video used 1.
MODEL_COMPLEXITY = 1

# Interals
# used to kill all threads before app exits
# gets used automaically -> dont change
KILL_THREADS = False
