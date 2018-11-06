import PyPDF2
import os
import easygui
from gtts import gTTS
import re
file = easygui.fileopenbox(msg="Select your PDF", title="Select an PDF File",default="*.pdf",filetypes=["*.pdf",])
file_path = file

if(os.path.exists(file_path)):
    pass
else:
    print("File does not exists")
    exit()

f = open(file_path, 'rb')

pdffile = PyPDF2.PdfFileReader(f)
no_of_pages = pdffile.getNumPages()

# Using regex to filter only words and numbers

string_words = ''
for pageno in range(no_of_pages):
    pi = pdffile.getPage(pageno)
    page = pdffile.getPage(pageno)
    content = page.extractText()
    textonly = re.findall(r'[a-zA-Z0-9]+', content)
    for word in textonly:
        string_words = string_words + ' ' + word

# Convert the string of words to mp3 file 
tts = gTTS(text=string_words, lang='en')
tts.save("listen_pdf.mp3")

