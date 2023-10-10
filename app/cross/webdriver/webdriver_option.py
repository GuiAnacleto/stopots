from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from variables.variables import WEBDRIVER_PATH

class webdriverOptions:
    def normal():
        options = Options()
        options.add_argument("--window-size=1080,720")
        driver = webdriver.Chrome(options= options)
        return driver
    def headless():
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1080,720")
        driver = webdriver.Chrome(options= options)
        return driver