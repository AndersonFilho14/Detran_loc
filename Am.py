import time
import pandas as pd

locadora = 'C:/Users/anderson.filho/PycharmProjects/pythonProject/Detran_loc/LOCADORA_2024.xlsx'
locadora_df = pd.read_excel(locadora)

renavam = str(locadora_df.loc[4,'Renavam'])
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
imagem_veiculo = py.locateCenterOnScreen('C:/Users/anderson.filho/Pictures/Veiculos.png',confidence=0.7)
py.click(imagem_veiculo.x,imagem_veiculo.y)

#Clicar na imagem de 'licenciamento manual'
py.sleep(2)
imagem_licenciamento = py.locateCenterOnScreen('C:/Users/anderson.filho/Pictures/licenciamento.png',confidence=0.7)
py.click(imagem_licenciamento.x,imagem_licenciamento.y)


#Passar pelo captcher; sem estar marcado
py.sleep(2)
py.press('Tab'),py.press('Tab'),py.sleep(1)
py.typewrite(renavam),py.press('Backspace'),py.sleep(1)
py.press('Tab'),py.press('Tab'),py.sleep(1),py.press('Enter')
py.sleep(2),py.press('Tab'),py.press('Tab'),py.press('Tab'),py.press('Tab'),py.press('Enter')


#Caso apareça, clicar na imagem de 'cancelar protocolo'
py.sleep(3),py.press('Down'),py.sleep(1)
imagem_cancelarP = 'C:/Users/anderson.filho/Pictures/cancelarP.png'
try:
    # Tenta localizar a imagem na tela
    posicao = py.locateCenterOnScreen(imagem_cancelarP,confidence=0.7)
    # Se a imagem for encontrada, clique nela
    if posicao is not None:
        py.click(posicao)
        print("Imagem de cancelarP encontrada e clicada com sucesso!")
    else:
        print("Imagem de cancelarP não .")
# Se ocorrer uma exceção (imagem não encontrada), continue para a próxima etapa
except py.ImageNotFoundException:
    print("Imagem não encontrada na tela. Continuando para a próxima etapa.")


#Clicar no botao de 'solicitar' para pegar o boleto

py.sleep(3),py.press('PageDown'),py.sleep(1)
imagem_solicitar = 'C:/Users/anderson.filho/Pictures/solicitar.png'
try:
    # Tenta localizar a imagem na tela
    posicao = py.locateCenterOnScreen(imagem_solicitar, confidence=0.7)
    # Se a imagem for encontrada, clique nela
    if posicao is not None:
        py.click(posicao)
        print("Imagem de solicitar encontrada e clicada com sucesso!")
    else:
        print("Imagem de Solicitar não .")
# Se ocorrer uma exceção (imagem não encontrada), continue para a próxima etapa
except py.ImageNotFoundException:
    print("Imagem não encontrada na tela. Continuando para a próxima etapa.")


#CLicar em "pagar taxa do detran " para pegar boleto
py.sleep(4),py.press('PageUP'),py.press('PageUP'),py.sleep(2),py.press('PageUP')
imagem_pagar = py.locateCenterOnScreen('C:/Users/anderson.filho/Pictures/pagar.png',confidence=0.7)
py.click(imagem_pagar.x,imagem_pagar.y)

#salvar boleto
py.sleep(3)
py.hotkey('Ctrl','s'),py.sleep(2),py.press('Backspace'),py.typewrite(renavam),py.sleep(1)
py.press('Tab'),py.press('Tab'),py.press('Tab'),py.press('Enter')

#pegando dados bancario do boleto

py.sleep(2)
import PyPDF2
boleto = (f'C:/Users/anderson.filho/Pictures/{renavam}.pdf')
with open(boleto, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # Obtenha o número total de páginas
    num_pages = len(pdf_reader.pages)
    # Obtenha o objeto da última página
    last_page = pdf_reader.pages[-1]
    text_last_page = last_page.extract_text()
    lines = text_last_page.split('\n')
    dados_bancario = lines[-7]
    print(dados_bancario)

#Colocar o codigo do banco na planilha

#testando