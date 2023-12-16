# name = "Elena"  # инициализация переменной
# print("Hello,", name)
# age = 20.4
# print(age)
# text = "Hello"
# print(text)
# print(text + str(age))
# print(type(age))  # int - 20, float - 20.4
# print(type(text))  # str - "Hello"
# a = False  # True
# print(a)
# print(type(a))  # bool - True, False

# a = 4
# b = 5
# print(a, id(a))
# print(b, id(b))
# a = b
# print(a, id(a))
# print(b, id(b))


# a = b = c = 1
# print(a)
# print(b)
# print(c)


# a, b, c = 5, "Hello", 9.2
# print(a)
# print(b)
# print(c)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 10
# b = 20
# print("a:", a)
# print("b:", b)
# # c = a  # 1
# # a = b  # 2
# # b = c  # 1
# a, b = b, a
# print("a:", a)
# print("b:", b)


# print("строка \
# символов")
# print('\tстрока \n          символов D:\\folder\\file.txt')

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# # print(s1, ",", s2, "!")
# b = s3 * 5
# print(b)

# print(456414654165341563454789)
# print(4.56414654165341563454789)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)  # 3.0
# print(6 / 4)  # 1.5
# print(6 // 2)  # 3
# print(6 // 4)  # 1
# print(6 ** 2)
# print(6 % 4)

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)  # 113

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
#
# num -= 3  # num = num - 3
# print(num)  # 12

#
# num = 4325  # => 432
# print("Исходное число:", num)
# a = num % 10
# print(a)  # 5
# num //= 10
# # print(num)  # 432
# b = num % 10
# print(b)  # 2
# num //= 10
# # print(num)  # 43
# c = num % 10
# print(c)  # 3
# num //= 10
# # print(num)  # 4
# d = num % 10
# print(d)  # 4
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4325
# a = num // 1000
# b = (num // 100) % 10
# c = (num % 100) // 10
# d = num % 10
# new_num = d * 1000 + c * 100 + b * 10 + a
# print(new_num)


# num = 4325  # => 432
# print("Исходное число:", num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)


# num1 = "2.3"
# num2 = 3
# # res = num1 + str(num2)  # 23
# # res = int(num1) + num2  # 5
# res = float(num1) + num2  # 5.3
# print(res)

# print(int(3.8))
# print(round(3.895, 2))
# print(type(round(3.891, 2)))

# name = "Виктор"
# age = 28
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", end=" --//-- ", sep="---")
# print("Я учу Python.")

# name = input("Введите имя: ")
# print(name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# res = num ** power
# print("Число", num, "в степени", power, "равно", res)
# print(type(num))

# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5

# False => "", 0, False, None

# print(bool("python"))
# print(bool(""))
# print(bool(-0.2))
# print(bool(0))
# print(bool(False))
# print(bool(None))
# test = None
# print(test)

# print(7 == 7)
# print(2 + 5 == 7)
# print(7 != 10 - 7)
# print(8 > 5)
# print(8 < 5)
# print(9 <= 9)
# print(9 >= 9)
# print("привет" > "ПРИВЕТ")


# print(2 < 4 < 9)  # 2 < 4 < 9  => True && True  => True
# print(2 * 5 > 7 >= 4 + 3)  # True && True => True
# print(3 * 3 <= 7 >= 2)  # False && True => False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 5 False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True:False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False:True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False:False)


# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True:False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False:True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False:False)


# print(9 - 7)
# print(not 9 - 7)
# print(not 7 - 7)


# cnt = 5
# if cnt < 10:
#     cnt += 2
#     print(cnt)


# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")


# a = 35
# b = 25
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")

# a = input('Введите a = ')
# b = input('Введите b = ')
# c = input('Введите c = ')
#
# if a == b == c:
#     print('Треугольник равносторонний.')
# elif a == b or a == c or b == c:
#     print('Треугольник равнобедренный.')
# else:
#     print('Треуголник разносторонний.')

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:   # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")


# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("ворона")
#     elif 2 <= n <= 4:  # n == 2 or n == 3 or n == 4
#         print("вороны")
#     else:
#         print("ворон")
# else:
#     print("Ошибка ввода данных")

# password = "qwerty"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Логин не найден")

# day = 'вторник'
# time = 14
#
# match day:
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница" if 9 <= time <= 13 or 15 <= time <= 16:
#         print("Рабочий день")
#     case "суббота" | "воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")


# a, b = 10, 20
#
# print(a if a < b else b)
#
# if a < b:
#     print(a)
# else:
#     print(b)

# a, b = 10, 20
#
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a = 5
# b = 0
# print("на ноль делить нельзя " if b == 0 else a / b)
# print(a / b)

# a = int(input('Введите числитель: '))
# b = int(input('Введите знаменатель: '))
# print('Результат:', a / b if b else 'На ноль делить нельзя')


# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
#
#
# print("Следующая строка")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводит строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводит строки или нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключения
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполнится в любом случае
#     print("Конец программы")


# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     n = int(n)  # n = 5
#     m = int(m)  # m = 'два'
# except ValueError:
#     n = str(n)  # n = '5'
# finally:
#     print(n + m)  # '5' + 'два'


# n1 = input('Введите первое число: ')
# n2 = input('Введите второе число: ')
# try:
#     print(int(n1) + int(n2))
# except ValueError:
#     print(str(n1) + str(n2))


# Циклы
# while

# i = 0
# while i < 5:
#     print("i =", i)
#     i = i + 1  # i += 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1


# i = 1
# while i <= 20:
#     print("i =", i)
#     i += 2

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# n = int(input("Кол-во символов: "))
# # i = 0
# # while i < n:
# #     print("*")
# #     i += 1
# print("*\n" * n)

# a = int(input("Введите начало диапазона: "))  # 5
# b = int(input("Введите конец диапазона: "))  # 10
# res = 0
# while a <= b:  # 5 6 7 8 9 10
#     if a % 2:  # a % 2 != 0
#         res += a
#     a += 1
# print(res)  # 21


# a = int(input('Введите начало диапазона: '))  # 5
# b = int(input('Введите конец диапазона: '))  # 10
# if a % 2 == 0:  # 5
#     a += 1
# res = 0
# while a <= b:  # 5 <= 10
#     print("a =", a)
#     res += a  # res = 0 + 5
#     a += 2  # a = a + 2
# print(res)


# n = int(input("Введите количество символов: "))  # 5
# symbol = input("Тип символа: ")
# orient = int(input("0 - горизонтальная\n1 - вертикальная\nориентация линии: "))
# i = 0
# while i < n:
#     if orient == 0:
#         print(symbol, end=" ")
#     if orient == 1:
#         print(symbol)
#     i += 1

#
# n = input("Введите число: ")
#
# while type(n) != int and type(n) != float:
#     try:
#         n = int(n)
#     except ValueError:
#         try:
#             n = float(n)
#         except ValueError:
#             print("Число не целое и не вещественное!")
#             n = input("Введите число: ")
# n = int(n)
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     res *= n
#
# print(res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i, end=" ")
#     i += 1
# else:
#     print("\nЦикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 15:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1


# for element in collection:
#    print(element)

# for i in "Hello", "World", "!":
#     print(i)


# for element in range(n):
#    print(element)

# print(list(range(5)))

# range(start, stop, step)  # start=0  step=1

# for i in range(1, 9):
#     print(i, end=" ")
#
# print()
#
# i = 9
# while i > 0:
#     print(i, end=" ")
#     i -= 2

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 99 + 1, 11):
#     print(i, end=' ')
# print()
# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")
# print()
# a = 100
# for i in range(11, a + 1, 11):
#     # if a % 0.5 == 0:
#     print(i, end=" ")
# print()
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a, b + 1):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')


# for i in range(3):  # 0 1 2
#     print("+++ i =", i)
#     for j in range(2):  # 0 1
#         print("----- j =", j)

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# nums = [letter * 3 for letter in "Banana"]
# nums = [i for i in range(30) if i % 2 == 0]
# print(nums)


