from sys import argv

date = argv[1]
print(argv[1])

def validity_check(date):
    parameters = ['Day', 'Month', 'Year']
    try:
        date = date.split(".")
        date = dict(zip(parameters, date))

        longer_months = [1, 3, 5, 7, 8, 10, 12]
        shorter_months = [4, 6, 9, 11]
        varying_month = 2

        day = int(date['Day'])
        month = int(date['Month'])
        year = int(date['Year'])
    except:
        return False

    if(year >= 1 and year <= 9999):
        if(month in longer_months):
            if(day>=1 and day<=31):
                return True
            else: 
                return False
        elif(month in shorter_months):
            if(day>=1 and day<=30):
                return True
            else: 
                return False
        elif(month in varying_month):
            if(year % 4 == 0 and (day>=1 and day <= 29)):
                return True
            elif(year % 4 != 0 and (day>=1 and day <=28)):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

print(validity_check(date))