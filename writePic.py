import base64

if __name__ == '__main__':
    strs = ""
    imgdata = base64.b64decode(strs)
    file = open('1.jpg', 'wb')
    file.write(imgdata)
    file.close()