# Список (list)
# nums = [8, 3, 9, 4, 1]
# print(nums)
# # print(type(nums))
# #
# # print(nums[0])
# # print(nums[2])
# # # print(nums[6])  # IndexError
# # print(nums[-1])
# # print(nums[-2])
# #
# # nums[1] = 256
# # print(nums)
# # nums[3] += 100
# # print(nums)
# # print(len(nums))
# for i in range(len(nums)):
#     print(nums[i] ** 2)


# s = []
# print(s)
#
# b = list("Hello")  # "Hello" => []
# print(b)
# print(b[0])

# print(range(6))
# n = list(range(6))
# print(n)
#
# print(list(range(2, 10)))
# print(list(range(2, 10 + 1, 2)))


# [выражение for переменная in последовательность]

# a = [0 for _ in range(5)]
# print(a)


# n = 5
# b = [i ** 2 for i in range(1, n + 1)]
# print(b)

# a, b = [1, 2, 3], [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)


# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("-> ") for i in range(int(input("n = ")))]
# print(a)

# a = [int(input("->")) for i in range(int(input("Количество элементов: ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         print(a[i])
#         s += a[i]
# print("Сумма: ", s)

# a = [int(input()) for i in range(int(input("Введите количество элементов списка: ")))]
# print(a)
# j = 0
# for i in a:
#     if i < 0:
#         j += i
# print(j)

# a = list(range(10, 100, 10))
# print(a)
#
# for i in range(len(a)):  # 0 1 2 3 4 5 6 7 8
#     print(a[i] + 2, end=" ")  # a[i] = 10 20 30 40 50 60 70 80 90
# print()

# for i in a:
#     print(i + 2, end=" ")  # 10 20 30 40 50 60 70 80 90

# n = int(input('Введите количество элементов списка: '))
# a = [int(input('-> ')) for _ in range(n)]
#
# sum_negative = sum([num for num in a if num < 0])
# print('Сумма отрицательных элементов:', sum_negative)

# a = [int(input('-> ')) for _ in range(int(input('n = ')))]
# print('Сумма отрицательных элементов:', sum([num for num in a if num < 0]))

# n = list(range(21, 41))
# print(n)
# s = k = 0
# # for i in range(len(n)):
# #     if n[i] % 2 == 0:  # четный элемент
# #         k += 1  # 10
# #     else:
# #         s += n[i]  # 300
#
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print("sum нечетных элементов: ", s)
# print("count четных элементов: ", k)


# n = list(range(21, 41, 2))
# print(n)
# a = 2
# print(n[a])
# print(n[a-1])
# print(n[a+1])

# a = [int(input('-> ')) for _ in range(int(input('n = ')))]
# print(a)
# for i in range(1, len(a)):
#     # print(a[i], "-> ", end="")
#     # print(a[i - 1])
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# Срез
# список[start:stop:step]

# a = [7, 8, 2, 1, 17, 9]
# print(a)
# # a[0], a[1] = a[1], a[0]
# # print(a)
# # print(a[1:4])
# # print(a[1:])
# # print(a[:3])
# print(a[5:2:-1])
# b = a[10:20]
# print(b)

# a = list(range(1, 8))
# print(a)
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[:1])
# print(a[-1:])
# print(a[3:4])
# print(a[-3:])
# print(a[-3:1:-1])
# print(a[2:5])

# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
#
# # s[2:5] = []
# # del s[1]
# del s[:]
#
# print(s)

# Методы списков

# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет список элементов в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(1, 100)  # добавляет элемент (второй параметр), в заданный индекс (первый параметр)
# print(s)
# s.insert(-1, 200)
# print(s)

# s = []
# n = int(input("Кол-во элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
# print(s)

