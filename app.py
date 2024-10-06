import os

from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

import util

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
util.load_artifacts()


def allowed_file(filename):
    path = '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    print("path", path)
    return path


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        # print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        flash(file_path)
        print(file_path)
        # print(classify(file_path))
        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


@app.route('/classify/<img_path>')
def classify(img_path):
    predicted_value, details, video1, video2 = util.classify_waste(app.config['UPLOAD_FOLDER'] + img_path)
    # Markup the details as safe HTML
    from markupsafe import Markup
    safe_details = Markup(details)
    return render_template('classify.html', predicted_value=predicted_value, details=safe_details, video1=video1,
                           video2=video2)


if __name__ == '__main__':
    app.run(debug=True)
