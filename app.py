from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import openpyxl

# Configurando o caminho para o ChromeDriver
#chrome_driver_path = "/home/andre/.cache/selenium/chromedriver/linux64/123.0.6312.105/chromedriver"
chrome_driver_path = "/usr/local/bin/chromedriver"

# Configurando o serviço do ChromeDriver
service = Service(chrome_driver_path)

# Inicializando o driver do Chrome
driver = webdriver.Chrome(service=service)

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

    sleep(10)

    # Carregar a planilha Excel
    print("Carregar a planilha Excel...")
    chamados = openpyxl.load_workbook('/home/andre/python/chamados.xlsx')
    pag_chamados = chamados['chamado']  # Certifique-se de alterar o nome da planilha conforme necessário

    # Iterar sobre as linhas da planilha
    for linha in pag_chamados.iter_rows(min_row=2, values_only=True):
        Assunto, Mensagem = linha
        # Faça algo com os dados de cada linha, como preencher campos do formulário
        # Exemplo:
        assunto_input = driver.find_element(By.NAME, "subject")
        assunto_input.send_keys(Assunto)
        mensagem_input = driver.find_element(By.NAME, "message")
        mensagem_input.send_keys(Mensagem)
        sleep(2)

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

