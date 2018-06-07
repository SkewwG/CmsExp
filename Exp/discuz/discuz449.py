#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'darkkid'
# Name:Discuz! X3 tools
import requests

def assign(service, arg):
    if service == "discuz":
        return True, arg


def audit(arg):
    payload = 'source/plugin/tools/tools.php'
    verify_url = arg + payload
    try:
        req = requests.get(verify_url, timeout=5)
        if req.status_code == 200 and "Discuz" in req.content:
            security_warning(verify_url + ' Discuz! X3 tools')
    except requests.Timeout:
        pass

# if __name__ == '__main__':
#     from dummy import *
#     audit(assign('discuz', 'http://www.example.com/')[1])
from hackhttp import hackhttp
from func import *