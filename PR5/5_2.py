# -*- coding: utf-8 -*-
"""

    Практическая работа 5. номер зачетной книжки 21-702
    Автор: Федоров Артем Андреевич
    Дата:26.01.2022

    Задание 2:Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
"""

def chislo():
    x=int(input("ввидите число больше 2:"))
    p=1
    if x<=2:
        print("ввидите другое число")
    else:
        while p <= x:
            p=p+1
            if x%p!=0:
                print(x)
            break
    return "конец"
print (chislo()) 