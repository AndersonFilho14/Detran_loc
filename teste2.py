import pyautogui as py

py.sleep(2)
import pandas as pd

locadora = 'C:/Users/anderson.filho/PycharmProjects/pythonProject/Detran_loc/LOCADORA_2024.xlsx'
locadora_df = pd.read_excel(locadora)
renavam = str(locadora_df.loc[3,'Renavam'])
print(renavam)
py.sleep(1)
py.PAUSE = 1
py.hotkey('Ctrl','s'),py.press('Backspace'),py.typewrite(renavam),py.sleep(1)
py.press('Tab'),py.press('Tab'),py.press('Tab'),py.press('Enter')

#leitura do boleto
import PyPDF2
#pegando o dados bancario
with open('C:/Users/anderson.filho/Pictures/{renavam}.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # Obtenha o número total de páginas
    num_pages = len(pdf_reader.pages)
    # Obtenha o objeto da última página
    last_page = pdf_reader.pages[-1]
    # Extraia o texto da última página
    text_last_page = last_page.extract_text()
    # Divida o texto em linhas
    lines = text_last_page.split('\n')
    last_line = lines[-7]
    print(last_line)