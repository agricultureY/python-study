#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ycn'

from xml.parsers.expat import ParserCreate

# 操作XML有两种方法：DOM和SAX。
# DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
# 正常情况下，优先考虑SAX，因为DOM实在太占内存。

# 在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。
# 举个例子，当SAX解析器读到一个节点（<a href="/">python</a>）时：
# 会产生3个事件：
#   1、start_element事件，在读取<a href="/">时；
#   2、char_data事件，在读取python时；
#   3、end_element事件，在读取</a>时。

# 定义xml数据
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''


# 定义xml解析类
class XmlSaxHandler:
    def startElement(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def endElement(self, name):
        print('sax:end_element: %s' % name)

    def charData(self, text):
        print('sax:char_data: %s' % text)


handler = XmlSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.startElement
parser.EndElementHandler = handler.endElement
parser.CharacterDataHandler = handler.charData
parser.Parse(xml)
print('==============================================')

# 最简单也是最有效的生成XML的方法是拼接字符串
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append('some & data')
L.append(r'</root>')
print(''.join(L))
