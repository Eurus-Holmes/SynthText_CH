import datetime
import os
import h5py
import numpy as np

# f = h5py.File('path/filename.h5','r') #打开h5文件
f = h5py.File('results/SynthText_800000.h5','r')
f.keys() #可以查看所有的主键
print([key for key in f.keys()])
# print(f['depth'])
# print(f['image'])
# print(f['seg'])
