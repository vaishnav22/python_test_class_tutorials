from PIL import Image
import pytesseract

im = Image.open("vrkIj.png")
txt = pytesseract.image_to_string(im,lang='english')
print(txt)