# s = []
# n = int(input("Кол-во элементов: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print("Число не кратно 3: ")
#
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:  # 4
#     for j in b:  # 4
#         if i in c:  # если i находится в c
#             continue
#         if i == j:  # 3 == 3
#             c.append(i)
#             break
# print(c)  # [2, 1, 4, 3]

# a = [5, 9, 2, 1, 4, 3, 4, 2]
# b = [4, 2, 1, 3, 7, 2, 4]
# c = []
#
# for element in a:  # 2
#     if element not in c and element in b:  # if False and True
#         c.append(element)
#
# print(c)  # [2,1,4,3]

# a = [1, 2, 3, 7, 8, 9, 5]  # [11, 22, 33]
# b = [11, 22, 33]  # [1, 2, 3, 7, 8, 9, 5]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):  # 0 1 2
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):  # 3 4
#     c.append(b[i])

# if len(b) > len(a):
#     for i in range(len(a)):  # 0 1 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # 3 4
#         c.append(b[i])
# else:
#     for i in range(len(b)):  # 0 1 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):  # 3 4
#         c.append(a[i])


# print(c)


# s = [5, 9, 3, 7, 9, 1, 8, 9]
# print(s)
# s.remove(9)  # удаляет элемент по заданному значению
# print(s)
# s.pop()  # без параметров - удаляет последний элемент из списка
# print(s)
# a = s.pop(-1)  # передаем индекс для удаления элемента
# print(a)
# print(s)
# s.clear()  # очистка всех элементов списка
# print(s)

# a = [int(input('-> ')) for _ in range(int(input('n = ')))]
# print(a)

# numbers = [int(input('-> ')) for _ in range(int(input('n =')))]
# # numbers = [6, 4, 7, 8, 9]
# index = int(input('Введите индекс удаляемого элемента: '))
# numbers.pop(index)
# print(numbers)


# s = [5, 9, 3, 7, 9, 1, 8, 9]
# print(s)
# num = s.count(-9)  # считает кол-во заданных значений в списке
# # print(num)
#
# a = 9
# if a in s:
#     ind = s.index(a)  # возвращает индекс первого искомого элемента
#     print(ind)
# else:
#     print("Элемента", a, "не существует в списке")
# ind = s.index(9, 5)
# print(ind)


# a = [1, 2, 3]
# b = a.copy()  # возвращает копию списка
# print("a =", a)
# print("b =", b)
# a.append(20)
# print("a =", a)
# print("b =", b)
# b.append(120)
# print("a =", a)
# print("b =", b)

# a = [5, 4, 1, 2, 3]
# print(a)
# # a.reverse()  # перестраивает элементы списка в обратном порядке
# # print(a)
#
# # a.sort()  # сортировка элементов списка
# # print(a)
# a.sort(reverse=True)
# print(a)

# b = ["Виталий", "Сергей", "Александр", "Анна"]
# b.sort(key=len, reverse=True)
# print(b)

# a = [5, 4, 1, 2, 3]
# print(a)
# # a.sort()
# # print(a)
#
# #
# sort = sorted(a, reverse=True)
# print(sort)
# print(a)


# a = [5, 4, 1, 2, 3]
# print('a =', a)
# print(id(a))
# a.sort()
# print(id(a))
# sort = sorted(a)
# print(sort)
# print(id(sort))

# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(3, 9))  # (3, 9) - от 3 по 9 (включительно)
# print(random.randrange(3, 9, 2))  # # (3, 9) - от 3 до 9 (не включительно)
#
# print(random.uniform(10.5, 25.5))
# print(round(random.uniform(10.5, 25.5), 2))
#
# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# # print(random.choice(city_list))
# # print(random.choices(city_list, k=3))
# random.shuffle(city_list)
# print(city_list)


# s = [55, 66, 77, 88, 99, 9, 8, 7, 6, 5, 4, 1, 2, 3]
# print(random.choice(s))
# print(random.choices(s, k=5))

# lst = ['5', '4', '3', '2', '1']
# print(len(lst))
# # print(sum(lst))
# print(min(lst))
# print(max(lst))
#
# a = ['5', '4', '3', '2', '1']
# res = 0
# for i in a:
#     res += i  # res = res + i  => res = 0 + '5'
# print(res)
# print(sum(a))

