import time
import pandas as pd


locadora = 'C:\\Users\\anderson.filho\\Documents\\PDF\\LOCADORA_2024.xlsx'
locadora_df = pd.read_excel(locadora)


renavam = str(locadora_df.loc[1,'Renavam'])
print(renavam)

UF_Choose = 'AM'
#abrindo o chrome
import os
# Especifique o caminho para o executável do Google Chrome
link_AM = "https://digital.detran.am.gov.br/"

# Abra o Google Chrome
os.system(f"start {link_AM}")


# clicando na imagem de veiculos
import pyautogui as py
py.sleep(4)
imagem_veiculo = py.locateCenterOnScreen('C:\\Users\\anderson.filho\\Pictures\\Veiculos.png',confidence=0.7)
py.click(imagem_veiculo.x,imagem_veiculo.y)


#Clicar na imagem de 'licenciamento manual'
py.sleep(2)
imagem_licenciamento = py.locateCenterOnScreen('C:\\Users\\anderson.filho\\Pictures\\licenciamento.png',confidence=0.7)
py.click(imagem_licenciamento.x,imagem_licenciamento.y)

#Passar pelo captcher; sem estar marcado
py.sleep(2)
py.press('Tab'),py.press('Tab'),py.sleep(1)
py.typewrite(renavam),py.press('Backspace'),py.sleep(1)

py.press('Tab'),py.press('Tab'),py.sleep(1),py.press('Enter')
py.sleep(2),py.press('Tab'),py.press('Tab'),py.press('Tab'),py.press('Tab'),py.press('Enter')

#Caso apareça, clicar na imagem de 'cancelar protocolo'
py.sleep(2)
py.press('Down'),py.press('Down')
imagem_cancelarP = py.locateOnScreen('C:/Users/anderson.filho/Pictures/cancelarP.png',confidence=0.7)
if imagem_cancelarP is not None:
   imagem_cancelarP = py.locateOnScreen('C:/Users/anderson.filho/Pictures/cancelarP.png', confidence=0.7)
   x, y = py.center(imagem_cancelarP)
   py.click(x, y)
else:
   print('n teve 0 cacelamento de protocolo')

#Clicar no botao de 'solicitar' para pegar o boleto
py.sleep(2)
py.press('PageDown')
imagem_solicitar = py.locateOnScreen('C:\\Anderson\\Captures\\Screenshots\\solicitar.png',confidence=0.7)
py.click(imagem_solicitar.x,imagem_solicitar.y)

#CLicar em "pagar taxa do detran " para pegar boleto
py.sleep(4)
py.press('PageDown')
py.press('Up'),py.press('Up'),py.press('Up'),py.press('Up')
imagem_pagar = py.locateCenterOnScreen('C:\\Users\\anderson.filho\\Pictures\\pagar.png',confidence=0.7)
py.click(imagem_pagar.x,imagem_pagar.y)
#Colocar o codigo do banco na planilha

