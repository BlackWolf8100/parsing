import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

driver = webdriver.Firefox()

url = 'https://4.ident.me/'
driver.get(url)
time.sleep(5)
driver.close()

url = 'https://4.ident.me/'
headers = {
    'User-Agent' : 'Вписуємо свій User-Agent'
}
socks_proxy = 'socks5://вписуємо свій proxy'

proxies = { 
            "https" : socks_proxy
            }
chrome_options = Options()
chrome_options.add_argument('--proxy-server=вписуємо свій proxy')
driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
# driver = webdriver.Chrome()
driver.get("https://www.example.com")
time.sleep(5)
