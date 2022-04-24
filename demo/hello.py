from urllib import response
from webbrowser import get
import requests


if __name__ == '__main__':
    response = requests.request(method='get',url='https://www.baidu.com')
    print(response)
