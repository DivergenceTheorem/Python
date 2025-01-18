import os 
from pathlib import Path
from random import randint
from random import uniform

MIN_NUMBER = -1000
MAX_NUMBER = 1000

filename = 'data.txt'
print(os.getcwd())
os.chdir("Documents/GitHub/Python/Python tutorials/HW7")


def generate_number_file(count: int, filename: str):
    """Заполняет файл случайными числами"""
    with open(filename, 'w+', encoding='utf-8') as f:
        for i in range(count):
            num = str((randint(MIN_NUMBER, MAX_NUMBER), uniform(MIN_NUMBER, MAX_NUMBER)))
            f.write(f"{num} \n" if i+1 < count else f"{num}")


# if __name__ == '__main__':
#     generate_number_file(8, filename)
