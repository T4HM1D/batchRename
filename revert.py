from pathlib import Path
import os

fileList = []

videoPath = Path()
print(videoPath.resolve())

for files in videoPath.iterdir():
    if files.is_file() and files.suffix == '.mkv':
        fileList.append(files)

with open('name.txt', 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        oldName = fileList[i]
        newName = lines[i].strip()
        print(oldName)
        print(newName)
        fileList[i].rename(newName)
