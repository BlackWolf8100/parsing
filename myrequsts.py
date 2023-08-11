import requests
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
response = requests.get(url, headers=headers, proxies=proxies)
proxies = { 
               
            "https" : socks_proxy
     
            }
response = requests.get(url, headers=headers, proxies=proxies)
print(response.status_code)
print(response.headers['content-type'])
print(response.encoding)
print(response.text)