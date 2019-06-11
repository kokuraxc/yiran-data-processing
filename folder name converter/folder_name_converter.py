from pypinyin import lazy_pinyin
import os
import urllib

path = r'D:\Gallery\Chinese Temple'

filelist = os.listdir(path)

file1 = filelist[0]
print(file1)
print(''.join(lazy_pinyin(file1)))