from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# Inicializar o driver do navegador
driver = webdriver.Chrome()

# Abrir a página da web
driver.get("https://online6.detran.pe.gov.br/ServicosWeb/VeiculoMVC/ConsultaPlaca/ConsultarPlaca")

# Esperar até que o campo esteja presente na página
campo_placa = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "placa"))
)

# Inserir os dados da placa
campo_placa.send_keys("RZX6C85")
#Após a inserção da Placa, necessario validar ou quebrar o Captha ( ainda em desenvolvimento) .
# Clicar no botão "CONSULTAR" usando JavaScript
botao_consultar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "consultar"))
)
driver.execute_script("arguments[0].click();", botao_consultar)

pyautogui.sleep(250)