# File System 
# with open('./filesystem/poema.txt', mode = 'r', encoding = 'utf-8') as file:
#     for line in file.readlines():
#         print(line)

import os

with os.scandir('./filesystem') as entries:
    for entry in entries:
        if entry.is_dir():
            print("Pasta: ", entry.name)
        elif entry.is_file():
            print("Arquivo:", entry.name)