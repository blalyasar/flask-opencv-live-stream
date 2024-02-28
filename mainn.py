
from flask import Flask, render_template, Response
from flask_caching import Cache
from camera import VideoCamera

app = Flask(__name__)

config={'CACHE_TYPE': 'SimpleCache'} 
app.config.from_mapping(config)


cache = Cache(app) 


# https://stackoverflow.com/questions/62756045/facial-recognition-trough-flask-with-dlib-gives-nameerror-name-face-utils-is
# http://localhost:5000/

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@cache.cached(timeout=50)
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)