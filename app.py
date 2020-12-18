import os
from flask import Flask, render_template

from text_detection_0 import ocr_core

# define a folder to store and later serve the images
UPLOAD_FOLDER = '/static/uploads'

# Only files of a specific type. Note the type is `set`
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)


def allowed_file(filename):
    """Check if we have an acceptable file extension."""
    return '.' in file and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home_page():
    """Route and function to handle the home page."""
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    """Route and function to handle the upload page."""
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected.')
        file = request.files['file']

        # if no file selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected.')

        # If everything's clear, shoot.
        if file and allowed_file(file.filename):
            extracted_text = ocr_core(file)
            return render_template(
                'upload.html',
                msg='Successfully processed.',
                extracted_text=extracted_text,
                img_src=UPLOAD_FOLDER + file.filename
            )

    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == '__main__':
    app.run()
