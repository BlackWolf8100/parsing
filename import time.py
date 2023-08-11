import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    service = Service()

    options.add_argument(f'--proxy-server=socks5://Вписуємо свій proxy')
    driver = webdriver.Chrome(service=service, options=options)

    url = 'https://4.ident.me/'
    driver.get(url)
    time.sleep(5)
