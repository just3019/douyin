import requests

cookies = {
    '_ga': 'GA1.2.1505543331.1534763857',
    '_gid': 'GA1.2.1133988330.1534763857',
    'ccid': '0a377fe45460976ca1593b956de7dfc0',
}

headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'Referer': 'https://sso.douyin.com/login/?service=https%3A%2F%2Frenzheng.douyin.com%2F%3Fplatform%3DPC%26source%3Dwww.douyin.com',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

params = (
    ('mobile', '13675822154'),
    ('captcha', 'amxr'),
    ('type', '24'),
    ('aid', '0'),
)

response = requests.get('https://sso.douyin.com/send_activation_code/', headers=headers, params=params, cookies=cookies)
print(response.text)
