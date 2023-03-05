import sys
from pathlib import Path
import shutil
from dictionary import transliterate


try:
    path = Path(sys.argv[1])
except IndexError:
    print('Sorry. No param.')

create = None

def get_folders(path: Path):

    global create
    create = Path(f'{path}\\all_files')
    create.mkdir(exist_ok=True)

    def open_folder(name: Path):

        for item in name.iterdir():

            if not item.is_dir():
                shutil.move(item, create)
            if item.is_dir():
                open_folder(item)
    
    open_folder(path)


def remove_empty_folders(path: Path):
    count_ch = 0
    for i in path.iterdir():
        if i != create and i.is_dir():
            try:
                i.rmdir()
            except OSError:
                remove_empty_folders(i)

    for ch in path.iterdir():
        count_ch += 1

    if count_ch > 1:
        remove_empty_folders(path)

        

get_folders(path)

remove_empty_folders(path)

for item in create.iterdir():
    if item.suffix[1:] in ('jpeg', 'png', 'jpg', 'svg'):
        fold_i = Path(f'{path}\\images')
        fold_i.mkdir(exist_ok=True)
        shutil.move(item.replace(transliterate(item.name)), fold_i)
    elif item.suffix[1:] in ('avi', 'mp4', 'mov', 'mkv'):
        fold_v = Path(f'{path}\\videos')
        fold_v.mkdir(exist_ok=True)
        shutil.move(item.replace(transliterate(item.name)), fold_v)
    elif item.suffix[1:] in ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx', 'rtf'):
        fold_d = Path(f'{path}\\docs')
        fold_d.mkdir(exist_ok=True)
        shutil.move(item.replace(transliterate(item.name)), fold_d)
    elif item.suffix[1:] in ('mp3', 'ogg', 'wav', 'amr'):
        fold_m = Path(f'{path}\\musics')
        fold_m.mkdir(exist_ok=True)
        shutil.move(item.replace(transliterate(item.name)), fold_m)
    elif item.suffix[1:] in ('zip', 'gz', 'tar', 'rar'):
        fold_a = Path(f'{path}\\archives')
        fold_a.mkdir(exist_ok=True)
        shutil.move(item.replace(transliterate(item.name)), fold_a)
    else:
        fold_anot = Path(f'{path}\\another')
        fold_anot.mkdir(exist_ok=True)
        shutil.move(item.replace(transliterate(item.name)), fold_anot)
create.rmdir()