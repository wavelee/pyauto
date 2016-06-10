#!/usr/bin/env python3
#-*- coding:UTF-8 -*- 

# to test in windows cmd: u can use : python simple3.py nginx.conf.v1 nginx.conf.v2 > diff.html

import difflib
import sys


def printHelpMsg():
    ''''''
    print("Usage: simple3.py filename1 filename2")

def readfile(filename):
    '''读取文件'''
    with open(filename,'rt') as fileHandle:
        return fileHandle.read().splitlines()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        printHelpMsg()
        print(len(sys.argv))
        sys.exit()
    else:
        try:
            text1_lines = readfile(sys.argv[1]) 
            text2_lines = readfile(sys.argv[2])   
        except Exception as e:
                print("Error:",str(e.args))
                printHelpMsg()
                sys.exit()  
                
        d = difflib.HtmlDiff()
        diff = d.make_file(text1_lines,text2_lines)
        print(diff)