import logging
from selenium.webdriver.common.by import By
from app.cross.webdriver.webdriver_option import webdriverOptions
from variables.variables import STOPOTS_LINK

class anonimous:
    def __init__(self, username = "Anonimo Generico"):
        self.__username = username
        self.__webdriver = webdriverOptions.normal()

    def login(self, ):
        #Clica no botão anonimo e preenche o nome escolhido pelo usuario
        self.__webdriver.get(STOPOTS_LINK)
        self.__webdriver.find_element(By.XPATH, "/html/body/header/div[1]/div[2]/div[1]/form/button").click()
        logging.info(msg="Login Efetuado com Sucesso")
