import sys
from pathlib import Path


jpeg_files = list()
png_files = list()
jpg_files = list()
txt_files = list()
docx_files = list()
folders = list()
archives = list()
others = list()
unknown = list()
extensions = list()

registered_extensions = {
    "JPEG": jpeg_files,
    "PNG": png_files,
    "JPG": jpg_files,
    "TXT": txt_files,
    "DOCX": docx_files,
    "ZIP": archives,
    "FOLDERS": folders,
    "UNKNOWN EXTENSIONS": unknown,
    "OTHER FILES": others,
    "KNOWN EXTENSIONS": extensions
}


def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()

def scan(root_folder) :
    for file in root_folder.iterdir() :
        if file.is_dir() :
            folders.append(file.name)
            scan(file)

        else :
            extension = get_extensions(file)
            file_preffix = str(root_folder.parent)
            file_name = str(root_folder/file.name)
            if not extension :
                others.append(file_name.removeprefix(file_preffix))
            elif extension not in extensions :
                extensions.append(extension)
                try :
                    container = registered_extensions[extension]
                    container.append(file_name.removeprefix(file_preffix))
                except KeyError :
                    unknown.append(extension)
                    others.append(file_name.removeprefix(file_preffix))




def write_info(root_folder) :
    test_file = root_folder/'ScanInfo'
    with open(str(test_file),'w+') as fh :
        for key, value in registered_extensions.items() :
            fh.write(f'{key} : {value}\n')












if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")

    arg = Path(path)
    scan(arg)
    write_info(arg)




