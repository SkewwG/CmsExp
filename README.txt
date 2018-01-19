# 对-u指定的url扫描-c指定的cms里的所有exp
python3 scan.py -u http://gaokao.hnjy.com.cn -c phpcms

# 对-u指定的url扫描所有cms里的所有exp
python3 scan.py -u http://gaokao.hnjy.com.cn -a all

# 对-d指定的txt文件内的所有url扫描-c指定的cms里的所有exp
python3 scan.py -d C:\Users\Asus\Desktop\py\py3\project\infoGather\ret\wordpress\wp.txt -c wordpress

# 对-d指定的txt文件内的所有url扫描-c指定的cms里的所有exp,并设置线程数为10
python3 scan.py -d C:\Users\Asus\Desktop\py\py3\project\infoGather\ret\wordpress\wp.txt -c wordpress -t 10

# 存在漏洞url都会保存在/ret/ret.txt文件内。格式为：url+exp名称
http://120.92.155.53           wordpress_rest_sql_injection