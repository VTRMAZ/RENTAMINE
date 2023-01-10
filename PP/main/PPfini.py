import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
#from subprocess import CREATE_NO_WINDOW  # Windows only
def calculate_profitability(Yourhash):

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('window-size=1920x1080')

    chrome_service = Service('chromedriver')
    #chrome_service.creationflags = CREATE_NO_WINDOW
    browser = webdriver.Chrome(executable_path=r"C:\Users\VICTOR\pythonProject\venv\Scripts\chromedriver.exe", options=chrome_options, service=chrome_service)

    #browser = webdriver.Chrome(options=chrome_options, service=chrome_service)

    url = 'https://miningpoolstats.stream/'

    browser.get(url)
    sleep(5)  # Ce n'est pas la meilleure méthode...

    ratio_etc_ethash = 1
    ratio_Kapow = 0.451852
    ratio_Equihash1254 = 13 / 13500
    ratio_RandomX = 37 / 2700000
    ratio_Lyra2rew2 = 1.13
    ratio_Skein = 200 / 9
    ratio_Autolykos2 = 19 / 9
    ratio_eaglesong = 400 / 17
    ratio_kKeavyhash = 220 / 27
    ratio_octopus = 5 / 6
    ratio_Cuckoocycle = 1 / 6750000
    ratio_ProgPow = 4 / 9
    ratio_FiroPow = 7 / 18
    ratio_Beamhash = 23 / 45000000
    ratio_Equihash2109 = 7 / 1350000



    DICO = {}
    def transfo(i, Yourhash, ratio):
        NETWORKHASH1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[11]'.format(i))
        EMISSION1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[5]/div'.format(i))

        NETWORKHASH2 = str(NETWORKHASH1.text)
        EMISSION2 = str(EMISSION1.text)

        lennet = len(NETWORKHASH2)
        # lenprice=len(PRICE2)
        lenemi = len(EMISSION2)
        networkchiffre = NETWORKHASH2[0:lennet - 4]
        # pricechiffre=PRICE1[0:lenprice-1]
        emissionchiffre = EMISSION2[0:lenemi - 3]

        networkfloat = float(networkchiffre.replace(',', ''))
        # pricefloat=float(pricechiffre.replace(',',''))
        emissionfloat = float(emissionchiffre.replace(',', ''))

        for z, c in enumerate(NETWORKHASH2):
            if c == "T" or c == "P" or c == "G" or c == "M" or c == "K":
                for y, l in enumerate(NETWORKHASH2):
                    if l == "P":
                        networkfloat = networkfloat * (1000 ** 3)
                        break
                for y, l in enumerate(NETWORKHASH2):
                    if l == "T":
                        networkfloat = networkfloat * (1000 ** 2)
                        break
                for y, l in enumerate(NETWORKHASH2):
                    if l == "G":
                        networkfloat = networkfloat * (1000)
                        break
                for y, l in enumerate(NETWORKHASH2):
                    if l == "M":
                        networkfloat = networkfloat * 1
                        break
                for y, l in enumerate(NETWORKHASH2):
                    if l == "K":
                        networkfloat = networkfloat / 1000
                        break
                for y, l in enumerate(NETWORKHASH2):
                    if l != "T" and l != "P" and l != "G" and l != "M" and l != "K" and l != "0" and l != "1" and l != "2" and l != "3" and l != "4" and l != "5" and l != "6" and l != "7" and l != "8" and l != "9" and l != "/" and l != " " and l != "H" and l != "s" and l != "." and l != "o" and l != "l" and l != "S" and l != "i" and l != "B" and l != "p" and l != "h":
                        networkfloat = networkfloat / (1000 ** 2)
                        break
                break
            continue

        for o, m in enumerate(EMISSION2):
            if (m == "M" or m == "K"):
                for e, n in enumerate(EMISSION2):
                    if n == "M":
                        emissionfloat = emissionfloat * (1000 ** 2)

                        break
                for e, n in enumerate(EMISSION2):
                    if n == "K":
                        emissionfloat = emissionfloat * (1000)
                        break

        resultat = ((Yourhash * ratio) / networkfloat) * emissionfloat

        NAME1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[2]/div/a/b'.format(i))
        ACRONYME1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[2]/div/small'.format(i))
        ALGO1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[3]/div'.format(i))
        PRICE1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[6]/span'.format(i))
        print(f"{i} - ", NAME1.text, ACRONYME1.text, ALGO1.text, PRICE1.text, EMISSION1.text, NETWORKHASH1.text, resultat,
              "$")
        NAME1 = str(NAME1.text)
        ACRONYME1 = str(ACRONYME1.text)
        ALGO1 = str(ALGO1.text)
        PRICE1 = str(PRICE1.text)

        DICO[NAME1] = ACRONYME1  # https://www.delftstack.com/fr/howto/python/dictionary-with-multiple-values-in-python/
        DICO[NAME1] = round(resultat, 4)

        # liste.append(resultat)
        # liste.append(NAME1)


    def tout(nb_max):
        # chaine a completer
        chaine = ['Etchash', 'Ethash', 'KawPow', 'Equihash 125,4', 'RandomX', 'Lyra2REv2', 'Skein', 'Autolykos 2',
                  'Eaglesong', 'kHeavyHash', 'Octopus', 'Cuckoo Cycle', 'ProgPow', 'FiroPoW', 'BeamHash', 'Equihash 210,9']
        # cest good  faire teste xpath for all mais teste plus rapide sur 50
        browser.find_element(By.XPATH, '//*[@id="coins_length"]/label/select/option[3]').click()
        # ca marcche en balle pour changer de page

        #Yourhash = float(input("Rentre ton hash\n"))

        for i in range(1, nb_max):
            try:
                EMISSION1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[5]/div'.format(i))
                PRICE1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[6]/span'.format(i))
                NETWORKHASH1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[11]'.format(i))
                ALGO1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[3]/div'.format(i))
                for j in range(0, 15):
                    if (NETWORKHASH1.text and PRICE1.text and EMISSION1.text and ALGO1.text == chaine[
                        j]):  # faut aussi sup si c'est egale a zero car apres div par 0
                        if chaine[j] == chaine[0] or chaine[j] == chaine[1]:
                            transfo(i, Yourhash, ratio_etc_ethash)

                        elif chaine[j] == chaine[2]:
                            transfo(i, Yourhash, ratio_Kapow)

                        elif chaine[j] == chaine[3]:
                            NETWORKHASH1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[11]'.format(i))
                            EMISSION1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[5]/div'.format(i))

                            NETWORKHASH2 = str(NETWORKHASH1.text)
                            EMISSION2 = str(EMISSION1.text)

                            lennet = len(NETWORKHASH2)
                            # lenprice=len(PRICE2)
                            lenemi = len(EMISSION2)
                            networkchiffre = NETWORKHASH2[0:lennet - 6]
                            # pricechiffre=PRICE1[0:lenprice-1]
                            emissionchiffre = EMISSION2[0:lenemi - 3]

                            networkfloat = float(networkchiffre.replace(',', ''))
                            # pricefloat=float(pricechiffre.replace(',',''))
                            emissionfloat = float(emissionchiffre.replace(',', ''))

                            for z, c in enumerate(NETWORKHASH2):
                                if c == "T" or c == "P" or c == "G" or c == "M" or c == "K":
                                    for y, l in enumerate(NETWORKHASH2):
                                        if l == "P":
                                            networkfloat = networkfloat * (1000 ** 3)
                                            break
                                    for y, l in enumerate(NETWORKHASH2):
                                        if l == "T":
                                            networkfloat = networkfloat * (1000 ** 2)
                                            break
                                    for y, l in enumerate(NETWORKHASH2):
                                        if l == "G":
                                            networkfloat = networkfloat * (1000)
                                            break
                                    for y, l in enumerate(NETWORKHASH2):
                                        if l == "M":
                                            networkfloat = networkfloat * 1
                                            break
                                    for y, l in enumerate(NETWORKHASH2):
                                        if l == "K":
                                            networkfloat = networkfloat / 1000
                                            break
                                    for y, l in enumerate(NETWORKHASH2):
                                        if l != "T" and l != "P" and l != "G" and l != "M" and l != "K" and l != "0" and l != "1" and l != "2" and l != "3" and l != "4" and l != "5" and l != "6" and l != "7" and l != "8" and l != "9" and l != "/" and l != " " and l != "H" and l != "s" and l != "." and l != "o" and l != "l" and l != "S" and l != "i" and l != "B" and l != "p" and l != "h":
                                            networkfloat = networkfloat / (1000 ** 2)
                                            break
                                    break
                                continue

                            for o, m in enumerate(EMISSION2):
                                if (m == "M" or m == "K"):
                                    for e, n in enumerate(EMISSION2):
                                        if n == "M":
                                            emissionfloat = emissionfloat * (1000 ** 2)

                                            break
                                    for e, n in enumerate(EMISSION2):
                                        if n == "K":
                                            emissionfloat = emissionfloat * (1000)
                                            break
                                            # copier le sous prog et modife len-6
                        elif chaine[j] == chaine[4]:
                            transfo(i, Yourhash, ratio_RandomX)
                        elif chaine[j] == chaine[5]:
                            transfo(i, Yourhash, ratio_Lyra2rew2)
                        elif chaine[j] == chaine[6]:
                            transfo(i, Yourhash, ratio_Skein)
                        elif chaine[j] == chaine[7]:
                            transfo(i, Yourhash, ratio_Autolykos2)
                        elif chaine[j] == chaine[8]:
                            transfo(i, Yourhash, ratio_eaglesong)
                        elif chaine[j] == chaine[9]:
                            transfo(i, Yourhash, ratio_kKeavyhash)
                        elif chaine[j] == chaine[10]:
                            transfo(i, Yourhash, ratio_octopus)
                        elif chaine[j] == chaine[11]:
                            transfo(i, Yourhash, ratio_Cuckoocycle)
                        elif chaine[j] == chaine[12]:
                            transfo(i, Yourhash, ratio_ProgPow)
                        elif chaine[j] == chaine[13]:
                            transfo(i, Yourhash, ratio_FiroPow)
                        elif chaine[j] == chaine[14]:
                            transfo(i, Yourhash, ratio_Beamhash)
                        elif chaine[j] == chaine[15]:
                            transfo(i, Yourhash, ratio_Equihash2109)


            except:
                continue

        for z in range(1, 6):
            button = browser.find_element(By.XPATH, '//*[@id="coins_next"]/a')
            browser.execute_script("arguments[0].click();", button)
            for i in range(1, nb_max):
                try:
                    EMISSION1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[5]/div'.format(i))
                    PRICE1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[6]/span'.format(i))
                    NETWORKHASH1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[11]'.format(i))
                    ALGO1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[3]/div'.format(i))
                    for j in range(0, 15):
                        if (NETWORKHASH1.text and PRICE1.text and EMISSION1.text and ALGO1.text == chaine[
                            j]):  # faut aussi sup si c'est egale a zero car apres div par 0
                            if chaine[j] == chaine[0] or chaine[j] == chaine[1]:
                                transfo(i, Yourhash, ratio_etc_ethash)

                            elif chaine[j] == chaine[2]:
                                transfo(i, Yourhash, ratio_Kapow)

                            elif chaine[j] == chaine[3]:
                                transfo(i, Yourhash, ratio_Equihash1254)  # copier le sous prog et modife len-6
                            elif chaine[j] == chaine[4]:
                                transfo(i, Yourhash, ratio_RandomX)
                            elif chaine[j] == chaine[5]:
                                transfo(i, Yourhash, ratio_Lyra2rew2)
                            elif chaine[j] == chaine[6]:
                                transfo(i, Yourhash, ratio_Skein)
                            elif chaine[j] == chaine[7]:
                                transfo(i, Yourhash, ratio_Autolykos2)
                            elif chaine[j] == chaine[8]:
                                transfo(i, Yourhash, ratio_eaglesong)
                            elif chaine[j] == chaine[9]:
                                transfo(i, Yourhash, ratio_kKeavyhash)
                            elif chaine[j] == chaine[10]:
                                transfo(i, Yourhash, ratio_octopus)
                            elif chaine[j] == chaine[11]:
                                transfo(i, Yourhash, ratio_Cuckoocycle)
                            elif chaine[j] == chaine[12]:
                                transfo(i, Yourhash, ratio_ProgPow)
                            elif chaine[j] == chaine[13]:
                                transfo(i, Yourhash, ratio_FiroPow)
                            elif chaine[j] == chaine[14]:
                                transfo(i, Yourhash, ratio_Beamhash)
                            elif chaine[j] == chaine[15]:
                                transfo(i, Yourhash, ratio_Equihash2109)


                except:
                    continue


    tout(100)
    DICO = sorted(DICO.items(), key=lambda x: x[1])
    DICO = list(reversed(DICO))
    browser.quit()
    return DICO
calculate_profitability(270)