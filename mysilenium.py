import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


driver = webdriver.Firefox()
# url = 'https://ikscs.in.ua/'
url = 'https://4.ident.me/'
driver.get(url)
time.sleep(5)
driver.close()
# url = 'https://ikscs.in.ua/'
url = 'https://4.ident.me/'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'
}
# https_proxy = 'https://138.199.48.1:8443'
socks_proxy = 'socks5://127.0.0.1:9150'

proxies = { 
            "https" : socks_proxy
            }
chrome_options = Options()
chrome_options.add_argument('--proxy-server=127.0.0.1:9150')
driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
# driver = webdriver.Chrome()
driver.get("https://www.example.com")
time.sleep(5)