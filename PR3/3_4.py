# -*- coding: utf-8 -*-
"""

    Практическая работа 3. номер зачетной книжки 21-702
    Автор: Федоров Артем Андреевич
    Дата:26.01.2022

    Задание 4:Дано несколько чисел. Вычислите их сумму. Сначала вводите количество чисел N, затем вводится ровно N целых чисел. Постройте решение так, чтобы использовалось минимальное количество переменных.
"""

s=0
n=int(input('введите число n:'))
for i  in range(n):
    a=int(input('введите число:'))
    s += a
    print('сумма всех чисел=', s)
