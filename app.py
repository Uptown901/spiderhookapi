from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

 
@app.route('/video')
def play_video():
    video_path = '/Video_Project/video/Volume_1.mp4'
    return send_file(video_path, mimetype='video/mp4') 

if __name__ == '__main__':
    app.run(debug=True)
