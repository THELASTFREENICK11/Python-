day = int(input("День - "))
month = int(input("Месяц - "))
year = int(input("Год - "))
if (day > 31 or day < 1) or (month > 12 or month < 1):
    print("НЕВЕРНО")
else:
    if (month == 4 or 6 or 9 or 11) and (day>30):
        print("Неверно 1")
    elif (month == 2 and day>28) or (year%4==0 and day>29):
        print("Неверно 2")
    else:
        print("Верно")