import pyttsx3
from pypdf import PdfReader

# Extracting text from PDF
reader = PdfReader('gcf_answer.pdf')
page = reader.pages[0]
text = page.extract_text()

# Text-to-speech
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
