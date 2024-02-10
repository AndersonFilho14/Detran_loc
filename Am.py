import time
import pandas as pd

locadora = 'C:\\Users\\filho\\PycharmProjects\\Detran_loc\\LOCADORA_2024.xlsx'
locadora_df = pd.read_excel(locadora)

renavam = str(locadora_df.loc[3,'Renavam'])
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
imagem_veiculo = py.locateCenterOnScreen('C:\\Users\\filho\\PycharmProjects\\Detran_loc\\Veiculos.png',confidence=0.7)
py.click(imagem_veiculo.x,imagem_veiculo.y)

#Clicar na imagem de 'licenciamento manual'
py.sleep(2)
imagem_licenciamento = py.locateCenterOnScreen('C:\\Users\\filho\\PycharmProjects\\Detran_loc\\licenciamento.png',confidence=0.7)
py.click(imagem_licenciamento.x,imagem_licenciamento.y)


#Passar pelo captcher; sem estar marcado
py.sleep(2)
py.press('Tab'),py.press('Tab'),py.sleep(1)
py.typewrite(renavam),py.press('Backspace'),py.sleep(1)
py.press('Tab'),py.press('Tab'),py.sleep(1),py.press('Enter')
py.sleep(2),py.press('Tab'),py.press('Tab'),py.press('Tab'),py.press('Tab'),py.press('Enter')


#Caso apareça, clicar na imagem de 'cancelar protocolo'
py.sleep(2),py.press('Down'),py.sleep(1)
imagem_cancelarP = 'C:\\Users\\filho\\PycharmProjects\\Detran_loc\\cancelarP.png'
try:
    # Tenta localizar a imagem na tela
    posicao = py.locateCenterOnScreen(imagem_cancelarP,confidence=0.7)
    # Se a imagem for encontrada, clique nela
    if posicao is not None:
        py.click(posicao)
        print("Imagem encontrada e clicada com sucesso!")
    else:
        print("Imagem não encontrada na tela. Continuando para a próxima etapa.")
# Se ocorrer uma exceção (imagem não encontrada), continue para a próxima etapa
except py.ImageNotFoundException:
    print("Imagem não encontrada na tela. Continuando para a próxima etapa.")


#Clicar no botao de 'solicitar' para pegar o boleto

py.sleep(3),py.press('PageDown'),py.sleep(1)
imagem_solicitar = py.locateOnScreen('C:\\Users\\filho\\PycharmProjects\\Detran_loc\\solicitar.png',confidence=0.7)
py.click(imagem_solicitar)


#CLicar em "pagar taxa do detran " para pegar boleto
py.sleep(4),py.press('PageUP'),py.sleep(1)
imagem_pagar = py.locateCenterOnScreen('C:\\Users\\filho\\PycharmProjects\\Detran_loc\\pagar.png',confidence=0.7)
py.click(imagem_pagar.x,imagem_pagar.y)
#Colocar o codigo do banco na planilha

#alteração git
