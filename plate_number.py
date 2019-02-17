import pytesseract
from PIL import Image


im = Image.open("b.png")
txt = pytesseract.image_to_string(im)
print(txt)