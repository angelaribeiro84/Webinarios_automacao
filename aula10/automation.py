from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def abrir_pagina():
    driver = webdriver.Chrome()

    driver.get('https://www.automationexercise.com/login')

    return driver

def testar_login_inexistente():

    driver = abrir_pagina()

    time.sleep(15)

    campo_username = driver.find_element(By.CSS_SELECTOR, '#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=email]:nth-child(2)')
    campo_username.send_keys('eduardomiranda@tripleten-team.com')

    campo_senha = driver.find_element(By.CSS_SELECTOR, '#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=password]:nth-child(3)')
    campo_senha.send_keys('senhasenha')

    botao_de_login = driver.find_element(By.CSS_SELECTOR, '#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > button')
    botao_de_login.click()

    mensagem_de_erro_do_login = driver.find_element(By.CSS_SELECTOR, '#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > p')

    mensagem_de_erro_do_login.is_displayed()


def testar_cadastro():

    driver = abrir_pagina()

    time.sleep(15)
    
    campo_name = driver.find_element(By.CSS_SELECTOR, '#form > div > div > div:nth-child(3) > div > form > input[type=text]:nth-child(2)')
    campo_name.send_keys('Eduardo M')

    campo_email = driver.find_element(By.CSS_SELECTOR, '#form > div > div > div:nth-child(3) > div > form > input[type=email]:nth-child(3)')
    campo_email.send_keys('eduardomiranda@tripleten-team.com')

    botao_de_cadastro = driver.find_element(By.CSS_SELECTOR, '#form > div > div > div:nth-child(3) > div > form > button')
    botao_de_cadastro.click()

    account_more_info_text = driver.find_element(By.CSS_SELECTOR, '#form > div > div > div > div.login-form > h2 > b')
    
    account_more_info_text.is_displayed()




 ## Código principal (main)
print('Testando login...')
testar_login_inexistente()

print('Testando cadastro...')
testar_cadastro()