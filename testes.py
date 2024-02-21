import pyautogui as py
import pandas as pd
locadora = 'C:/Users/anderson.filho/PycharmProjects/pythonProject/Detran_loc/LOCADORA_2024.xlsx'
locadora_df = pd.read_excel(locadora)

renavam = str(locadora_df.loc[4,'Renavam'])
py.sleep(1)
py.hotkey('Ctrl','s'),py.sleep(2),py.press('Backspace'),py.typewrite(renavam),py.sleep(1)
py.press('Tab'),py.press('Tab'),py.press('Tab'),py.press('Enter')