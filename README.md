# flask-opencv-live-stream
Shape predictor app on web based with caching mechanism but slow becasue dlib process and python slow....

CREATE VENV for  WINDOWS:

python3.exe -m venv flaskenv 

activate venv 

.\flaskenv\Scripts\activate.bat 
                     
pip install cmake    imutils  flask_caching opencv

Download : dlib lib for built windows.
1 - https://github.com/z-mahmud22/Dlib_Windows_Python3.x/blob/main/dlib-19.22.99-cp310-cp310-win_amd64.whl

python -m pip install dlib-19.22.99-cp310-cp310-win_amd64.whl   

Download shape file same path:

https://github.com/MortezaNedaei/Facial-Landmarks-Detection/blob/master/shape_predictor_68_face_landmarks.dat
 
RUN CODE: 

python  mainn.py. 

