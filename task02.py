from PyPDF2 import PdfFileReader
from pathlib import Path
pdf = PdfFileReader('SeniorExpertAgreement01.pdf')
page_1_object = pdf.getPage(0)
print(page_1_object)
page_1_text = page_1_object.extractText()
print(page_1_text)

with Path ('Senior_Expert_text.csv').open(mode='w') as output_file:
    text = ''
    for page in pdf.pages:
        text = page.extractText()
        output_file.write(text)

