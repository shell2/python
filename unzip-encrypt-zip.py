
#-*- coding: UTF-8 -*-
import codecs
import zipfile

# python 2.7

def progressbar(nowprogress, toyal):    #nowprogress现在的进度数   toyal#总数
    get_progress=int((nowprogress+1)*(50/toyal))   #显示多少>
    get_pro=int(50-get_progress)	#显示多少-
    percent=(nowprogress+1)*(100/toyal)
    print "\r"+"["+">"*get_progress+"-"*get_pro+']'+ "%.2f" % percent + "\%"

def setpass(zip, password):
    try:
        print 'password=%s.' % password.encode("ascii")
        zip.extractall(pwd=password.encode("ascii"))
        #zip.extractall(pwd=char(password))
        print 'return password=%s' % password.encode("ascii")
        return password
    except Exception as e:
        return

def main():
    with zipfile.ZipFile('spam.zip', 'w') as myzip:
      myzip.write('test2.1')
    with zipfile.ZipFile('spam.zip', 'r') as myzip:
      ret3=myzip.extractall('logs2')
      print 'ret3=', ret3

    zf1=zipfile.ZipFile(r"/Users/haili/logs/data.zip")
    ret1 = zf1.extractall()
    print 'ret1=', ret1

    #zf2=zipfile.ZipFile(r"/Users/haili/logs/test.zip")
    #ret2=zf2.extractall(pwd='123456')
    #print 'ret2=', ret2
    zf=zipfile.ZipFile(r"/Users/haili/logs/test.zip")
    zpassword=codecs.open(r'/Users/haili/logs/password.txt', encoding='utf-8', mode='r')
    zpw=zpassword.readlines()
    for i in zpw:
        progressbar(zpw.index(i), len(zpw))
        password=i.strip("\n")
	print 'ps=', password
        gess=setpass(zf, password)
	print 'gess=', gess
        if gess:
            print("\n"+"Correct ps: "+password+"....")
            exit(0)
        print "\n"+" Wrong ps: "+password 

if __name__=="__main__":
    main()
