#import gunicorn

import app as app
from flask import Flask, render_template, request
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from flask import Flask, render_template, request


# from subprocess import CREATE_NO_WINDOW  # Windows only
app = Flask(__name__, static_folder='static')
#gunicorn app:app commande pour lancer



@app.route("/", methods=['GET','POST'])
def main():
        data = None
        if request.method=='POST':
            yourhash = int(request.form['Yourhash'])

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument('window-size=1920x1080')
            browser = webdriver.Chrome(options=chrome_options)
            url = 'https://miningpoolstats.stream/'
            browser.get(url)
            sleep(5)

            ratio_etc_ethash = 1
            ratio_Kapow = 0.451852
            ratio_Equihash1254 = 13 / 13500
            ratio_RandomX = 37 / 2700000
            ratio_Lyra2rew2 = 1.13
            ratio_Skein = 200 / 9
            ratio_Autolykos2 = 19 / 9
            ratio_eaglesong = 400 / 17
            ratio_kKeavyhash = 220 / 27
            ratio_octopus = 221 / 270
            ratio_Cuckoocycle = (7 / 45000000) / 3.9
            ratio_ProgPow = 0  # 4 / 9 doit avoir EIP
            ratio_FiroPow = (7 / 18) * (0.55)
            ratio_Beamhash = 23 / 45000000
            ratio_Equihash2109 = 7 / 135000
            ratio_NexaPow = 29 / 54
            ratio_SHA256DT = 790 / 27
            ratio_Blake3 = 490 / 27
            ratio_HeavyHash = ratio_kKeavyhash
            ratio_GhostRider = 0.0055/270
            ratio_Sha512256D=2200/270
            DICO = {}

            def transfo(i, yourhash, ratio):
                NETWORKHASH1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[11]'.format(i))
                EMISSION1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[5]/div'.format(i))
                PRICE1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[6]/span'.format(i))

                NETWORKHASH2 = str(NETWORKHASH1.text)
                PRICE1 = str(PRICE1.text)
                EMISSION2 = str(EMISSION1.text)

                lennet = len(NETWORKHASH2)
                lenemi = len(EMISSION2)
                lenprice = len(PRICE1)
                networkchiffre = NETWORKHASH2[0:lennet - 4]
                PRICE1 = PRICE1[0:lenprice - 1]
                emissionchiffre = EMISSION2[0:lenemi - 3]

                networkfloat = float(networkchiffre.replace(',', ''))
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

                resultat = round(((yourhash * ratio) / networkfloat) * emissionfloat,3)

                NAME1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[2]/div/a/b'.format(i))
                ACRONYME1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[2]/div/small'.format(i))
                ALGO1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[3]/div'.format(i))
                print(f"{i} - ", NAME1.text, ACRONYME1.text, ALGO1.text, PRICE1, EMISSION1.text, NETWORKHASH1.text,
                      resultat, "$")
                NAME1 = str(NAME1.text)
                ACRONYME1 = str(ACRONYME1.text)
                ALGO1 = str(ALGO1.text)
                PRICE1 = float(PRICE1)
                REWARDS1 = round(float(resultat / PRICE1),3)

                DICO[NAME1] = {'acronyme': ACRONYME1, 'algo': ALGO1, 'resultat': resultat, 'rewards': REWARDS1}

            def tout(nb_max, yourhash):
                # chaine a completer
                chaine = ['Etchash', 'Ethash', 'KawPow', 'Equihash 125,4', 'RandomX', 'Lyra2REv2', 'Skein',
                          'Autolykos 2',
                          'Eaglesong', 'kHeavyHash', 'Octopus', 'Cuckoo Cycle', 'ProgPow', 'FiroPoW', 'BeamHash',
                          'Equihash 210,9',
                          'NexaPow', 'SHA256DT', 'Blake3', 'HeavyHash', 'GhostRider','Sha512256D']
                browser.find_element(By.XPATH, '//*[@id="coins_length"]/label/select/option[3]').click()
                browser.find_element(By.XPATH, '//*[@id="coins"]/thead/tr/th[5]').click()

                # yourhash = float(input("Rentre ton hash\n"))

                for i in range(1, nb_max):
                    ALGO1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[3]/div'.format(i))
                    if (ALGO1 == element for element in chaine):
                        try:
                            for j in range(0, 22):
                                if (ALGO1.text == chaine[
                                    j]):  # faut aussi sup si c'est egale a zero car apres div par 0
                                    if chaine[j] == chaine[0] or chaine[j] == chaine[1]:
                                        transfo(i, yourhash, ratio_etc_ethash)

                                    elif chaine[j] == chaine[2]:
                                        transfo(i, yourhash, ratio_Kapow)

                                    elif chaine[j] == chaine[3]:
                                        NETWORKHASH1 = browser.find_element(By.XPATH,
                                                                            '//*[@id="coins"]/tbody/tr[{}]/td[11]'.format(
                                                                                i))
                                        EMISSION1 = browser.find_element(By.XPATH,
                                                                         '//*[@id="coins"]/tbody/tr[{}]/td[5]/div'.format(
                                                                             i))

                                        NETWORKHASH2 = str(NETWORKHASH1.text)
                                        EMISSION2 = str(EMISSION1.text)

                                        lennet = len(NETWORKHASH2)
                                        lenemi = len(EMISSION2)
                                        networkchiffre = NETWORKHASH2[0:lennet - 6]
                                        emissionchiffre = EMISSION2[0:lenemi - 3]

                                        networkfloat = float(networkchiffre.replace(',', ''))
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
                                    elif chaine[j] == chaine[4]:
                                        transfo(i, yourhash, ratio_RandomX)
                                    elif chaine[j] == chaine[5]:
                                        transfo(i, yourhash, ratio_Lyra2rew2)
                                    elif chaine[j] == chaine[6]:
                                        transfo(i, yourhash, ratio_Skein)
                                    elif chaine[j] == chaine[7]:
                                        transfo(i, yourhash, ratio_Autolykos2)
                                    elif chaine[j] == chaine[8]:
                                        transfo(i, yourhash, ratio_eaglesong)
                                    elif chaine[j] == chaine[9]:
                                        transfo(i, yourhash, ratio_kKeavyhash)
                                    elif chaine[j] == chaine[10]:
                                        transfo(i, yourhash, ratio_octopus)
                                    elif chaine[j] == chaine[11]:
                                        transfo(i, yourhash, ratio_Cuckoocycle)
                                    elif chaine[j] == chaine[12]:
                                        transfo(i, yourhash, ratio_ProgPow)
                                    elif chaine[j] == chaine[13]:
                                        transfo(i, yourhash, ratio_FiroPow)
                                    elif chaine[j] == chaine[14]:
                                        transfo(i, yourhash, ratio_Beamhash)
                                    elif chaine[j] == chaine[15]:
                                        transfo(i, yourhash, ratio_Equihash2109)
                                    elif chaine[j] == chaine[16]:
                                        transfo(i, yourhash, ratio_NexaPow)
                                    elif chaine[j] == chaine[17]:
                                        transfo(i, yourhash, ratio_SHA256DT)
                                    elif chaine[j] == chaine[18]:
                                        transfo(i, yourhash, ratio_Blake3)
                                    elif chaine[j] == chaine[19]:
                                        transfo(i, yourhash, ratio_HeavyHash)
                                    elif chaine[j] == chaine[20]:
                                        transfo(i, yourhash, ratio_GhostRider)
                                    elif chaine[j] == chaine[21]:
                                        transfo(i, yourhash, ratio_Sha512256D)

                        except:
                            continue

            tout(100, yourhash)

            DICO = sorted(DICO.items(), key=lambda x: x[1]['resultat'], reverse=True)
            browser.quit()
            data = DICO

        return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)



'''


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        data = request.form['Yourhash']
        data = int(data)*2
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()

'''