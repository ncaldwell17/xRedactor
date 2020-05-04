from flask import render_template, request
from werkzeug.utils import secure_filename
from pdf_extractor import convert_pdf_to_txt, save_to_file
from app import app
import os

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def process_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))

        if f.filename.endswith('.pdf'):
            text = convert_pdf_to_txt(secure_filename(f.filename))
            save_to_file(text)
            os.remove(secure_filename(f.filename))
            return text
        else:
            return 'This was not a PDF file.'

