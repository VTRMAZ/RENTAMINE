from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from subprocess import CREATE_NO_WINDOW #Windows only

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument('window-size=1920x1080')
browser = webdriver.Chrome(options=chrome_options)
url = 'https://miningpoolstats.stream/'
browser.get(url)
sleep(5)
for i in range (1,3):
    EMISSION1 = browser.find_element(By.XPATH, '//*[@id="coins"]/tbody/tr[{}]/td[5]/div'.format(i))
    print(EMISSION1.text)
browser.quit()