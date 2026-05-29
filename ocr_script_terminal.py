from PIL import Image
import pytesseract
import numpy as np
from PIL import PdfImagePlugin
import cv2
from pathlib import Path
import os

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

filename = "ocr.png"
img1 = cv2.imread("ocr.png", cv2.IMREAD_GRAYSCALE)
img2 = np.array(Image.open(filename))

scale_factor = 1
width = int(img1.shape[1] * scale_factor)
height = int(img1.shape[0] * scale_factor)
resized_image = cv2.resize(img1, (width, height))#, interpolation=cv2.INTER_LANCZOS4)
_, binary_image = cv2.threshold(resized_image, 127, 255, cv2.THRESH_BINARY)
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(binary_image, config=custom_config)

text1 = pytesseract.image_to_string(img2)
if text1 == "TEXT":
    mypath = fr"C:\Users\Emanuel-Tiberiu Petr\Desktop\OCR_Script\{text1}"
    if not os.path.isdir(mypath):
        os.makedirs(mypath)

print(text1)