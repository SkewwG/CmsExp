#-*- coding:utf-8 -*-
from optparse import OptionParser
from Libs.func import *
import threading
from queue import Queue

event = threading.Event()
event.set()
q_urls = Queue(-1)

col = Color()
init = ExpFunction()

# 多线程类
class multi_thread(threading.Thread):
    def __init__(self, q_urls, cms, num):
        threading.Thread.__init__(self)
        self.q_urls = q_urls
        self.cms = cms
        self.t = num

    def run(self):
        while event.is_set():
            if self.q_urls.empty():
                break
            else:
                url = self.q_urls.get()
                scan(url, self.cms, self.t)

# 多线程方法
def scan_thread(q_urls, cms, t):
    threads = []
    thread_num = t
    for num in range(1, thread_num + 1):
        t = multi_thread(q_urls, cms, num)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# 对单个url扫描cms的所有exp
def scan(url, cms, t=1):
    init.setSysPath(cms)                        # 将cms所在的目录添加到系统变量里
    ExpScripts = init.ExpScriptList(cms)        # 获取cms下的所有exp脚本
    print('[*t{}] Scan url : {}'.format(t, url))
    for exp in ExpScripts:
        output = '[*t{}] Load Exp {}'.format(t, exp)
        col.OutputBlue(output)
        init.ExeExp(url, exp[:-3])                   # 执行exp


# 打开域名txt文件，获取所有域名
def get_urls(urlsFile):
    with open(urlsFile, 'rt') as f:
        for each in f:
            q_urls.put(each[:-1])
    return q_urls

def cmdParser(url, urlsFile, cms, all, t):
    ExpFolders = init.ExpFloderList()
    # 调用指定cmsexp
    if not all:
        if not urlsFile:            # 对单个目标进行扫描
            scan(url, cms)
        else:                       # 对txt文件内的所有目标扫描
            q_urls = get_urls(urlsFile)
            scan_thread(q_urls, cms, t)             # 调用了多线程

    # 调用所有cmsexp
    elif all == 'all':
        if not urlsFile:
            for cms in ExpFolders:
                scan(url, cms)
        else:
            q_urls = get_urls(urlsFile)
            scan_thread(q_urls, cms, t)


if __name__ == '__main__':
    usage = r'usage : &prog python3 scan.py -u http://gaokao.hnjy.com.cn -c phpcms' \
            r'python3 scan.py -u http://gaokao.hnjy.com.cn -c phpcms -a all' \
            r'python3 scan.py -d C:\Users\Asus\Desktop\py\py3\project\infoGather\ret\wordpress\wp.txt -c wordpress' \
            r'python3 scan.py -d C:\Users\Asus\Desktop\py\py3\project\infoGather\ret\wordpress\wp.txt -c wordpress -t 10'

    parse = OptionParser(usage=usage)
    parse.add_option('-u', '--url', dest='url', type='string', help='attack url')
    parse.add_option('-d', '--urls', dest='urlsFile', type='string', help='input urls file path')
    parse.add_option('-c', '--cms', dest='cms', type='string', help='execute CMS Exp')
    parse.add_option('-a', '--all', dest='all', type='string', help='execute all CMS Exp')
    parse.add_option('-t', '--threads', dest='threads', type='int', help='the num of scan threads')
    options, args = parse.parse_args()
    cmdParser(options.url, options.urlsFile, options.cms, options.all, options.threads)
    print('scan end!')