#!/usr/bin/env python   
import re  
import requests

def assign(service, arg):  
    if service != "discuz":  
        return  
    return True, arg  
  
def audit(arg):  
    url = arg
    try:
        req = requests.get(url + 'api.php?mod[]=Seay', timeout=5)

        if req.status_code == 200:
            m = re.search('<b>Warning</b>:[^\r\n]+or an integer in <b>([^<]+)api\.php</b> on line <b>(\d+)</b>', req.content)
            if m:
                security_info(m.group(1))
    except requests.Timeout:
        pass
  
  
from hackhttp import hackhttp
from func import *