from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import openpyxl

# Configurando as opções do Chrome para o modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executar em modo headless
chrome_options.add_argument("--no-sandbox")  # Necessário para o Linux
chrome_options.add_argument("--disable-dev-shm-usage")  # Necessário para o Linux

# Configurando o caminho para o ChromeDriver
#chrome_driver_path = "/home/andre/.cache/selenium/chromedriver/linux64/123.0.6312.105/chromedriver"
chrome_driver_path = "./chromedriver"
# Configurando o serviço do ChromeDriver
service = Service(chrome_driver_path)

# Inicializando o driver do Chrome com as opções configuradas
driver = webdriver.Chrome(service=service, options=chrome_options)

# Definindo o tempo de espera implícito
driver.implicitly_wait(10)

# Abrindo a página desejada
driver.get("https://sau.ssp.sc.gov.br/index.php?category=29&a=add")

try:
    print("Preenchendo campo de nome...")
    name_input = driver.find_element(By.NAME, "name")
    name_input.send_keys("André Gonçalves")

    print("Preenchendo campo de e-mail...")
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("andregoncalves@ssp.sc.gov.br")

    print("Preenchendo campo de ramal...")
    ramal_input = driver.find_element(By.NAME, "custom2")
    ramal_input.send_keys("58123")

    print("Esperando até que o campo de seleção esteja disponível...")
    campo_selecao = driver.find_element(By.ID, "custom1-selectized")
    driver.execute_script("arguments[0].removeAttribute('disabled')", campo_selecao)

    print("Clicando no campo de seleção...")
    campo_selecao.click()

    print("Esperando até que a opção desejada esteja disponível...")
    opcao_desejada = driver.find_element(By.XPATH, "//div[@class='option' and text()='SSP  - DTI- 5º ANDAR.']")
    opcao_desejada.click()

    print("Preenchendo campo de mensagem...")
    assunto_input = driver.find_element(By.NAME, "subject")
    assunto_input.send_keys("{ALERT.SUBJECT}")

    print("Preenchendo campo de mensagem...")
    mensagem_input = driver.find_element(By.NAME, "message")
    mensagem_input.send_keys("{ALERT.MESSAGE}")

    sleep(10)

    # Esperar até que o botão de envio esteja visível e clicável
    botao_enviar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "recaptcha-submit"))
    )

    # Clicar no botão de envio
    botao_enviar.click()

except Exception as e:
    print("Erro ao preencher os campos:", e)

finally:
    driver.quit()  # Certifique-se de fechar o navegador após o uso
