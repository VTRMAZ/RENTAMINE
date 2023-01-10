#Librairie pour scraping
import requests
from bs4 import BeautifulSoup

220
#Naviguer sur les 28 pages de 25 crypto
#trier les algos, selction pour gpu prendre adresse HMTL si bon algo entrer dans page
#trouver un racourcir pour les cryptos quipeuvent etre miner sous plusieurs algo
#Dans la page prendre 3 infos : hashrate network, price, block par jour
#Demander les hash qui dvt sous ethash
#Creer un ratio sur chaque algo 

#1 Calcule pour les 3 infos + dm à lutilisateur modifier les variables pour prendre celle du site HTML

#mettre en structure
"""
HashrateNetwork=0;
Price=0;
BlockTotal=0;
YourHashrate=0;
Total=0;



YourHashrate=input("Entrer votre hashrate\n");
print("Votre hashrate",YourHashrate)

def calcul():
    #global Total,HashrateNetwork,Price,BlockTotal,YourHashrate

    Total= (int(YourHashrate)/HashrateNetwork)*BlockTotal*Price
    return Total


print("Total des gains:", calcul())
"""
#Connection a la page 

url = 'https://miningpoolstats.stream/'

response =requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.text, "html.parser") 
    ThePrice= soup.find('div',{"class":"table"})
    print(ThePrice)
   #https://www.youtube.com/watch?v=iWFHCQtdQ78
'''
Chemin d'acces par le termianl (je crois que y a une diff avec inspecter sur google):div
Si je tape td je ne vois que une fois show1050, pour usd 
si je tape tr je trouve show1050 mais que pour USD
apres verifications les dossier nes sont pas visible regarder commetn regler ca 
teste par https://miningpoolstats.stream/sitemap.xml pour accer a chaque page 



CSS de tout les prix dune page td.show1050 > span

'''