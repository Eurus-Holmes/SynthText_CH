import os
import numpy as np
import itertools


# 获取目标文件夹的路径
filedir = r'./data/newsgroup'
# 获取文件夹中的文件名称列表
filenames = os.listdir(filedir)

# 遍历文件名
for filename in filenames:
    filepath = filedir + '/' + filename
    print(filepath)
    lines = open(filepath, 'r', encoding='utf-8').readlines()
    fileWrite = open(filepath, 'w', encoding='utf-8')
    for line in lines:
        ptr = line.strip().split('||||')
        recs = ptr[1].strip()
        print("recs: ", recs)
        fileWrite.write(recs)
        fileWrite.write('\n')
    fileWrite.close()