# import os
#
# file_path = './label_txt/'
#
# file_list = sorted(os.listdir(file_path))  # 文件名按字母排序
# file_nums = len(file_list)
# for i in range(file_nums):
#     if file_list[i] == ".DS_Store":
#         os.remove(file_path + file_list[i])
#     oldName = file_path + file_list[i]
#     newName = file_path + '{:06d}'.format(i + 5523) + '.txt'
#     print(oldName, '======>', newName)
#     os.rename(oldName, newName)
#
# print(file_nums)


import os

file_path = './org_img/'

file_list = sorted(os.listdir(file_path))  # 文件名按字母排序
file_nums = len(file_list)
for i in range(file_nums):
    if file_list[i] == ".DS_Store":
        os.remove(file_path + file_list[i])
    oldName = file_path + file_list[i]
    newName = file_path + '{:06d}'.format(i + 5523) + '.jpg'
    print(oldName, '======>', newName)
    os.rename(oldName, newName)

print(file_nums)