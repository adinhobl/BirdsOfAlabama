from flask import Flask, render_template, url_for, request, redirect, flash, send_from_directory
from werkzeug.utils import secure_filename
from fastai import Path, torch, defaults
from fastai.vision import (ImageDataBunch, create_cnn, open_image, models)
import os


app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, 'static')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'JPG'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_page():
    
    if request.method == 'POST':
        return upload_file()
    return render_template('upload.html')

@app.route('/<filename>', methods=['POST','GET'])
def predict(filename):
    # make prediction
    # result = "cat"
    result = classify(filename, learn)
    
    # display page & handle upload
    if request.method == 'POST':
        return upload_file()
    return render_template('result.html', user_image=filename, result=result)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file():
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('predict', filename=filename))

def classify(filename, learn):
    
    file = Path(UPLOAD_FOLDER)/filename

    image = open_image(file)
    pred = learn.predict(image)
    
    return pred[0]

def create_network():
    
    empty_data = ImageDataBunch.load_empty(Path(UPLOAD_FOLDER), 'export.pkl')
    learn = create_cnn(empty_data, models.resnet18).load('stage-2')
    
    return learn


if __name__ == '__main__':
    defaults.device = torch.device('cpu')
    learn = create_network()
    app.run(debug=True)