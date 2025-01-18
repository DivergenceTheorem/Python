# 1. Решить задачи, которые не успели решить на семинаре.
# 2. Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# 3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

import os
from pathlib import Path

NUMBER_OF_DIGITS = 3
SAVE_INTERVAL = [1, 3]

# os.chdir("/..")
os.chdir("/Users/meirzhankurmanov/Documents/GitHub/Python/Python tutorials/HW7/current_files")
current_names = os.listdir()
current_extensions = [x.split('.')[1] for x in current_names]

names_new = ['text1', 'file2', 'file3']
extensions_new = ['txt', 'py', 'ipynb']

# print(current_names, '\n', names_new)



def group_rename(names_new: list[str], num: int, current_extensions: list[str], extensions_new: list[str], interval: list[int]) -> None:
    omit = 0 # Если перед каким-либо файлом, предыдущий файл не был переименован и не получил порядковый номер, то кол-во непронумерованных файлов сохраняется в этой переменной 
    for i, name in enumerate(names_new):
        order = str(i + 1 - omit) # Смещение переиодического номера с учетом непронумерованных файлов
        periodic_num = ['0' for _ in range(num)]
        periodic_num.append(order)
        if(len(periodic_num) > num):
            periodic_num.pop(0)
        if(names_new[i] + f'.{extensions_new[i]}' != current_names[i]):
            saved_old = current_names[i][interval[0] - 1:interval[1] - 1] # Часть старого имени, которую мы сохраняем (пункт 'e')
            names_new[i] = saved_old + name + f' #{''.join(periodic_num)}' + f'.{extensions_new[i]}'
        else:
            names_new[i] = names_new[i] + f'.{extensions_new[i]}'
            omit += 1

    for old_name, new_name in zip(current_names, names_new):
        os.rename(old_name, new_name)


# group_rename(names_new, NUMBER_OF_DIGITS, current_extensions, extensions_new, SAVE_INTERVAL)