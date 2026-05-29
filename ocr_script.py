from PIL import Image
from pytesseract import *
import numpy as np
import cv2
from PIL import PdfImagePlugin



pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

filename = "ocr.png"

img1 = cv2.imread(filename)
#text = pytesseract.image_to_string(img1)
results = pytesseract.image_to_data(img1, output_type=Output.DICT)
for i in range(0, len(results["text"])):
    x = results["left"][i]
    y = results["top"][i]

    w = results["width"][i]
    h = results["height"][i]

    text = results["text"][i]
    conf = int(results["conf"][i])

    if conf > 60:
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img1, text, (x, y - 10), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)

cv2.imshow("dokument",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()