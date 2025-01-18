import os
import random

filename = 'data2.txt'
os.chdir("Documents/GitHub/Python/Python tutorials/HW7")
NAME_LENGTH_MIN = 4
NAME_LENGTH_MAX = 7
VOWELS = 'aeiouy'

def name_generator(count: int, filename: str):
    names = []

    for _ in range(count):
        while True:
            length = random.randint(NAME_LENGTH_MIN, NAME_LENGTH_MAX)
            name = ''.join(chr(random.randint(65, 90)) for _ in range(length))

            if any(v in name.lower() for v in VOWELS):
                names.append(name.title())
                break

        with open(filename, 'w+', encoding='utf-8') as f:
            for name in names:
                f.write(f"{name} \n" if name != names[-1] else f"{name}")

    # while(counter < count): # Генерируем список имен
    #     has_vowel = False
    #     name = []
    #     length = random.randint(NAME_LENGTH_MIN, NAME_LENGTH_MAX) # Задаем длину имени
    #     for _ in range(length): # Генерируем имя внутри цикла
    #         letter = chr(random.randint(65, 90))
    #         if(letter.lower() in vowels): 
    #             has_vowel = True
    #         name.append(letter) # Генерирует имя в виде списка, состоящего из символов
            
    #     if(has_vowel):
    #         names.append((''.join(name)).title()) # Добавляет имя в список имя, в виде обычной строки, с заглавной буквы
    #         counter += 1
        # f.writelines(f"{name} \n" for name in names)

# if __name__ == '__main__':
#     name_generator(8, filename)
        
