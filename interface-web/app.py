from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import openpyxl

app = Flask(__name__)

# Configurando o caminho para o ChromeDriver
chrome_driver_path = "/home/andre/.cache/selenium/chromedriver/linux64/123.0.6312.105/chromedriver"

# Inicializando o driver do Chrome
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

def enviar_chamados(nome, email, ramal, assunto, mensagem):
    try:
        # Abrindo a página desejada
        driver.get("https://sau.ssp.sc.gov.br/index.php?category=29&a=add")

        # Preenchendo os campos do formulário
        driver.find_element(By.NAME, "name").send_keys(nome)
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.NAME, "custom2").send_keys(ramal)

        # Esperando até que o campo de seleção esteja disponível
        campo_selecao = driver.find_element(By.ID, "custom1-selectized")
        driver.execute_script("arguments[0].removeAttribute('disabled')", campo_selecao)

        # Clicando no campo de seleção
        campo_selecao.click()

        # Esperando até que a opção desejada esteja disponível
        opcao_desejada = driver.find_element(By.XPATH, "//div[@class='option' and text()='SSP  - DTI- 5º ANDAR.']")
        opcao_desejada.click()

        # Preenchendo os campos do formulário com os dados fornecidos
        driver.find_element(By.NAME, "subject").send_keys(assunto)
        driver.find_element(By.NAME, "message").send_keys(mensagem)
        sleep(2)

        # Esperar até que o botão de envio esteja visível e clicável
        botao_enviar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "recaptcha-submit"))
        )

        # Clicar no botão de envio
        botao_enviar.click()

    except Exception as e:
        raise RuntimeError(f"Erro ao enviar chamado: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Obter os dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        ramal = request.form['ramal']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        # Enviar os chamados
        enviar_chamados(nome, email, ramal, assunto, mensagem)

        return "Chamados enviados com sucesso!"

    except Exception as e:
        return f"Erro ao enviar chamados: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

