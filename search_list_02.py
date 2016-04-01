# -*- coding: utf-8 -*- 
#URLと該当箇所のリストを出力する場合

import xml.dom.minidom,os,sys,glob,re

li = []
fileList = glob.glob("*.xml")
print(fileList)

for xmlFile in fileList:
    if __name__ == "__main__":
        #print(xmlFile)
        dom = xml.dom.minidom.parse(xmlFile) #Your xml File
        displaystr = dom.getElementsByTagName("mm_displaystr")
        for i,url in enumerate(dom.getElementsByTagName("mm_file")): #Parameter name to get
            li.append([url.firstChild.data,displaystr[i].firstChild.data])

    list_uniq = sorted(li)
    print (list_uniq)

    fileName = '%s_02.txt' % xmlFile

    f = open(fileName, 'w')
    f.write("")

    for i in list_uniq: 
        f = open(fileName, 'a')
        f.writelines(i[0].replace('\\', '/').encode('utf-8'))
        f.writelines("\t")
        f.writelines(i[1].encode('utf-8'))
        f.writelines('\n')

    f.close