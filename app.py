from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/stream', methods=['POST'])
def stream():

    stream_url = request.json['stream_url']


    ffmpeg_cmd = f'ffmpeg -i {stream_url} -c:v libx264 -c:a aac -f hls -hls_list_size 3 -hls_segment_filename "segment_%03d.ts" output.m3u8'
    subprocess.run(ffmpeg_cmd, shell=True)


    return jsonify({'message': 'Stream converted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)