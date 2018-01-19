import os
import sys
from Libs.color import *

col = Color()

# 定义Exp文件夹各个功能的类
class ExpFunction():
    def __init__(self):
        self.path = os.getcwd() + '/Exp/'     # 跳到根目录

    # 列出Exp文件夹内的所有CMS名字
    def ExpFloderList(self):
        FolderList = filter(lambda x : (True,False)[x[-3:] == '.py'], os.listdir(self.path))
        return FolderList

    # 列出某个CMS的所有Exp脚本
    def ExpScriptList(self, cms):
        ScriptList = filter(lambda x : (True,False)[x[-3:] == 'pyc' or x[-5:] == '__.py' or x[:2] == '__'], os.listdir(self.path + cms))
        return ScriptList

    # 执行Exp
    def ExeExp(self, url, expName):
        md = __import__(expName)
        #print(md)
        try:
            if hasattr(md, 'Exploit'):
                exp = getattr(md, 'Exploit')()
                ret = exp.attack(url)
                # col.OutputGreen('[+Success] : {}'.format(ret)) if ret else col.OutputRed('[-Fail]')
                if ret:
                    col.OutputGreen('[+Success] : {}'.format(ret))
                    with open('{}/ret/ret.txt'.format(os.getcwd()), 'at') as f:
                        ret = '%-30s %s\n' % (url, expName)
                        f.writelines(ret)
                else:
                    col.OutputRed('[-Fail]')
        except Exception as e:
            print(e)

    # 给系统环境变量添加cms的路径
    def setSysPath(self, cms):
        sys.path.append(self.path + cms)


# expFunction = ExpFunction()
# expFunction.setSysPath('phpcms')
# expFunction.ExeExp('phpcms_down','http://demo.phpcms960.com')

