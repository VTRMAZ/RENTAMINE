import requests
import json
import pyfiglet
from colorama import init, Fore, Style

url = 'https://whattomine.com/coins.json?eth=true&factor%5Beth_hr%5D=260.0&factor%5Beth_p%5D=690.0&e4g=true&factor%5Be4g_hr%5D=260.3&factor%5Be4g_p%5D=690.0&zh=true&factor%5Bzh_hr%5D=390.0&factor%5Bzh_p%5D=760.0&cnh=true&factor%5Bcnh_hr%5D=1380.0&factor%5Bcnh_p%5D=190.0&cng=true&factor%5Bcng_hr%5D=11650.0&factor%5Bcng_p%5D=810.0&s5r=true&factor%5Bs5r_hr%5D=2.49&factor%5Bs5r_p%5D=390.0&cx=true&factor%5Bcx_hr%5D=0.0&factor%5Bcx_p%5D=0.0&eqa=true&factor%5Beqa_hr%5D=1110.0&factor%5Beqa_p%5D=600.0&cc=true&factor%5Bcc_hr%5D=39.8&factor%5Bcc_p%5D=810.0&cr29=true&factor%5Bcr29_hr%5D=30.4&factor%5Bcr29_p%5D=600.0&hh=true&factor%5Bhh_hr%5D=2140.0&factor%5Bhh_p%5D=550.0&ct32=true&factor%5Bct32_hr%5D=2.12&factor%5Bct32_p%5D=780.0&eqb=true&factor%5Beqb_hr%5D=134.1&factor%5Beqb_p%5D=780.0&factor%5Bb3_hr%5D=4.9&factor%5Bb3_p%5D=620.0&ns=true&factor%5Bns_hr%5D=1300.0&factor%5Bns_p%5D=130.0&al=true&factor%5Bal_hr%5D=606.5&factor%5Bal_p%5D=630.0&ops=true&factor%5Bops_hr%5D=221.4&factor%5Bops_p%5D=810.0&eqz=true&factor%5Beqz_hr%5D=51.1&factor%5Beqz_p%5D=220.0&zlh=true&factor%5Bzlh_hr%5D=253.5&factor%5Bzlh_p%5D=720.0&kpw=true&factor%5Bkpw_hr%5D=122.2&factor%5Bkpw_p%5D=850.0&ppw=true&factor%5Bppw_hr%5D=115.8&factor%5Bppw_p%5D=820.0&factor%5Bnx_hr%5D=180.0&factor%5Bnx_p%5D=520.0&fpw=true&factor%5Bfpw_hr%5D=106.8&factor%5Bfpw_p%5D=740.0&vh=true&factor%5Bvh_hr%5D=4.42&factor%5Bvh_p%5D=630.0&factor%5Bcost%5D=0.1&factor%5Bcost_currency%5D=USD&sort=MarketCap&volume=0&revenue=current&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main'
response = requests.get(url)

def pool_luck():
    pass


def ELEC():
    price_elec=float(input("Entrez le prix de l'elec en $/KWh: "))
    consommation = float(input("Entrez votre consomation en W: "))/1000
    price_consommation=price_elec*consommation*24
    return price_consommation;

def ERGO(yourhash,bitcoin_price,price_consommation):
    ergo = data['coins']['Ergo']

    block_reward = float(ergo['block_reward'])
    block_time = float(ergo['block_time'])
    price = float(ergo['exchange_rate'])
    nethash = float(ergo["nethash"])/(1000*1000)#en méga hash


    price_dollar=bitcoin_price*price

    total_block = (60 / block_time) * 60 * 24 * block_reward

    resultat = (((yourhash) / nethash) * total_block)*price_dollar

    print('Price ERGO:', price_dollar)
    print("REVENUE",resultat)
    profit=resultat-price_consommation
    if profit >= 0:
        print("\033[32mProfit: ", profit, "\033[0m")
    else:
        print("\033[31mProfit: ", profit, "\033[0m")

def ETHW(yourhash,bitcoin_price,price_consommation):
    EthPoW = data['coins']['EthereumPoW']

    block_reward = float(EthPoW['block_reward'])
    block_time = float(EthPoW['block_time'])
    price = float(EthPoW['exchange_rate'])
    nethash = float(EthPoW["nethash"])/(1000*1000)#en méga hash


    price_dollar=bitcoin_price*price

    total_block = (60 / block_time) * 60 * 24 * block_reward

    resultat = (((yourhash) / nethash) * total_block)*price_dollar

    print('Price ETHW:', price_dollar)
    print("REVENUE",resultat)
    profit=resultat-price_consommation
    if profit >= 0:
        print("\033[32mProfit: ", profit, "\033[0m")
    else:
        print("\033[31mProfit: ", profit, "\033[0m")
def ETC(yourhash,bitcoin_price,price_consommation):
    etc = data['coins']['EthereumClassic']

    block_reward = float(etc['block_reward'])
    block_time = float(etc['block_time'])
    price = float(etc['exchange_rate'])
    nethash = float(etc["nethash"])/(1000*1000)#en méga hash


    price_dollar=bitcoin_price*price

    total_block = (60 / block_time) * 60 * 24 * block_reward

    resultat = (((yourhash) / nethash) * total_block)*price_dollar

    print('Price ETC:', price_dollar)
    print("REVENUE",resultat)
    profit=resultat-price_consommation
    if profit >= 0:
        print("\033[32mProfit: ", profit, "\033[0m")
    else:
        print("\033[31mProfit: ", profit, "\033[0m")


if response.status_code == 200:
    init()

    url_api = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }

    retour = requests.get(url_api, params=params)

    if retour.status_code == 200:
        data = retour.json()
        bitcoin_price = data['bitcoin']['usd']

    else:
        print("erroer requests")

    #bitcoin_price = 24000
    ascii_art = pyfiglet.Figlet(font='standard')
    ascii_text = ascii_art.renderText('RENTAMINE')
    ascii_text = Fore.BLUE + ascii_text + Style.RESET_ALL
    print(ascii_text)


    data = json.loads(response.content.decode('utf-8'))

    ascii_art = pyfiglet.Figlet(font='small')
    ascii_text = ascii_art.renderText('ERG')
    ascii_text = Fore.BLUE + ascii_text + Style.RESET_ALL
    print(ascii_text)


    price_consommation=ELEC()
    yourhash = float(input("Entrez votre puissance en MH/s pour ergo : "))
    ERGO(yourhash,bitcoin_price,price_consommation)



    ascii_art = pyfiglet.Figlet(font='small')
    ascii_text = ascii_art.renderText('ETHW')
    ascii_text = Fore.BLUE + ascii_text + Style.RESET_ALL
    print(ascii_text)

    price_consommation = ELEC()
    yourhash = float(input("Entrez votre puissance en MH/s pour Ethash : "))
    ETHW(yourhash, bitcoin_price, price_consommation)



    ascii_art = pyfiglet.Figlet(font='small')
    ascii_text = ascii_art.renderText('ETC')
    ascii_text = Fore.BLUE + ascii_text + Style.RESET_ALL
    print(ascii_text)

    price_consommation = ELEC()
    yourhash = float(input("Entrez votre puissance en MH/s pour Ethash : "))
    ETC(yourhash, bitcoin_price, price_consommation)

else:
    print("error", response.status_code)


