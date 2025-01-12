print("---- Задание 1 ----")
matrix = [[1,2, 3], [4, 5, 6], [7, 8, 9]]

def matrix_transpose(matrix: list[list]) -> list[list]:
    height = len(matrix)
    width = 0
    is_square = True
    for i in range(height):
        width = len(matrix[i])
        if width != len(matrix[i-1]) or width != height:
            is_square = False # Чтобы матрицу можно было транспонировать, она должа быть квадратной
    
    height = width
    if(is_square):     
        t_matrix = [[0 for _ in range(height)] for _ in range(height)]
        for i in range(height):
            for j in range(height):
                t_matrix[i][j] = matrix[j][i]
        return t_matrix
    
print(matrix_transpose(matrix))

print("---- Задание 2 ----")

def is_hashable(value): # Функция, которая проверяют "хэшируемость"
    try:
        hash(value)
        return True
    except TypeError:
        return False

def func(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        if(is_hashable(value)):
            my_dict[value] = key
        else:
            value = str(value)
            my_dict[value] = key
    return my_dict

print(func(maximus = 'gladiator', john = 'carpenter', leonidas = 'king'))

print("---- Задание 3 ----")

class BankAccount: # Cоздали отдельный класс, чтобы не приходилось заново объявлять все константы как nonlocal внутри каждой функции

    STANDARD_COMISSION_COEFFICIENT = 0.015
    MINIMUM_COMISSION_THRESHOLD = 30
    MAXIMUM_COMISSION_THRESHOLD = 600
    BONUS_COEFFICIENT = 0.03
    RICH_TAX_THRESHOLD = 5_000_000
    RICH_TAX_COEFFICIENT = 0.1

    def __init__(self):
        self.balance = 0
        self.history = []

    def deposit(self, amount: int | float = 0):
        if (amount % 50 == 0): # Кратно 50
            interest = int(amount * self.STANDARD_COMISSION_COEFFICIENT) # Cтандартная комиссия
            if(interest < self.MINIMUM_COMISSION_THRESHOLD): # Минимальная комиссия
                interest = self.MINIMUM_COMISSION_THRESHOLD
            elif(interest > self.MAXIMUM_COMISSION_THRESHOLD): # Максимальная комиссия
                interest = self.MAXIMUM_COMISSION_THRESHOLD
            
            if((len(self.history) + 1) % 3 == 0): # Проценты после каждой третьей операции
                interest = int(-amount * self.BONUS_COEFFICIENT)
            
            print("Операция прошла успешно!")
            if(self.balance < self.RICH_TAX_THRESHOLD):
                self.balance = self.balance - interest + amount # Новый баланс
            else:
                self.balance = self.balance * (1 - self.RICH_TAX_COEFFICIENT) - interest + amount
                print(f"Удержан налог на богатство: {self.balance * self.RICH_TAX_COEFFICIENT}")

            print(f"Зачислено: {amount}, комиссия: {interest}, баланс: {self.balance}" if interest > 0 else f"Зачислено: {amount}, бонус: {-interest}, баланс: {self.balance}")

            self.history.append(("Пополнение", amount))
            return None
        
        print("Сумма должна быть кратна 50!")

    def withdraw(self, amount: int | float = 0):
        if (self.balance < amount + self.MINIMUM_COMISSION_THRESHOLD): # Если денег на счете меньше чем суммая снятия + 30 
            print("Недостаточно средств для списания денег")
            return None
        
        if (amount % 50 == 0): # Кратно 50
            interest = int(amount * self.STANDARD_COMISSION_COEFFICIENT) # Cтандартная комиссия
            if(interest < self.MINIMUM_COMISSION_THRESHOLD): # Минимальная комиссия
                interest = self.MINIMUM_COMISSION_THRESHOLD
            elif(interest > self.MAXIMUM_COMISSION_THRESHOLD): # Максимальная комиссия
                interest = self.MAXIMUM_COMISSION_THRESHOLD
            
            if((len(self.history) + 1) % 3 == 0): # Проценты после каждой третьей операции
                interest = int(-amount * self.BONUS_COEFFICIENT)
            
            print("Операция прошла успешно!")
            if(self.balance < self.RICH_TAX_THRESHOLD):
                self.balance = self.balance - interest - amount # Новый баланс (без налога на богатство)
            else:
                self.balance = self.balance * (1 - self.RICH_TAX_COEFFICIENT) - interest - amount # Новый баланс (с налогом на богатство)
                print(f"Удержан налог на богатство: {self.balance * self.RICH_TAX_COEFFICIENT}")

            print(f"Зачислено: {amount}, комиссия: {interest}, баланс: {self.balance}" if interest > 0 else f"Зачислено: {amount}, бонус: {-interest}, баланс: {self.balance}")

            self.history.append(("Пополнение", amount))
            return None
        
        print("Сумма должна быть кратна 50!")
    

account = BankAccount()

operation = int(input("Добро пожаловть в банк! Выберите операцию \n 1 - Пополнение баланса \n 2 - Снятие денег \n 3 - Просмотр истории \n 4 - Выход из приложения \n"))

while(True):
    match operation:
        case 1:
            amount = int(input("Введите сумму: "))
            account.deposit(amount)
        case 2:
            amount = int(input("Введите сумму: "))
            account.withdraw(amount)
        case 3: 
            print(account.history)
        case 4:
            print("Приложение закрывается, спасибо за визит!")
            break
    operation = int(input("Выберите операцию \n 1 - Пополнение баланса \n 2 - Снятие денег \n 3 - Просмотр истории \n 4 - Выход из приложения \n"))


