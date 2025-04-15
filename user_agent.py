import requests

userAgent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.get('https://google.com', headers=userAgent)
print(response.status_code)
print(requests.get("https://httpbin.org/user-agent", headers=userAgent).json())