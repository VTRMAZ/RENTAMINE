#je test githcd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
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
 
def tout(nb_max):
    #chaine a completer
    chaine=['Etchash','RandomX','Equihash','Ethash','KawPow','Equihash 125,4','Lyra2REv2','Skein','Autolykos 2','Eaglesong','Octopus','kHeavyHash','Cuckoo Cycle']
     #cest good  faire teste xpath for all mais teste plus rapide sur 50     
    browser.find_element(By.XPATH, '//*[@id="coins_length"]/label/select/option[3]').click()

   
    for i in range (1,nb_max):
        try:
            EMISSION1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[5]/div'.format(i))
            PRICE1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[6]/span'.format(i))
            NETWORKHASH1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[11]'.format(i))
            ALGO1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[3]/div'.format(i))
            for j in range (0,15):
                if (NETWORKHASH1.text and PRICE1.text and EMISSION1.text and ALGO1.text==chaine[j]):#faut aussi sup si c'est egale a zero car apres div par 0
                    NAME1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[2]/div/a/b'.format(i))
                    ACRONYME1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[2]/div/small'.format(i))
                    ALGO1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[3]/div'.format(i))
                    print(f"{i} - ", NAME1.text, ACRONYME1.text,ALGO1.text,PRICE1.text, EMISSION1.text,NETWORKHASH1.text)
                    DICO={}
                    DICO[NAME1.text]=ACRONYME1.text,ALGO1.text
                    print(DICO)
                    
            
        except:
                continue

    
tout(20)
  
browser.quit()
