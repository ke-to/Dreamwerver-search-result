# -*- coding: utf-8 -*- 

import xml.dom.minidom
import os,glob
import sys

li = []
if __name__ == "__main__":
    dom = xml.dom.minidom.parse("ResultsReport.xml") #Your xml File
    for url in dom.getElementsByTagName("mm_file"): #Parameter name to get
        print (url.firstChild.data)
        li.append(url.firstChild.data)

list_uniq2 = list(set(li))
list_uniq = sorted(list_uniq2)
print (list_uniq)

fileName = 'test.txt'

f = open(fileName, 'w')
f.write("")

for i in list_uniq: 
    f = open(fileName, 'a')
    f.writelines(i)
    f.writelines('\n')

f.close