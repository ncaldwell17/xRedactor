from flask import render_template, request
from werkzeug.utils import secure_filename
from pdf_extractor import convert_pdf_to_txt, save_to_file
from redact import clause_redactor
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

            with open("exampleText.txt", 'r+') as file:
                doc_as_list = file.readlines()
                file.close()

            doc_as_string = str()
            for line in doc_as_list:
                redacted_clause = clause_redactor.redact(line)
                doc_as_string += " " + redacted_clause

            # return render_template('ui.html', redactions=redactions)
            return doc_as_string

        else:
            return 'This was not a PDF file.'

