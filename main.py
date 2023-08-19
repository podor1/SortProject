import shutil
import sys
import scan
import normalize
from pathlib import Path

''' List of extensions'''

images = ['.JPEG', '.PNG', '.JPG', '.SVG']
videos = ['.AVI', '.MP4', '.MOV', '.MKV']
docs = ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX']
music = ['.MP3', '.OGG', '.WAV', '.AMR']
archives = ['.ZIP', '.GZ', '.TAR']
FOLDERS = ['IMAGES','VIDEOS', 'DOCS', 'MUSIC', 'ARCHIVES', 'UNKNOWN', 'UNPACKED']



def handle(path, root_folder, dist):
    target_folder = root_folder/dist
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/normalize.normalize(path.name))




def handle_archive(path, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    new_path = path.replace(target_folder / normalize.normalize(path.name))
    unpack(new_path, target_folder)


def unpack(new_path, archives_folder):
    dist = new_path.name + '_unpacked'
    unpack_folder = archives_folder/dist
    unpack_folder.mkdir(exist_ok=True)
    shutil.unpack_archive(str(new_path.resolve()), str(unpack_folder.resolve()))






def remove_empty_folders(folder_path):
    for folder in folder_path.iterdir() :
        if folder.is_dir() :
            remove_empty_folders(folder)
            try :
                folder.rmdir()
            except OSError :
                pass








def main(folder_path):

    for iter_file in folder_path.iterdir() :
        if iter_file.is_dir() :
            if iter_file.name in FOLDERS :
                continue
            main(iter_file)
        else :
            if iter_file.suffix.upper() in images:
                handle(iter_file,arg.resolve() ,'IMAGES')

            elif iter_file.suffix.upper() in videos:
                handle(iter_file, arg.resolve(), 'VIDEOS')

            elif iter_file.suffix.upper() in docs:
                handle(iter_file, arg.resolve(), 'DOCS')

            elif iter_file.suffix.upper() in music:
                handle(iter_file, arg.resolve(), 'MUSIC')

            elif iter_file.suffix.upper() in archives:
                handle_archive(iter_file, arg.resolve(),'ARCHIVES')


            else :
                handle(iter_file, arg.resolve(), 'UNKNOWN')

    remove_empty_folders(folder_path)







if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")

    arg = Path(path)
    main(arg.resolve())
    scan.scan(arg.resolve())
    scan.write_info(arg.resolve())
    print("Sorting finished successfully")