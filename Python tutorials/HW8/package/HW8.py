"""
2. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
"""

import os

# os.chdir("/Users/meirzhankurmanov/Documents/GitHub/Python/Python tutorials/HW8/test_directory")
directory = os.getcwd()


def recursive_path(directory: str): # Функция, которая рекурсивно проходится по всему содержимому директории
    my_dict = {}
    file_sizes = {}
    # directory_sizes = {}
    walk_path = os.walk(directory)
    for dir_path, dir_name, dir_names in walk_path:
        my_dict[dir_path] = {'Directories': dir_name, 'Files': dir_names, 'Size': 0}
    
    for key, value in my_dict.items():
        if value['Directories'] == []:
            for file in value['Files']:
                path = key + '/' + file
                file_sizes[file] = os.path.getsize(path)
                value['Size'] += file_sizes[file]

        
    for key, info in my_dict.items():
        if info['Directories'] != []: # Если внутри директории есть другие директории...
            for i in info['Directories']: # То проходимся по каждой вложенной директории
                path = key + '/' + i # Получаем путь к ней
                # directory_sizes[i] = my_dict[path]['Size']
                info['Size'] += my_dict[path]['Size']
        print(f'{key} : {info}')

    return my_dict


# recursive_path(directory)