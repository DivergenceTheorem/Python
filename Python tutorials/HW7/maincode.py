from package.HW7 import group_rename
# import package.task1
# import package.task2
import os

# os.chdir("/..")
os.chdir("/Users/meirzhankurmanov/Documents/GitHub/Python/Python tutorials/HW7/current_files")

NUMBER_OF_DIGITS = 3    
SAVE_INTERVAL = [1, 3]

current_names = os.listdir()
print(os.listdir())
current_extensions = [x.split('.')[1] for x in current_names]

names_new = ['text1', 'file2', 'file3']
extensions_new = ['txt', 'py', 'ipynb']

group_rename(names_new, NUMBER_OF_DIGITS, current_extensions, extensions_new, SAVE_INTERVAL)