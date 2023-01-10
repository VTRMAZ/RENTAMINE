network= '54 Th/s'
price='17 $'#price pas utile
emission= '17.6M $'
lennet=len(network)
lenprice=len(price)
lenemi=len(emission)
networkchiffre=network[0:lennet-4]
pricechiffre=price[0:lenprice-1]
emissionchiffre=emission[0:lenemi-3]
networkfloat=float(networkchiffre.replace(',',''))
pricefloat=float(pricechiffre.replace(',',''))
emissionfloat=float(emissionchiffre.replace(',',''))
Yourhash=float(input("Rentre ton hash\n"))



for i, c in enumerate(network):
    if c == "T" or c == "P" or c == "G"or c == "M"or c == "K":
        for j, l in enumerate(network):
            if l=="P":
                networkfloat=networkfloat*(1000**3) 
                print("iciiii") 
                break
        for j, l in enumerate(network):
            if l=="T":
                networkfloat=networkfloat*(1000**2)  
                break     
        for j, l in enumerate(network):
            if l=="G":
                networkfloat=networkfloat*(1000)  
                break
        for j, l in enumerate(network):
            if l=="M":
                networkfloat=networkfloat*1  
                break
        for j, l in enumerate(network):
            if l=="K":
                networkfloat=networkfloat/1000
                break         
        for j, l in enumerate(network):
            if l!="T" and l != "P" and l != "G"and l != "M"and l != "K" and l != "0"and l != "1" and l != "2" and l != "3" and l != "4" and l != "5" and l != "6" and l != "7" and l != "8" and l != "9" and l != "/" and l != " " and l != "H"and l != "s" and l != "." and l != "o" and l != "l" and l != "S" and l != "i" and l != "B" and l != "p" and l != "h":
                networkfloat=networkfloat/(1000**2)
                print('ici')
                break 
                   
       
    
 
for o, m in enumerate(emission):
    if (m == "M"or m == "K"):
        for e, n in enumerate(emission):
            if n=="M":
                emissionfloat=emissionfloat*(1000**2)  
                
                break
        for e, n in enumerate(emission):
            if n=="K":
                emissionfloat=emissionfloat*(1000)   
                break   
       # for e, n in enumerate(emission):
          #  if n!="M" or n!="K":
           #     emissionfloat=emissionfloat/1
   
resultat=(Yourhash/networkfloat)*emissionfloat
print(resultat)    
    
#Programme qui transforme les chaines en float et retire les unités 
'''   
network= '5,4 Th/s'
Yourhash=0
len=len(network)
networkchiffre=network[0:len-4]
networkfloat=float(networkchiffre.replace(',',''))
#type(networkfloat)
Yourhash=float(input("Rentre ton hash\n"))
resultat=Yourhash/networkfloat
print(resultat)

'''
#Marche 

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
    chaine=['Etchash','RandomX','Ethash','KawPow','Equihash 125,4','Lyra2REv2','Skein','Autolykos 2','Eaglesong','Octopus','kHeavyHash','Cuckoo Cycle']
     #cest good  faire teste xpath for all mais teste plus rapide sur 50     
    browser.find_element(By.XPATH, '//*[@id="coins_length"]/label/select/option[3]').click()
    Yourhash=float(input("Rentre ton hash\n"))
   
    for i in range (1,nb_max):
        try:
            EMISSION1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[5]/div'.format(i))
            PRICE1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[6]/span'.format(i))
            NETWORKHASH1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[11]'.format(i))
            ALGO1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[3]/div'.format(i))
            for j in range (0,15):
                if (NETWORKHASH1.text and PRICE1.text and EMISSION1.text and ALGO1.text==chaine[j]):#faut aussi sup si c'est egale a zero car apres div par 0
                    if chaine[j]==chaine[1]:
        
                        ratio=50
                        
                        NETWORKHASH1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[11]'.format(i))
                        EMISSION1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[5]/div'.format(i))

                        
                        NETWORKHASH2=str(NETWORKHASH1.text)
                        EMISSION2=str(EMISSION1.text)
                        

                        lennet=len(NETWORKHASH2)
                        #lenprice=len(PRICE2)
                        lenemi=len(EMISSION2)
                        print(lennet)
                        networkchiffre=NETWORKHASH2[0:lennet-4]
                        #pricechiffre=PRICE1[0:lenprice-1]
                        emissionchiffre=EMISSION2[0:lenemi-3]
                        
                        networkfloat=float(networkchiffre.replace(',',''))
                        #pricefloat=float(pricechiffre.replace(',',''))
                        emissionfloat=float(emissionchiffre.replace(',',''))
                        
                        
                        for z, c in enumerate(NETWORKHASH2):
                            if c == "T" or c == "P" or c == "G"or c == "M"or c == "K":
                                for y, l in enumerate(NETWORKHASH2):
                                    if l=="T":
                                        networkfloat=networkfloat*(1000**3) 
                                        break
                                for y, l in enumerate(NETWORKHASH2):
                                    if l=="P":
                                        networkfloat=networkfloat*(1000**2)
                                        break     
                                for y, l in enumerate(NETWORKHASH2):
                                    if l=="G":
                                        networkfloat=networkfloat*(1000)  
                                        break
                                for y, l in enumerate(NETWORKHASH2):
                                    if l=="M":
                                        networkfloat=networkfloat*1  
                                        break
                                for y, l in enumerate(NETWORKHASH2):
                                    if l=="K":
                                        networkfloat=networkfloat/1000
                                        break         
                                for y, l in enumerate(NETWORKHASH2):
                                    if l!="T" and l != "P" and l != "G"and l != "M"and l != "K" and l != "0"and l != "1" and l != "2" and l != "3" and l != "4" and l != "5" and l != "6" and l != "7" and l != "8" and l != "9" and l != "/" and l != " " and l != "H"and l != "s" and l != "." and l != "o" and l != "l" and l != "S" and l != "i" and l != "B" and l != "p" and l != "h":
                                        networkfloat=networkfloat/(1000**2)
                                        break
                                        
                            
                            
                        
                        for o, m in enumerate(EMISSION2):
                            if (m == "M"or m == "K"):
                                for e, n in enumerate(EMISSION2):
                                    if n=="M":
                                        emissionfloat=emissionfloat*(1000**2)  
                                       
                                        break
                                for e, n in enumerate(EMISSION2):
                                    if n=="K":
                                        emissionfloat=emissionfloat*(1000)   
                                        break 
                                
                                
                                
                                  
                        resultat=((Yourhash*ratio)/networkfloat)*emissionfloat 
                                                    
                        NAME1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[2]/div/a/b'.format(i))
                        ACRONYME1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[2]/div/small'.format(i))
                        ALGO1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[3]/div'.format(i))
                        print(f"{i} - ", NAME1.text, ACRONYME1.text,ALGO1.text,PRICE1.text, EMISSION1.text,NETWORKHASH1.text,resultat)
                        
                        
                    else :
                                             
                        NAME1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[2]/div/a/b'.format(i))
                        ACRONYME1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[2]/div/small'.format(i))
                        ALGO1=browser.find_element(By.XPATH,'//*[@id="coins"]/tbody/tr[{}]/td[3]/div'.format(i))
                        print(f"{i} - ", NAME1.text, ACRONYME1.text,ALGO1.text,PRICE1.text, EMISSION1.text,NETWORKHASH1.text)

        except:
                continue

    
tout(50)
  
browser.quit()
