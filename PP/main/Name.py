from selenium import webdriver
import pytest
import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import sleep
import requests
from bs4 import BeautifulSoup
from subprocess import CREATE_NO_WINDOW #Windows only
 
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('window-size=1920x1080')
 
chrome_service = Service('chromedriver')
chrome_service.creationflags = CREATE_NO_WINDOW
 
browser = webdriver.Chrome(options=chrome_options, service=chrome_service)
 
url='https://miningpoolstats.stream/'


response =requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.text, "html.parser") 
    
browser.get(url)
sleep(5) #Ce n'est pas la meilleure méthode...
def tout():
    #for j in (0,28):    
        for i in range (1,10):
            #Prend tout les names d'une page
            NAME1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[2]/div/a/b'.format(i))
            ACRONYME1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[2]/div/small'.format(i))
            ALGO1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[3]/div'.format(i))
            PRICE1AVECSIGNE=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[6]/span'.format(i))
            #EMISSION1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[5]/div'.format(i)) faire si pas de donner passer
            NETWORKHASH1AVECSIGNE=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[11]'.format(i))
            print(NAME1.text,ACRONYME1.text,ALGO1.text,PRICE1AVECSIGNE.text,NETWORKHASH1AVECSIGNE.text)
            

        #teste de mettre page 2 puis page 3 avec bouvle qui modifie path
        browser.find_element(By.LINK_TEXT, "Next").click()
        #sleep(2)
        j=j+1


tout()

browser.quit()