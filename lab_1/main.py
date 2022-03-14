import numpy as np
import random as rnd
import timeit as tmi


def key(arr, x):
    return x in arr


def count(arr, x):
    return arr.count(x) == 1


def forIf(arr, x):
    for item in arr:
        if item == x:
            return True
    return False


def whileIf(arr, x):
    i = 0
    while i < 10 ** 7:
        if arr[i] == x:
            return True
        i += 1
    return False


def search(arr, x):
    arr2 = sorted(arr)
    for item in arr2:
        if item == x:
            return True
    return False


val = 0
lst = []
while val < 10 ** 7:
    val += 1
    lst.append(rnd.randint(0, 10 ** 9))

arr = np.array(lst)
print("Первые элементы в списке: ", lst[0:10])
x1 = int(input("Введите элемент для правильного поиска: "))
x2 = int(input("Введите элемент для ложного поиска: "))


time1 = tmi.timeit(lambda: key(lst, x1), number=5)
time2 = tmi.timeit(lambda: key(lst, x2), number=5)
print("1) key in arr # list\t", time1/5 * 1000, "м/с\t", time2/5 * 1000, "м/с")


time1 = tmi.timeit(lambda: count(lst, x1), number=5)
time2 = tmi.timeit(lambda: count(lst, x2), number=5)
print("2) arr.index или arr.count # list\t", time1/5 * 1000, "м/с\t", time2/5 * 1000, "м/с")


time1 = tmi.timeit(lambda: forIf(lst, x1), number=5)
time2 = tmi.timeit(lambda: forIf(lst, x2), number=5)
print("3) for, if, == # list\t", time1/5 * 1000, "м/с\t", time2/5 * 1000, "м/с")


time1 = tmi.timeit(lambda: whileIf(lst, x1), number=5)
time2 = tmi.timeit(lambda: whileIf(lst, x2), number=5)
print("4) while, if, == # list \t", time1/5 * 1000, "м/с\t", time2/5 * 1000, "м/с")


time1 = tmi.timeit(lambda: key(arr, x1), number=5)
time2 = tmi.timeit(lambda: key(arr, x2), number=5)
print("5) key in arr  # np.array \t", time1/5 * 1000, "м/с\t", time2/5 * 1000, "м/с")


time1 = tmi.timeit(lambda: forIf(arr, x1), number=5)
time2 = tmi.timeit(lambda: forIf(arr, x2), number=5)
print("6) for, if, ==  # np.array \t", time1/5 * 1000, "м/с\t", time2/5 * 1000, "м/с")


time1 = tmi.timeit(lambda: whileIf(arr, x1), number=5)
time2 = tmi.timeit(lambda: whileIf(arr, x2), number=5)
print("7) while, if, ==  # np.array,  \t", time1/5 * 1000, "м/с\t", time2/5 * 1000, "м/с")


time1 = tmi.timeit(lambda: search(arr, x1), number=5)
time2 = tmi.timeit(lambda: search(arr, x2), number=5)
print("8) Придумать самим. ,  \t", time1/5 * 1000, "м/с\t", time2/5 * 1000, "м/с")


# Первые элементы в списке:  [803656985, 915170751, 460823590, 655057713, 149325537, 733426126, 491146615, 372769561, 332229122, 509990510]
# Введите элемент для правильного поиска: 509990510
# Введите элемент для ложного поиска: -9
# 1) key in arr # list	 0.0011799857020378113 м/с	 158.4096200298518 м/с
# 2) arr.index или arr.count # list	 191.14178000018 м/с	 194.21938001178205 м/с
# 3) for, if, == # list	 0.0023199710994958878 м/с	 528.8080000318587 м/с
# 4) while, if, == # list 	 0.003220001235604286 м/с	 1292.3765600193292 м/с
# 5) key in arr  # np.array 	 14.683219976723194 м/с	 20.797959994524717 м/с
# 6) for, if, ==  # np.array 	 0.03442000597715378 м/с	 3354.541159979999 м/с
# 7) while, if, ==  # np.array,  	 0.008899997919797897 м/с	 5524.704799987376 м/с
# 8) Придумать самим. ,  	 19888.666460011154 м/с	 22642.855639988557 м/с