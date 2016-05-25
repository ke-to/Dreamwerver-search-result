# -*- coding: utf-8 -*- 
#URLの重複なしリストを出力する場合

import xml.dom.minidom,os,sys,glob,re

fileList = glob.glob("*.xml")
print(fileList)

for xmlFile in fileList:
    li = []
    if __name__ == "__main__":
        print(xmlFile)
        dom = xml.dom.minidom.parse(xmlFile) #Your xml File
        for url in dom.getElementsByTagName("mm_file"): #Parameter name to get
            print (url.firstChild.data)
            li.append(url.firstChild.data)

    list_uniq2 = list(set(li))
    list_uniq = sorted(list_uniq2)
    print (list_uniq)

    fileName = '%s.txt' % xmlFile

    f = open(fileName, 'w')
    f.write("")

    for i in list_uniq: 
        f = open(fileName, 'a')
        f.writelines(i.replace('\\', '/').encode('utf-8'))
        f.writelines('\n')

    f.close