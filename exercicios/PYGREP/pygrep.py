import sys
import io
import os

argv_len = len(sys.argv)

# if argv_len > 1:
#     search_string = sys.argv[1]
# if argv_len > 2:
#     search_string = sys.argv[2]
if argv_len > 3:
    search_string = sys.argv[1]
    search_type = sys.argv[2]
    path = sys.argv[3]
else:
    sys.exit("Argumentos inválidos. Utilize string_de_busca tipo_de_busca(arquivo/pasta) caminho")

def search_file(file_path):
    with io.open(file_path) as file:
        if search_string in file.read():
            print("Texto encontrado no arquivo localizado em:", file_path)

def search_folder(folder_path):
    with os.scandir(folder_path) as entries:
        for entry in entries:
            if entry.is_file():
                search_file(entry.path)
            if entry.is_dir():
                search_folder(entry.path)

if search_type == 'arquivo':
    search_file(path)
elif search_type == 'pasta':
    search_folder(path)
else:
    sys.exit("Tipo de busca não reconhecido pelo sistema, Utilize arquivo ou pasta")