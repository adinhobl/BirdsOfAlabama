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

@app.route('/', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        return upload_file()
    return render_template('upload.html')

@app.route('/<filename>', methods=['POST','GET'])
def predict(filename):
    # make prediction
    classes = ['Summer_Tanager', 'Barn_Swallow', 'Eastern_Bluebird', 'Brown_Pelican', 'American_Robin',
        'American_Goldfinch', 'Northern_Cardinal', 'Cedar_Waxwing', 'Bald_Eagle', 'Blue_Jay', 'Great_Blue_Heron',
        'Red-winged_Blackbird', 'Killdeer', 'Barred_Owl', 'Indigo_Bunting', 'White-breasted_Nuthatch',
        'Brown_Headed_Nuthatch', 'American_Crow', 'Hooded_Warbler', 'Northern_Mockingbird', 'Carolina_Chickadee']
        # at somepoint, make this pull from a text file
    
    
    result = "cat"
    
    # display page & handle upload
    if request.method == 'POST':
        return upload_file()
    return render_template('result.html', user_image=filename, result=result)




if __name__ == '__main__':
    app.run(debug=True)