print("----- Задание 1 -----")
file = "Users/Desktop/Coding/Python/HW5.py"

def file_path(file):
    print("File path: ", file)
    file = file.split("/") 
    print("File name: ", file[-1])
    print("File extension: ", file[-1].split(".")[-1])

file_path(file)

print("----- Задание 2 -----")
names = ["Pete", "Jeff", "Whitney"]
salary = [10000, 8000, 11000]
bonus = ['10.25%', '8.0%', "11.5%"]

def dict_generator(names: list[str], salary: list[int], bonus: list[str]) -> dict:
    bonus = [float(i.replace("%", ''))/100 for i in bonus]
    my_dict = dict(zip(names, [i * j for i in salary for j in bonus]))
    print(my_dict)

dict_generator(names, salary, bonus)

print("---- Задание 3 ----")

def fibonacci(n): #1, 1, 2, 3, 5, 8, 13 ...
    f_0 = 1
    f_1 = 1
    for i in range(n):
        yield f_0
        yield f_1
        f_0 = f_0 + f_1
        f_1 = f_0 + f_1

numbers = []
for i in fibonacci(5):
    numbers.append(i)


