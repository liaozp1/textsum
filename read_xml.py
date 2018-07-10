#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse('D:/workspace/textsum/SogouCS.mini')
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element : %s" % collection.getAttribute("shelf"))


# 在集合中获取所有电影
docs = collection.getElementsByTagName("doc")

# 打印每部电影的详细信息
for doc in docs:
    print("*****doc*****")

    #if movie.hasAttribute("title"):
       # print("Title: %s" % movie.getAttribute("title"))

    contenttitle= doc.getElementsByTagName('contenttitle')[0]
    print("contenttitle: %s" % type.childNodes[0].data)

    description = doc.getElementsByTagName('content')[0]
    print("Description: %s" % description.childNodes[0].data)