# sum_ = 5
# print(sum_)
#
# s = [55, 66, 77, 88, 99, 9, 8, 7, 6, 5, 4, 1, 2, 3]
# print(sum(s))

# import random
#
# # mas = [random.randint(0, 20) for i in range(10)]
# # print(mas)  # [0,1,2,3,4,5,6,7,8,9]
# #
# # from random import randint
# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# m = max(lst)
# print(m)
# lst.insert(0, m)
# print(lst)

# import random
#
# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# print(max(lst))
# lst[0] = max(lst)
# print(lst)


# import random
# mas = [random.randint(0, 90) for i in range(10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)


# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# max_ = max(mas)
# print(max_)
# mas.remove(max_)
# mas.insert(0, max_)
# print(mas)

# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# print(max(mas))
# mas.insert(0, max(mas))
# mas.pop(-1)
# print(mas)

# import random
# #
# array = [random.randint(0, 20) for i in range(10)]
#
# max_element = max(array)
#
# print(array)
#
# print('Max:', max_element)
#
# for i in range(len(array)):
#     b = 5
#     if array[i] == max_element:
#         index_of_max_element = i
#         array.pop(i)
#         array.insert(0, max_element)
#         break
#
# # print(array)
# print(b)

# from random import randint
# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# m = max(lst)
# i = lst.index(m)
# print(m)
# m = lst.pop(i)
# lst.insert(0, m)
# print(lst)

# import random
#
# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
#
# min_ch = min(lst)
# print("min =", min_ch)
#
# ind_min = lst.index(min_ch)
# print("index min =", ind_min)
#
# del lst[:ind_min]
# print(lst)
# print(lst[ind_min:])


# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)
#
# print('a' not in x)
# print('e' not in x)

# lst = [5]
# # print(bool(lst))
# # # if len(lst) == 0:
# if not lst:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")
#
# b = 1
# if lst:
#     print('В списке есть элементы')
#     b = 5
# else:
#     print('Список пустой')
#
# print(b)


# import random
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# c = a + b
# a.extend(b)
# print("Третий список:", c)

# c = []
# d = []
# for element in a:
#     if element not in b and element not in d:
#         d.append(element)
# print('Элементы обоих списков без повторений:', d)


# d = []
# for element in a:
#     if element not in d:
#         d.append(element)
# for element in b:
#     if element not in d:
#         d.append(element)
# print('Элементы обоих списков без повторений:', d)

# c = []
# x = [i for i in c if c.count(i) == 2]
# print(x)

# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print("Элементы общие для двух списков:", c)

# c = [min(a), min(b), max(a), max(b)]
# print(c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# # m = ["Hello", "World"]
# print(m)
# # print(len(m))
# # print(m[1][2])
# print()
# # for row in range(len(m)):
# #     for col in range(len(m[row])):
# #         print(m[row][col], end="\t")
# #     print()
#
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# w, h = 4, 3
# # matrix = [[0 for x in range(w)] for y in range(h)]
# # matrix = []
# # for y in range(h):
# #     new_row = []
# #     for x in range(w):
# #         new_row.append(0)
# #     matrix.append(new_row)
# # print(matrix)
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# import random

# w, h = 4, 3
# matrix = [[random.randint(1, 30) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()


# matrix = [[random.randint(-20, 10) for x in range(3)] for i in range(4)]
# print(matrix)
# for i in matrix:
#     for j in i:
#         if j < 0:
#             print(j, end=" ")
# import random
#
# w, h = 3, 4
# matrix = [[random.randint(-20, 10) for x in range(w)] for y in range(h)]
#
# m = 0
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#         if x < 0:
#             m += 1
#     print()
#
# print("Количество отрицательный элементов:", m)


# for x, y, z in [[1, 2, 6], [3, 4, 8], [5, 6, 2], [7, 8, 4]]:
#     print(x, "+", y, "=", x + y)


