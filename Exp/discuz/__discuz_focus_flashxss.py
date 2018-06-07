#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: discuz X3 focus.swf flashxss漏洞
referer: unknown
author: Lucifer
description: 文件中focus.swf存在flashxss。
'''
import sys
import urllib
import hashlib
import requests
import warnings
from termcolor import cprint

class Exploit:

    def attack(self, url):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        flash_md5 = "c16a7c6143f098472e52dd13de85527f"
        payload = "/static/image/common/focus.swf"
        vulnurl = url + payload
        try:
            req = urllib.request.urlopen(vulnurl)
            data = req.read()
            md5_value = hashlib.md5(data).hexdigest()
            if md5_value in flash_md5:
                cprint("[+]存在discuz X3 focus.swf flashxss漏洞...(高危)\tpayload: "+vulnurl, "red")
                return '存在discuz X3 focus.swf flashxss漏洞'

        except:
            cprint("[-] "+__file__+"====>连接超时", "cyan")
