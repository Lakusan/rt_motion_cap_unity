#Real-time motion capturing with webcam for unity engine

# Description
Python scripts are used to process live stream from webcam.
Mediapipe is used to process the images and extract a humans pose.
NamedPipeServerStream is used on the server in unity to get data from python scripts.
MediaPipes Pose data is then translated to unity coords.
Representation of the joints is then shown with primitives in unity.

## Versions
Unity Engine 2022.3.4f1 LTS
numpy-1.25.1 
opencv-python-4.8.0.74
mediapipe

## Setup
- clone project
- in python_scripts install dependencies 

## Start
1. Python
    - set config_params
    - start main.py
2. Unity
    - start unity project and open sample scene
    - hit play
