from re import DEBUG, sub
from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename, send_from_directory
import os
import subprocess
from subprocess import Popen, PIPE, run
import json

app = Flask(__name__)


uploads_dir = os.path.join(app.instance_path, 'uploads')

os.makedirs(uploads_dir, exist_ok=True)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/detect", methods=['POST'])
def detect():
    if not request.method == "POST":
        return
    video = request.files['video']
    video.save(os.path.join(uploads_dir, secure_filename(video.filename)))
    #print(video)
    # subprocess.call(['cd','yolo'])
    # subprocess.call(['cd','Scripts'])
    # subprocess.call(['activate.bat'])
    # output = subprocess.run(['cd', 'yolo'], shell=True)
    # print(output)
    # print(subprocess.call("dir", shell=True))
    # print(subprocess.call("cd yolo", shell=True))
    # subprocess.run('ls')
    #subprocess.run(['yolo/Scripts/python', 'detect.py', '--source', os.path.join(uploads_dir, secure_filename(video.filename))])

    # p = Popen(['yolo/Scripts/python', 'detect.py', '--source', os.path.join(uploads_dir, secure_filename(video.filename))], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    # output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    # rc = p.returncode

    # ===================================================
    command =['env/Scripts/python', 'detect.py', '--source', os.path.join(uploads_dir, secure_filename(video.filename))]
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    # print(result.returncode, result.stdout, result.stderr)
    print( result.stdout)

    # print(output)

    # return os.path.join(uploads_dir, secure_filename(video.filename))
    #obj = secure_filename(video.filename)
    data = {
        'name': secure_filename(video.filename),
        'result': result.stdout
        
        
    }
    dict_1 = json.dumps(data)  # converting dictionary to JSON
    print(dict_1)  # {'Name' : 'Felix','Occupation' : 'Doctor'}
    return dict_1

@app.route("/opencam", methods=['GET'])
def opencam():
    print("here")
    subprocess.run(['env/Scripts/python', 'detect.py', '--source', '0'])
    return "done"



@app.route('/return-files', methods=['GET'])
def return_file():
    obj = request.args.get('obj')
    loc = os.path.join("runs/detect", obj)
    print(loc)
    try:
        return send_file(os.path.join("runs/detect", obj), attachment_filename=obj)
        # return send_from_directory(loc, obj)
    except Exception as e:
        return str(e)

# @app.route('/display/<filename>')
# def display_video(filename):
# 	#print('display_video filename: ' + filename)
# 	return redirect(url_for('static/video_1.mp4', code=200))