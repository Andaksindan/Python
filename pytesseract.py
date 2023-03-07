import pytesseract
from PIL import Image

# import pytesseract as pt
# text = pt.image_to_string(img)


# Load the image
image = Image.open('basic-symbols-table.jpg')

# Convert the image to grayscale
image = image.convert('L')

# Use Pytesseract to extract the text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
