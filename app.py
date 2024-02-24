from flask import Flask, send_file, render_template
from io import BytesIO
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)
connection_string = "DefaultEndpointsProtocol=https;AccountName=storageblueroom;AccountKey=3JykcOcy31dKS4LbyZl2wkgfy80SDAgR1CzEmWDV9/htI7q88XH9tBqUiD9FQnnRo4OGdy7RkO9W+AStMFjHqA==;EndpointSuffix=core.windows.net"
container_name = "videos"
blob_name = "John Danaher/Arm Bar System/Videos/Volume 1.mp4"


@app.route('/')
def index():
    return render_template('index.html')

 
@app.route('/video')
def play_video():
    #video_path = '/Video_Project/video/Volume_1.mp4'
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    stream = blob_client.download_blob().readall()
    stream_io = BytesIO(stream)
    return send_file(stream_io, mimetype='video/mp4') 

if __name__ == '__main__':
    app.run(debug=True)
