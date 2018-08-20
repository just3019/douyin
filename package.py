# 1.获取验证码。
# 2.获取手机号。
# 3.获取短信验证码。
# 4.拉取易码验证码
import base64
import json
import threading
from tkinter import *

import requests

import yima
from chaojiying import Chaojiying_Client

lock = threading.Lock()
TOKEN = "00499849cbf687835af75182698438eb3c2ccdf4"
ITEMID = "7732"
EXCLUDENO = "170.171.172.173.174.175.176.177.178.179"
PROVINCE = "330000"
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


def log(s):
    print(s)
    textView.insert(END, '%s\n' % s)
    textView.update()
    textView.see(END)


def get_vcode():
    # 进入抖音登录页，拉取验证码图片base64码，下载到本地，去超级鹰获取验证码。
    print("开始拉取登录页验证码")
    response = requests.get('https://sso.douyin.com/refresh_captcha/', headers=headers, cookies=cookies)
    print(response.text)
    result = json.loads(response.text)
    str = result["captcha"]
    imgdata = base64.b64decode(str)
    file = open('vcode.jpg', 'wb')
    file.write(imgdata)
    file.close()
    chaojiying = Chaojiying_Client('demon3019', '12345678', '896963')
    im = open('vcode.jpg', 'rb').read()
    vcode = chaojiying.PostPic(im, 1004)
    print(vcode["pic_str"])
    return vcode["pic_str"]


def send_vcode_sms(phone, vcode):
    params = (
        ('mobile', phone),
        ('captcha', vcode),
        ('type', '24'),
        ('aid', '0'),
    )
    response = requests.get('https://sso.douyin.com/send_activation_code/', headers=headers, params=params,
                            cookies=cookies)
    print(response.text)


def get_phone_code():
    phone = yima.ym_phone(TOKEN, ITEMID, EXCLUDENO, PROVINCE, "", "")
    vcode = get_vcode()
    send_vcode_sms(phone, vcode)
    sms_vcode = yima.ym_sms(TOKEN, ITEMID, phone, 100)
    log(phone + "  " + sms_vcode)


def ui():
    root = Tk()  # 创建窗口对象的背景色
    # 创建两个列表
    root.title('获取抖音手机号和验证码')
    root.geometry('600x600')
    global s1
    s1 = Scrollbar(root)
    s1.pack(side=RIGHT, fill=Y)
    global textView
    textView = Text(root, width=400, height=30, yscrollcommand=s1.set)
    label3 = Label(root, text='日志输出：')
    label3.pack()
    textView.pack(expand=YES, fill=X)
    s1.config(command=textView.yview)
    btn = Button(root, text='开始', command=submit)
    btn.pack(expand=YES, fill=X)
    root.mainloop()  # 进入消息循环


def submit():
    print("获取")
    th = threading.Thread(target=deal)
    th.setDaemon(True)  # 守护线程
    th.start()


def deal():
    lock.acquire()
    count = 0
    while count < 1:
        try:
            log("开始进行获取")
            get_phone_code()
            count += 1
        except RuntimeError as e:
            print(e)
    lock.release()


if __name__ == '__main__':
    print("开始")
    ui()
