import pytesseract
from PIL import Image

def to_text(path, lang='eng'):
	pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
	text = pytesseract.image_to_string(Image.open(path), lang=lang, config='--oem 1 --psm 3')
	return text