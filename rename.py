from pathlib import Path
import os

fileList = []

videoPath = Path()
print(videoPath.resolve())

for files in videoPath.iterdir():
    # and (template.split('%')[0] not in files.stem)
    if files.is_file() and files.suffix == '.mkv':
        fileList.append(files)


fileList.sort()

for f in fileList:
    # f1, f2, f3, ep = f.stem.split('-')
    # nameTemplate = '{}-{}-{}-{}{}'.format(f1.capitalize(),f2.capitalize(), f3.capitalize(), ep.upper(), f.suffix)
    fName1, fName2, fEp, fRes, fRip, fSource, fExt = f.name.split('.')
    nameTemplate = '{}-{}-{}.{}'.format(fName1.capitalize(),
                                        fName2.capitalize(), fEp.upper(), fExt)
    print(nameTemplate)
    f.rename(nameTemplate)
