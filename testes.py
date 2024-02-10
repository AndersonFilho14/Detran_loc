import cv2
import pytesseract

img = cv2.imread("boleto.pdf")
pytesseract.pytesseract.tesseract_cmd = "C:/Users/filho/tesseract.exe"
res = pytesseract.image_to_string(img)
print(res)

#lembrando de instalar o pytesseract