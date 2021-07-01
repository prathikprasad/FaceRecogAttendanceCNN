# Contactless Attendance Systen using Deep Learning

An end-to-end face identification and attendance approach using Convolutional Neural Networks (CNN), which processes the CCTV footage or a video of the class and mark the attendance of the entire class simultaneously.

## Make sure to have following directory structure
1. 'Main' directory:
<img src="https://github.com/prathikprasad/FaceRecogAttendanceCNN/blob/main/images/Screenshot%20(764).png" width="480">
2. 'output' directory:
<img src="https://github.com/prathikprasad/FaceRecogAttendanceCNN/blob/main/images/Screenshot%20(766).png" width="480">
3. '20180402-114759' directory:
<img src="https://github.com/prathikprasad/FaceRecogAttendanceCNN/blob/main/images/Screenshot%20(765).png" width="480">
4. Each person's directory will look somewhat like:
<img src="https://github.com/prathikprasad/FaceRecogAttendanceCNN/blob/main/images/Screenshot%20(767).png" width="480">
5. Output attendance folder:
<img src="https://github.com/prathikprasad/FaceRecogAttendanceCNN/blob/main/images/Screenshot%20(769).png" width="480">

## Libraries
1. Tensorflow 1.14
2. Numpy
3. OpenCV
4. MTCNN
5. xlsxwriter, xlrd
6. scipy
7. pickle

## How to use
### Installation
1. Install the required libraries. (Conda environment preferred).
2. Have all files and directories.
3. To verify is everything installed properly run 'user_interface.py'.
### Create Dataset
1. Run 'user_interface.py'
2. Click on the 'Create' button.
3. Type in name of person or ID number
4. Select 'webcam' if you wish to create live dataset. (you can leave all other fileds empty)
5. Click on the 'Create Dataset' button to start streaming webcam feed.
6. Hold 's' to save the face images. Take as many images as you can take. (approx. 80-100 preferred)
7. Press 'q' to exit.
8. Similarly create other datasets.
### Training
1. Run 'user_interface.py'
2. Click on the 'Train Model' button.
3. Training may take several minutes (depending upon your system configuration).
4. Once training is completed, a 'classifier.pkl' file will be generated.
### Run
1. Run 'user_interface.py'
2. Click on the 'Run' button.
3. Select 'Webcam' fom the list and leave all fields blank.
4. Click on 'Mark Attendance' button.
5. Attendance sheet will be generated automatically with current date/time.
