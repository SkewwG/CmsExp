# coding:utf-8
# http://120.92.155.53、http://112.33.15.108、http://112.33.15.108
import requests

class Exploit:

    payload_path = '/wp-json/wp/v2/posts'
    introduction = 'You can see the Link `http://blog.csdn.net/anprou/article/details/54926612` to use the Exploit'

    def attack(self, url):
        response = requests.get(url+self.payload_path, timeout=10)

        try:
            m = response.json()
        except:
            m = False

        if m:
            return "{} has WordPress REST API SQL Injection.\n{}".format(url, self.introduction)


# Exploit().attack('http://www.dacai.me/')