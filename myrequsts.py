import requests
# url = 'https://Вписуємо свою силку'
url = 'https://4.ident.me/'
headers = {
    'User-Agent' : 'Вписуємо свій User-Agent'
}
socks_proxy = 'socks5://Вписуємо свій proxy'

proxies = { 
            "https" : socks_proxy
            }
response = requests.get(url, headers=headers, proxies=proxies)
proxies = { 
               
            "https" : socks_proxy
     
            }
response = requests.get(url, headers=headers, proxies=proxies)
print(response.status_code)
print(response.headers['content-type'])
print(response.encoding)
print(response.text)
