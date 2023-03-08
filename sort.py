import sys
import re
from pathlib import Path
from dictionary import transliterate

FORMATS = {}
folders_to_del = []

try:
    path = Path(sys.argv[1])
except IndexError:
    print('Sorry. No param.')


def get_files(path: Path, file: Path):
    file.replace(path / item.name)


for item in path.glob('**/*.*'):
    get_files(path, item)

for item in path.glob('**'):
    folders_to_del.append(item)

for item in folders_to_del[::-1]:
    try:
        item.rmdir()
    except Exception as e:
        print(e)

with open('format.txt', 'r') as fd:
    line = fd.readline()
    while line:

        k = re.search(r'^\w+', line)
        v = re.findall(r'\.\w+', line)
        FORMATS.update({k.group() : v})
        line = fd.readline()

for file in path.iterdir():
    for k, v in FORMATS.items():
        for i in v:
            if file.suffix in i:
                fold_i = Path(f'{path}\{k}')
                fold_i.mkdir(exist_ok=True)
                file.replace(fold_i / file.name)
            else:
                fold_a = Path(f'{path}\\another')
                fold_a.mkdir(exist_ok=True)
                file.replace(fold_a / file.name)


