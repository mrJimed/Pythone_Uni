# Вариант 2 (openpyxl)
# 1.Нужно создать XLSX файл с таблицей размера около NxM, где N - количество букв в своем имени, M - количество букв в фамилии. Заполнить таблицу целыми числами от 1 до N*M, сохранить (проще в папке с .py файлом).
# 2.В Python открыть XLSX файл, считать таблицу.
# 3.Содержимое таблицы вывести в файл в CSV-формате, можно без заголовка — просто вывести все строки таблицы в отдельной строке в таком виде (пример таблицы 2x3):
# 232.1,112,324
# 1.3,34,9
# 4.Полученный csv-файл считать используя csv.reader (https://docs.python.org/3/library/csv.html)
# 5.Пусть A — матрица из считанных значений размера NxM, B — транспонированная матрица A. Нужно найти сумму элементов матрицы C=AB (произведение матриц) и вывести эту сумму на экран. Пусть d = суммы элементов по каждому из столбцов A (M чисел). Нужно найти сумму квадратов элементов d и вывести на экран.
# Сдать нужно .py файл, выполняющий 2–5, внизу комментариями написать 2 выведенных числа.
import math
import numpy as np
import openpyxl
import csv


def saveCSV(sheet):
    lst = [[], [], [], [], []]
    for row in range(1, sheet.max_row + 1):
        for col in range(sheet.max_column):
            lst[col].append(sheet[row][col].value)
    with open("TableCSV.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lst)
        file.close()


def readCSV():
    lst = [[], [], [], [], []]
    temp = 0
    with open("TableCSV.csv", newline='') as file:
        reader = csv.reader(file, delimiter=',', quotechar='|')
        for row in reader:
            for i in row:
                lst[temp].append(int(i))
            temp += 1
        file.close()
    arr = np.array(lst)
    return arr


def square(arr):
    sum = 0
    temp = 0
    for i in range(len(arr[0])):
        for k in range(len(arr)):
            temp += arr[k, i]
        sum += math.pow(temp, 2)
        temp = 0
    return int(sum)


saveCSV(openpyxl.open("TableX.XLSX", read_only=True).active)

A = readCSV()
B = A.transpose()
C = A.dot(B)

print("A\n")
print(A)

print("\n\nB\n")
print(B)

print("\n\nC\n")
print(C)

print("\nСумма всех элементов матрицы С: ", C.sum())
print("\nСумма квадратов элементов матрицы A: ", square(A))

# Сумма всех элементов матрицы С:  156525
# Сумма квадратов элементов матрицы A:  156525