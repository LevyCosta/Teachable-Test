from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service(executable_path='./chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://takehome.zeachable.com/')