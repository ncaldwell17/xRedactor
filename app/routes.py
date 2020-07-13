from flask import render_template, request
from werkzeug.utils import secure_filename
from pdf_extractor import convert_pdf_to_txt, save_to_file
from redact import ClauseRedactor, redactor_dict
from app import app
from nltk import sent_tokenize, word_tokenize
import os


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/redact')
def redact():
    return render_template('redact.html')

@app.route('/vectors')
def vectors():
    return render_template('vectors.html')


@app.route('/uploader', methods=['POST'])
def process_file():

    if request.method == 'POST':

        f = request.files['file']
        # v = request.form['redactors']
        f.save(secure_filename(f.filename))

        # for loop to make a list of values from a list of dict keys given the keys + dictionary mapping
        """
        if f.filename.endswith('.pdf'):
            text = convert_pdf_to_txt(secure_filename(f.filename))
            save_to_file(text)
            os.remove(secure_filename(f.filename))

            with open("exampleText.txt", 'r+') as file:
                doc_as_list = file.readlines()
                file.close()

            doc_as_string = str()
            for line in doc_as_list:
                clause_redactor = ClauseRedactor(redactor_dict.values())
                redacted_clause = clause_redactor.redact(line)
                doc_as_string += " " + redacted_clause

            with open("saveText.txt", 'w+') as savefile:
                savefile.write(doc_as_string)
                savefile.close()

            return render_template('redacted.html', content=doc_as_string)

        else:
            return 'This was not a PDF file.'
        """


