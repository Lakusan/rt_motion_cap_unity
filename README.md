  <!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Lakusan/invisnav">
    <img src="README_assets/invisnav_icon.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">
<span style="color: #84cc16;">Realtime Motion Capturing in Unity Engine</span>

  <p align="center">
    <br />
    </br>
    <a href="https://github.com/Lakusan/rt_motion_cap_unity/blob/main/aai_presentation.pdf"><strong>View Presentation »</strong></a>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project
<div>
    </br>
    <p>
   This application was developed during the Module Applied Artificial Intelligence as part of my Master Degree in Applied Computer Science at SRH University Heidelberg, in July 2023.
    </p>
    <p>
    Python scripts are used to process live video stream from webcam.
Mediapipe is used to process the images and extract a humans pose.
NamedPipeServerStream is used on the server in unity to get data from python scripts.
MediaPipes Pose data is then translated to unity coords.
Representation of the joints is then shown with primitives in unity.
</p>
</div>

<section style="display: grid; grid-template-columns: 1fr; gap: 20px; text-align: start;">
    <div style="color: white; padding: 10px; width: 100%; height: 100%; margin: 0;">
        <h3>Python: Pose Estimation</h3>
        <ul>
            <li style="padding: 5px; margin: 5px;">Manage I/O Camera Image Stream</li>
            <li style="padding: 5px; margin: 5px;">Estimate Pose</li>
        </ul>
    </div>
    <div style="color: white; padding: 10px; width: 95%; height: 96%; margin: 0;">
        <img src="python_classes.png" alt="Screenshot1" width="900" height="600"></img>
    </div>
        <div style="color: white; padding: 10px; width: 100%; height: 100%; margin: 0;">
        <h3>Unity </h3>
        <ul>
            <li style="padding: 5px; margin: 5px;">Joints and Pose rendering</li>
            <li style="padding: 5px; margin: 5px;">Landmark to Joint Mapping</li>
            <li style="padding: 5px; margin: 5px;">Networking with Python Interface</li>
        </ul>
    </div>
    <div style="color: white; padding: 10px; width: 100%; height: 100%; margin: 0;">
        <img src="csharp_classes.png" alt="Screenshot1" width="900" height="500"></img>
        <div style="color: white; padding: 10px; width: 100%; height: 100%; margin: 0;">
        <h3>App</h3>
        <ul>
            <li style="padding: 5px; margin: 5px;">Left side real-time Pose estimation on webcam images</li>
            <li style="padding: 5px; margin: 5px;">Right Side: Landmark to Pose Rendering</li>
            <li style="padding: 5px; margin: 5px;">Anchor Placement as Navigation Target (green cube)</li>
        </ul>
    </div>
    </div>
        <div style="color: white; padding: 10px; width: 100%; height: 100%; margin: 0;">
        <img src="app_running.png" alt="Screenshot1" width="900" height="500"></img>
    </div>
</section>


<!-- Dependencies -->
## Dependencies

* Unity Engine 2022.3.4f1 LTS
* python 3.11.4
* numpy-1.25.1 
* opencv-python-4.8.0.74
* mediapipe 0.10.2


<!-- Setup -->
## Setup
- clone project
- in python_scripts install dependencies [$ pip install -r requirements.txt]

<!-- USAGE EXAMPLES -->
## Usage
1. Python
    - set config_params
    - start main.py
2. Unity
    - start unity project and open sample scene
    - hit play
</br>

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE.txt` for more information.
</br>

<!-- CONTACT -->
## Contact

* Project Link: [https://github.com/Lakusan/invisnav](https://github.com/Lakusan/invisnav)
* [![LinkedIn][linkedin-shield]][linkedin-url]

<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/lakusan
