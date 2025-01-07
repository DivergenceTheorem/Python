print("----- Задание 1 -----") 
a = 12
b = 5
c = 12

triangle = [a, b, c]
exist = True
isosceles = (a == b or a == c or c == b)
equilat = (a == b and a == c)

for i in triangle:
    if i >= sum(triangle) - i:
        exist = False

if(exist):
    print("Треугольник существует")
    if (equilat):
        print("Треугольник - равносторонний")
    elif(isosceles):
        print("Треугольник - равнобедренный")
    else:
        print("Треугольник - разносторонний")
else:
    print("Такого треугольника не существует")


print("----- Задание 2 -----")

num = int(input("Введите число: "))
if(num > 100000 or num < 0):
    print("Некорректное число")
elif(num == 1):
    print("1 не относится ни к простым, ни к составным числам")
else:
    prime = True
    for i in range(num):
        if ((i!=1 and i!=0) and (num%i == 0)):
            prime = False

    print("Число - простое" if prime else "Число - составное")


print("----- Задание 3 -----")
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
import random
num = random.randint(LOWER_LIMIT, UPPER_LIMIT)
iter = 0
a = LOWER_LIMIT
b = UPPER_LIMIT
mid = (a+b)//2
guess = mid
while(guess != num):
    iter += 1
    if (guess > num):
        b = mid
        print(guess, " - меньше")
    elif(guess < num):
        a = mid
        print(guess, " - больше")
    mid = (a + b)//2
    guess = mid

print("Загаданное число = %i, пройдено %i итераций" % (guess, iter))