# -*- coding: utf-8 -*-
"""

    Практическая работа 3. номер зачетной книжки 21-702
    Автор: Федоров Артем Андреевич
    Дата:26.01.2022

    Задание 6:Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!. По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
"""

def chislo():
    n1=1
    n=int(input('введите число n:'))
    
    for i in range(1,n+1):
        n1 *=1
    print('факториал',n,'=',n1)


print(chislo())