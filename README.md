# BiometricAccessControl
A sample Python application for biometric access control. Here, the Actian Zen powers the solution for storing data locally (access schedule) and remotely (employee's actions log). FaceNet and TensorFlow are employed for facial recognition.

# Description
The logical pipeline and structure of the Python application BiometricAccessControl are sketched in the Figure below. The app first performs face recognition (recognizer.py). 

![App structure](/screenshots/Diagram.bmp)

Here, I am using face images from local files (but if you want to capture them from a camera, you can use opencv-python as shown in [this repository](https://github.com/dawidborycki/TalkingIoT) (refer to camera.py). 

Then, the facial recognition module returns the employee id and passes it to the access schedule module (accessSchedule.py). The latter determines whether the recognized employee or person can access the resource. The access schedule is stored in the local Actian Zen database. If the app determines that the person is scheduled to work, the app will start logging employee's actions (activityTracking.py). These actions are stored in the local collection, and transferred to the remote Actian database after the person signs out. 
