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

    file.replace(path / transliterate(file.name))
    

def get_key(dictation: dict, file_suffix) -> dict.keys:

    for key, val in FORMATS.items():
            for i in val:
                if file_suffix in i:
                    return key

def sort_files(path: Path, file_name: Path):

    key = get_key(FORMATS, file_name.suffix)
    
    if key:
        fold_i = Path(f'{path}\{key}')
        fold_i.mkdir(exist_ok=True)
        file.replace(fold_i / file_name.name)
    else:
        fold_n = Path(f'{path}\\another')
        fold_n.mkdir(exist_ok=True)
        file.replace(fold_n / file_name.name)



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
    sort_files(path, file)


