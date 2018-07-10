import jieba

f = open("D:/workspace/textsum/traindata/content_news.sohunews.210806.txt",encoding='UTF-8')
line = f.readline()
file_write_obj = open("D:/workspace/textsum/traindata/content_news.sohunews.210806_segment.txt", 'w',encoding='UTF-8')
while line:
    print(line)
    seg_list = jieba.cut(line)
    line_seg = " ".join(seg_list)
    print(line_seg)
    file_write_obj.writelines(line_seg)
    #file_write_obj.write('\n')
    line = f.readline()
f.close()
file_write_obj.close()

"""
file_write_obj = open("D:/workspace/textsum/traindata/title_segment.txt", 'w',encoding='UTF-8')
for var in mylist:
    file_write_obj.writelines(var)
    file_write_obj.write('\n')
file_write_obj.close()

"""