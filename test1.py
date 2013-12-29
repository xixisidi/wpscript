#-*- coding:utf-8 -*-

import sys
import os

def main():
    sys.stdout.write("开始程序\n")
    i=10
    j=u'老梅花'
    print str(i)+j
    dir= os.listdir('/opt')
    print type(dir)
    for s in dir:
        print s+'\r'
    
if __name__ == '__main__':
    main()

