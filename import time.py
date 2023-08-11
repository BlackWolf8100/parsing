import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    service = Service()

    options.add_argument(f'--proxy-server=socks5://127.0.0.1:9050')
    driver = webdriver.Chrome(service=service, options=options)

    url = 'https://4.ident.me/'
    driver.get(url)
    time.sleep(5)