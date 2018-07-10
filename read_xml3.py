# -*- coding: UTF-8 -*-

with open('D:/workspace/textsum/test.txt', 'r',encoding='UTF-8') as f:
    while True:
        line = f.readline()     # 逐行读取
        if not line:
            break
        print(line)