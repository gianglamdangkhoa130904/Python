from selenium import webdriver
import webbrowser as wb
from time import sleep

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://facbook.com")