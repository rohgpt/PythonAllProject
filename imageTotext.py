import pytesseract
import pyttsx3 as speak
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# this is path of tesseract software that is needed for Converting Image to text or pdf


def Convert():
    img = Image.open('2.jpg')
    text = pytesseract.image_to_string(img, lang='hin')
    print(text)
    w = speak.init()
    speak.speak(text)


Convert()