# w, h = 4, 3
# matrix = [[input("-> ") for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# import math

# num1 = math.sqrt(4)
# num2 = math.ceil(3.1)
# num3 = math.floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
# print(math.pi)


# import math as m
# from math import sqrt, ceil
# from math import *

# num1 = sqrt(4)
# num2 = ceil(3.1)
#
# print(num1)
# print(num2)

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")

# seconds = time.time()
# print("Количество секунд:", seconds)
#
# locale_time = time.ctime(1541589933)
# print("Местное время:", locale_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep="")
#
# print(time.strftime("Сегодня: %B %d, %Y"))
#
# # print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime()))

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)

# Function
# print()
#
#
# def hello(name):  # аргументы
#     print("Hello,", name)
#
#
# hello("Irina")  # параметры
# hello("Igor")

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, '+', '-')
# symbol(7, 'X', '0')


# def get_sum(a, b):
#     print("Сумма: ", end="")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))

# def maximum(one, two):
#     if one > two:
#         return one - two
#     else:
#         return one + two
#
#
# print(maximum(17, 26))


# def cube(a):
#     return a ** 3  # a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def cube(a):
#     str = ''
#     for i in range(0, a + 1):
#         str += f'{i} в кубе = {i ** 3}\n'
#     return str
#
#
# res = cube(10)
#
# print(res)

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     # symbol1 = lst.pop(0)
#     # symbol2 = lst.pop()
#     # lst.append(symbol1)
#     # lst.insert(0, symbol2)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = 20
# b = 15
# print(is_greater(a, b))
# print(is_greater(5, 10))
#
# if is_greater(a, b):
#     print(a, "больше", b)
# else:
#     print(b, "больше", a)


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif 'a' <= ch <= "z":
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d  # 1 + 5 + 0 + 2
#                          # 1 + 5 + 2 + 1
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))  # 9
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))  # 8

# def set_param(c=20, s="-"):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# set_param(5, "*")
# set_param(s="#")

# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         current = n % 10
#         if even and current % 2 == 0:
#             s += current
#         if not even and current % 2:
#             s += current
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("\nСумма нечетных цифр:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")  # TypeError

# Изменяемые и неизменяемые объекты

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False
#
# a = "Hello"
# b = "Hello"
# print(id(a))
# print(id(b))
# print(a == b)  # True
# print(a is b)  # True

# n = [1, 2, 3]
# print(id(n))
#
# n.append(4)
# print(n)
# print(id(n))

# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# 72
# 48

# a = (5,)
# print(type(a))
# print(a)

# n = ["Hello", "Python"]
# b = tuple(n)
# print(type(b))
# print(b)

# a = (1, 2, 3, 4, 5, 6)
# print(a)
# print(a[3])  # 4
# print(a[1:3])  # (2, 3)
# # a[1] = 3  # не работает - TypeError

# from random import randint

# s = tuple(int(input("-> ")) for i in range(5))
# s = tuple(randint(0, 100) for i in range(5))
# print(s)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)
#
# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)
# # print(t1 * 2)
#
# # print(t3.count('l'))
# # if 'e' in t3:
# #     print(t3.index('e'))  #
#
# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             # a = tpl.index(el)  # 1
#             # b = tpl.index(el, a + 1) + 1  # 4 + 1
#             # return tpl[a:b]
#             return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]  # tpl[2:]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append("hi")
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)  # 1 2 3


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# first_name, year, married = get_user()
# # user = get_user()
# # first_name, year, married = user
# # print(user[0])
# # print(user[1])
# # print(user[2])
# print(first_name, year, married)

# tpl = (1, 2, 3, 4, 5, 6)
# print(tpl)
# lst = list(tpl)
# print(lst)
# ptl1 = tuple(lst)
# print(ptl1)
# del ptl1
# print(ptl1)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries, end="\n\n")
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "население =", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород:", city_name, "население =", city_population)

print("Вносим изменения")

