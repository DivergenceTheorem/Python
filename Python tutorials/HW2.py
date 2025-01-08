import fractions
import math
import decimal

print("----- Задание 1 -----")
BASE = 16

num = int(input("Введите число: "))
ans = hex(num)
result = ''
while(num > BASE):
    result += str(num % BASE)
    num //= BASE
result += str(num)
print("Результат: ", result[::-1])
print("Проверяем: ", ans)

print("----- Задание 2 -----")
f1 = "1/3"
f2 = "3/5"
ans1 = fractions.Fraction(f1) + fractions.Fraction(f2)
ans2 = fractions.Fraction(f1) * fractions.Fraction(f2)

num1 = ''
num2 = ''
den1 = ''
den2 = ''

# Раскладываем строки на numerator - num и denominator - den

passed = False
for i in f1:
    if(i == '/'): 
        passed = True
        continue
    if(not passed):
        num1 += i
    else:
        den1 += i
num1 = int(num1)
den1 = int(den1)

passed = False
for i in f2:
    if(i == '/'): 
        passed = True
        continue
    if(not passed):
        num2 += i
    else:
        den2 += i
num2 = int(num2)
den2 = int(den2)

print(f"Дробь 1: {f1}; Дробь 2: {f2}")

# Сумма:

den = math.lcm(den1, den2)
num = int(num1 * (den/den1) + num2 * (den/den2))

print(f"Сумма: {num}/{den}" if den != 1 else f"Сумма: {num}", f"(Ответ: {ans1})")

# Произведение

num = num1 * num2
den = den1 * den2

simplify = math.gcd(num, den)
num = int(num / simplify)
den = int(den / simplify)

print(f"Произведение: {num}/{den}" if den != 1 else f"Произведение: {num}", f"(Ответ: {ans2})")











