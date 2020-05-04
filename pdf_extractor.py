import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    return text

    fp.close()
    device.close()
    retstr.close()

# allows for input of specific file, then conversion
# remember that it adds a random space at the end that messes up the proper path
'''
def extract_pdf_text_from_file():
    os.system('open .')
    input_file = input('Copy and paste your target PDFs path here')
    text = convert_pdf_to_txt(input_file)
    return text
'''


def save_to_file(text):
    new_file = open("exampleText.txt", "w+")
    # writes the text to file
    new_file.write(text)
    new_file.write("\n*************************************************"
                   "*************************************************\n")


