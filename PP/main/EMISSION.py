from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from subprocess import CREATE_NO_WINDOW #Windows only
 
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('window-size=1920x1080')
 
chrome_service = Service('chromedriver')
chrome_service.creationflags = CREATE_NO_WINDOW
 
browser = webdriver.Chrome(options=chrome_options, service=chrome_service)
 
url='https://miningpoolstats.stream/'
browser.get(url)
sleep(5) #Ce n'est pas la meilleure méthode...
for i in range(1,10):  
    EMISSION=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[5]/div'.format(i))
    if (EMISSION==#float):
        print(EMISSION.text)
    else:
        continue()



browser.quit()