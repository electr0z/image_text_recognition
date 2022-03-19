import pytesseract
from PIL import Image

# img = Image.open('png-clipart-number-drawing-font-others-miscellaneous-blue.png')
img = Image.open('dfdfdf.png')
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# custom_config = r'--oem 3 --psm 13'
custom_config = r'--oem 3 --psm 6'

filename = img.filename.split('.')[0]

text = pytesseract.image_to_string(img, config=custom_config)
print(text)

with open(f'{filename}.txt', 'w') as file:
    file.write(text)
