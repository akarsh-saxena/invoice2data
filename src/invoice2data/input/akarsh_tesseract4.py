import pytesseract
from PIL import Image

def to_text(path, lang='eng'):
	text = pytesseract.image_to_string(Image.open(path), lang=lang, config='--oem 1 --psm 4')
	return text
