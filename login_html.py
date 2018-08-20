import requests

if __name__ == '__main__':
    response = requests.get(
        "https://sso.douyin.com/login/?service=https%3A%2F%2Frenzheng.douyin.com%2F%3Fplatform%3DPC%26source%3Dwww.douyin.com")
    print(response.text)
