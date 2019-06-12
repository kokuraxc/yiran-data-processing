from pypinyin import lazy_pinyin
import os
import urllib
import csv

path = r'D:\Gallery\Chinese Temple'

filelist = os.listdir(path)

file1 = filelist[0]
print(file1)
print(''.join(lazy_pinyin(file1)))

temple_ids = {}

with open('folder name converter/chinese_temple_list.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    chinese_temple_list = list(csv_reader)

    for temple in chinese_temple_list:
        # # check duplicated temple names
        # if temple[4] in temple_ids:
        #     print(temple[4])

        temple_ids[temple[4]] = temple[0]

# print(temple_ids)
# print(len(temple_ids))

notFoundCount = 0
for file in filelist:
    # print(file)
    chunks = file.split('_')
    _chunks = []
    found = False
    

    for chunk in chunks:
        if chunk in temple_ids:
            # print('xxxx', chunk, temple_ids[chunk])
            _chunks.append(temple_ids[chunk])
            found = True
        else:
            _chunks.append(chunk)
        
    if not found:
        notFoundCount += 1
        print(notFoundCount, chunks)
        

    # print(_chunks)
    new_file_name = '_'.join(_chunks)
    # print(new_file_name)
