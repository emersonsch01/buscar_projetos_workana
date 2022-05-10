from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time

# dados de login e senha
login = ''
senha = ''


# inserir dentro da lista as palavras de busca (dentro das aspas)
lista_palavras = ['', '', '', '', '', '', '', '', '', '', '']

options = ChromeOptions()
options.add_argument("--headless")
options.add_argument("--log-level=3")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://www.workana.com/login?ref=home_top_bar')
driver.maximize_window()
time.sleep(5)
try:
    cookies = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
    cookies.click()
except:
    pass
time.sleep(2)
driver.find_element(By.NAME, 'email').send_keys(login)
time.sleep(1)
driver.find_element(By.NAME, 'password').send_keys(senha)
time.sleep(1)
driver.find_element(By.NAME, 'submit').click()
time.sleep(3)
driver.find_element(
    By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[2]/a').click()
time.sleep(3)
lista_projetos = []
# alterar o numero dentro do range para a quantidade de páginas desejadas na busca
for i in range(20):
    driver.get('https://www.workana.com/jobs?language=pt&page=' + str(i + 1))
    time.sleep(3)
    titulos = driver.find_elements(By.CLASS_NAME, 'project-header')
    time.sleep(1)
    for titulo in titulos:
        texto = titulo.find_element(By.TAG_NAME, 'span').text
        lista_projetos.append(texto.lower())
    time.sleep(5)
lista_final = []
for palavra in lista_palavras:
    for projeto in lista_projetos:
        if palavra in projeto:
            lista_final.append(projeto)
for final in lista_final:
    print('\n' + final)

fim = input('DIGITE ENTER PARA FINALIZAR...')
