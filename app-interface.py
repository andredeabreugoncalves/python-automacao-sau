from tkinter import Tk, Label, Entry, Button
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import openpyxl

def enviar_chamado():
    # Configurando o caminho para o ChromeDriver
    # chrome_driver_path = "/home/andre/.cache/selenium/chromedriver/linux64/123.0.6312.105/chromedriver"
    chrome_driver_path = "/usr/local/bin/chromedriver"

    # Configurando o serviço do ChromeDriver
    service = Service(chrome_driver_path)

    # Inicializando o driver do Chrome
    driver = webdriver.Chrome(service=service)
    #driver = webdriver.Chrome(executable_path=webdriver_path)

    # Definindo o tempo de espera implícito
    driver.implicitly_wait(2)

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

        #sleep(10)

        # Preencher com os dados da interface
        assunto = assunto_entry.get()
        mensagem = mensagem_entry.get()

        # Preencher campos do formulário com os dados da interface
        assunto_input = driver.find_element(By.NAME, "subject")
        assunto_input.send_keys(assunto)
        mensagem_input = driver.find_element(By.NAME, "message")
        mensagem_input.send_keys(mensagem)
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

# Criar a janela principal
root = Tk()
root.title("Envio de Chamado")

# Label e Entry para o assunto do chamado
assunto_label = Label(root, text="Assunto:")
assunto_label.grid(row=0, column=0, padx=10, pady=5)
assunto_entry = Entry(root)
assunto_entry.grid(row=0, column=1, padx=10, pady=5)

# Label e Entry para a mensagem do chamado
mensagem_label = Label(root, text="Mensagem:")
mensagem_label.grid(row=1, column=0, padx=10, pady=5)
mensagem_entry = Entry(root)
mensagem_entry.grid(row=1, column=1, padx=10, pady=5)

# Botão para enviar o chamado
enviar_button = Button(root, text="Enviar Chamado", command=enviar_chamado)
enviar_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Executar a interface
root.mainloop()
