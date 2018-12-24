from flask import Flask, render_template, url_for, request, redirect, flash, send_from_directory
from fastai import *
from fastai.vision import *
import os
from werkzeug.utils import secure_filename



app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, 'static')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'JPG'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('predict', filename=filename))
    return render_template('upload.html')

@app.route('/<filename>', methods=['POST','GET'])
def predict(filename):
    #make prediction
    result = "cat"

    # render template and display image
    # full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    #upload box

    
    return render_template('result.html', user_image=filename, result=result)
    # return redirect(url_for('predict', filename=filename))
    # return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



if __name__ == '__main__':
    app.run(debug=True)