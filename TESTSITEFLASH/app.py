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

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
        #if request.method == 'POST':
        #data = request.form['Yourhash']
    data = [('Super Zero', 5.5463), ('Cortex', 4.1401), ('Firo', 3.8132), ('Neoxa', 1.4224), ('Conflux', 1.4079), ('Ergo', 1.169), ('Ravencoin', 1.1648), ('Metaverse', 0.9393), ('Kaspa', 0.9303), ('DigiByte', 0.7224), ('Epic Cash', 0.4473), ('Dagger', 0.2587), ('Quantum R L', 0.1119), ('Monero', 0.1019), ('Nervos Network', 0.0032), ('Aeternity', 0.0011), ('QuarkChain', 0.0005)]

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()


