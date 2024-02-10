import pyautogui as py

py.sleep(4),py.press('PageUP'),py.sleep(1)
imagem_pagar = py.locateCenterOnScreen('C:\\Users\\filho\\PycharmProjects\\Detran_loc\\pagar.png',confidence=0.7)
py.click(imagem_pagar.x,imagem_pagar.y)


