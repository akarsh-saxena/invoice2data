import pytesseract
from PIL import Image

def to_text(path, lang='eng', oem='1', psm='3'):
	text = pytesseract.image_to_string(Image.open(path), lang=lang, config='--oem '+oem+' --psm '+psm)
	return text
