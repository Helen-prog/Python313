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

# import geometry

# num1 = geometry.sqrt(4)
# num2 = geometry.ceil(3.1)
# num3 = geometry.floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
# print(geometry.pi)


# import geometry as m
# from geometry import sqrt, ceil
# from geometry import *

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

# print("Вносим изменения")


# print("Склонированный репозиторий")


# Множества (set)

# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s)
# print(type(s))
# print(len(s))

# a = set("hello")
# print(a, type(a))

# c = ("red", "blue", "green", "red")
#
# a = set(c)
# print(a, type(a))

# mas = [1, 2, 3, 2, 3, 4, 4, 5]
# s = {x for x in mas if x % 2 == 0}
# print(s)

# def to_set(element):
#     st = set(element)
#     return st, len(st)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# t = {"red", "green", "blue"}
# # print("green" not in t)
# for i in t:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = [i for i in r if 'a' not in i]
# # a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r]
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c']
# print(a)

# a = {"Tom", "Bob", "Alice"}
# print(a)
# a.add("Ann")
# print(a)
# # a.remove("Ann")  # при обращении к несуществующему элементу - ошибка KeyError
# # print(a)
# # user = "Ann"
# # if user in a:
# #     a.remove(user)
# # print(a)
# # a.discard("Ann1")
# # print(a)
# n = a.pop()
# print(n)
# print(a)
# a.clear()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # a |= b
# # c = a & b
# a &= b
# # c = a - b
# # a -= b
# # c = a ^ b
# # a ^= b
# # print(c)
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# count = len(s)
# print("Count:", count)
# print("Min:", min(s))
# print("Max:", max(s))
# print("Sum:", sum(s))

# s1 = set("Hello")
# s2 = set("How are you")
# a = s1 & s2
# print(a)
# for i in a:
#     print(i, end=" ")

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# one_hobby = drawing ^ music
# print("Один кружок:", one_hobby)
#
# both_hobbies = drawing & music
# print("Оба кружка:", both_hobbies)
#
# # drawing = drawing - both_hobbies
# drawing -= both_hobbies
# print("Кружок рисования:", drawing)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)
# print(a >= b)

# Тип frozenset
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# print(type(s))
# a = frozenset({"hello", "world"})
# print(a)

# a = [8, 9, 7, 4, 5, 8, 7, 9, 4, 6, 5, 1, 2, 3, 5]
# print(a)
# b = set(a)
# print(b)
# a = tuple(b)
# print(a)


# Словарь  (dict)
# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3, 4: "four"}
# lst[0] = 10
# print(lst[0])
# d['one'] = 10
# print(d['one'])
# print(d[4])

# d = {'one': 1, 'two': 2, 'four': "four"}
# print(d)
# print(type(d))
#
# d1 = dict(one=1, two=2, four="four")
# print(d1)
# print(type(d1))

# d = {0: 1, 'two': 2, (1, 2.3): "кортеж", True: [2, 3, 6, 7], 1: 45, False: (1, 2)}
# {0: (1, 2), 'two': 2, (1, 2.3): "кортеж", True: 45}
# d = {0: 1, 'two': 2, (1, 2.3): "кортеж", True: [2, 3, 6, 7]}
# print(d)
# print(d[True][1])
# print(d[(1, 2.3)])
# print(d['two'])
# print(d[0])

# lst = (('one', 1), ('two', 2), ('tree', 3))
# d = dict(lst)
# print(d)


# d = {a: a ** 2 for a in range(7)}
# print(d)


# d = {'one': 1, 'two': 2, 'four': 4}
#
# # print('one1' in d)
# key = "four1"
#
# # if key in d:
# #     del d[key]
#
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + key + " нет в словаре")
#
# for i in d:
#     print(i, "->", d[i])

# myDict = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# composition = 1
# for key in myDict:
#     composition *= myDict[key]
# print('Произведение:', composition)


# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# myDict = {3: 'x1', 7: 'x2', 5: 'x3', -1: 'x4'}
# print(sum(myDict))

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400]
# }
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")

# while True:
#     n = input('№: ')  # '2'
#     if n != '0':
#         qty = int(input('Количество: '))  # 8
#         try:
#             goods[n][1] += qty  # goods[n][1] = goods[n][1] + qty  # goods['2'][1] = 8
#         except KeyError:
#             pass
#     else:
#         break

# while True:
#     n = input('№: ')
#     if n != '0':
#         if n in goods:
#             qty = int(input('Количество: '))
#             goods[n][1] += qty
#         else:
#             print("Некорректный номер товара! ❌")
#     else:
#         break

# while True:
#     n = input('№: ')
#     if n != '0' and int(n) in range(len(goods) + 1):  # 9 in 0, 5
#         qty = int(input('Количество: '))
#         goods[n][1] += qty
#     else:
#         break

# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")

# d = {'a': 1, 'b': 2, 'c': 3}

# print(d.keys())  # список ключей
# print(d.values())  # список значений
# print(d.items())  # список ключей и значений

# for i, j in d.items():
#     print(i, "->", j)

# print(list(d.items()))

# d = {'a': 1, 'c': 3, 'b': 2}
#
# # d2 = d.copy()
# #
# # print("d:", d, id(d))
# # print("d2:", d2, id(d2))
# #
# # d2['a'] = 5
# # d['e'] = 7
# #
# # print("d:", d, id(d))
# # print("d2:", d2, id(d2))
# #
# # d.clear()  # очищает словарь
# # print("d:", d, id(d))
# # print("d2:", d2, id(d2))
#
# # print(d['e'])
# # value = d.get('b', "Такого ключа не существует")
# # print(value)
# # item = d.pop('a', "Такого ключа не существует")
# # item = d.popitem()
# # print(item)
# # print(d)
#
# d1 = {'r': 7, 'q': 40}
# d.update(d1)
# d2 = [('a', 20), ('b', 9)]  # 'a': 20, 'b': 9
# d.update(d2)
# print(d)

# x = {
#     'a': 1,
#     'b': 2
# }
#
# y = {
#     'b': 3,
#     'c': 4
# }
# # new_dict = x.copy()
# # new_dict.update(y)
# new_dict = x | y
# print(new_dict)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")

# sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#          "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#          "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#          "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ": ", sales[x][y], sep="")

# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
#
# sales[person][region] = new_data
# print(sales[person])

# try:
#     person = input('Введите имя: ')
#     saler = sales[person]
#     try:
#         region = input('Введите регион: ')
#         new_data = int(input('Введите новое значение: '))
#         sales[person][region] = new_data
#         print(sales[person])
#     except KeyError:
#         print('Такого региона нет')
#     except ValueError:
#         print("Некорректный ввод объема продаж (числовое значение)")
# except KeyError:
#     print('Такого продавца нет.')

# d = {"N": 3056, "S": 8463, "E": 8441, "W": 2694}
# d = {value: key for key, value in d.items()}
# print(d)
#
# d = {"N": 3056, "S": 8463, "E": 8441, "W": 2694}
# d.update({value: key for key, value in d.items()})
# print(d)

# d = {"E": 3, "N": 1, "S": 2, "W": 4}  # {"N": 1, "S": 2}  # {"E": 3, "N": 1}
# new_d = {k: v for k, v in d.items() if v <= 2}
# print(new_d)

# d = {'N': 1, 'S': 2, 'E': 3, 'W': 4}

# for i in range(2):
#     print('key:', list(d.items())[i][0], 'value:', list(d.items())[i][1])
#
# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# c = list(d)
# for key in c[:2]:
#     print(f'{key}: {d[key]}')
#
# for key, value in list(d.items())[2:4]:
#     print(f'{key}: {value}')
#
# value = list(d.items())
# print(value)
#
# value = list(d.values())
# print(value)
#
# value = list(d)
# print(value)

# a = [7, "one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()  # {}
# current_key = ""
#
# for item in a:  # 10
#     if type(item) == str:  # type(item) is str
#         d[item] = []  # {"one": [1, 2, 3], "two": [10]}
#         current_key = item  # current_key = "two"
#     else:
#         d[current_key].append(item)  # d["two"]
#
# print(d)

# print(type(a[1]))

# a = [7, 'one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# my_dict = dict()
# for i in range(len(a)):
#     if type(a[i]) is str:
#         my_dict[a[i]] = []
#         for j in range(i + 1, len(a)):
#             if type(a[j]) is int:
#                 my_dict[a[i]].append(a[j])
#             else:
#                 break
# print(my_dict)


# d = dict([(1, 'one'), (2, 'two'), (3, 'three')])
# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# f = {k: v for k, v in zip(b, a)}
# print(f)

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = [4.5, 7.4, 9.6]
# # c = tuple(zip(a, b))
# # c = list(zip(a, b))
# # c = set(zip(a, b))
# # c = dict(zip(a, b))
# # c = list(zip(a, ))
# c = list(zip(a, b, d))
# print(c)

# d_one = {'name': "Igor", "last_name": "Petrov", "job": "Consultant"}
# d_two = {'name': "Irina", "last_name": "Irisova", "job": "Manager"}
#
# for (k1, v1), (k2, v2) in zip(d_one.items(), d_two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)


# d = [(1, 'one'), (2, 'two'), (3, 'three')]
# a, b = zip(*d)
# print(a)
# print(b)


# a = ['two', 'one', 'three']
# b = [3, 2, 1]
#
# d = list(zip(a, b))
# print(d)
#
# d.sort()
# print(d)
# print(dict(d))

# d = dict(zip(a, b))
# print(d)
# s = sorted(d.items())
# print(s)
# print(dict(s))


# one = {'apple': 0.45, 'orange': 0.35, 'pepper': 0.7}
# two = {'pepper': 0.2, 'onion': 0.55}
# # print({**one, **two})  # {'apple': 0.45, 'orange': 0.35, 'pepper': 0.2, 'onion': 0.55}
#
# # print({**two, **one})  # {'pepper': 0.7, 'onion': 0.55, 'apple': 0.45, 'orange': 0.35}
#
# for k, v in {**two, **one}.items():
#     print(k, "->", v)


# data = ["red", "green", "blue"]
# num = 1
# for val in data:
#     print(num, ") ", val, sep="")
#     num += 1
#
# print()
# for num, val in enumerate(data, 1):
#     print(num, ") ", val, sep="")

# month = ["January", "February", "March"]
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     print(sales)
#     profit = sales - costs
#     print("Чистая прибыль в", m, "=", profit)

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     return args
#
#
# print(func(2))
# print(func(2, 3, 4, "abc"))
# print(func())

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(3, 4, 5))

# def to_dict(*args):
#     return {element: element for element in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))


# def func(*args):  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
#     midle = sum(args) / len(args)
#     print(midle)
#     res = []
#     for element in args:
#         if element < midle:
#             res.append(element)
#     return res
#
#
# a = 1, 2, 3, 4, 5, 6, 7, 8, 9
# # print(a)
# first = func(*a)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(first)
# second = func(3, 6, 1, 9, 5)
# print(second)


# def solution(*args):
#     print(args)
#     # type(args)
#     avg = sum(*args) / len(*args)
#     print(avg)
#     # # print(type(avg))
#     # # res = []
#     # # for num in args:
#     # #     if num < avg:
#     # #         res.append(num)
#     # # return res
#
#     print(*args)
#     return [num for num in a]  #if num < avg
#
#
# a = 1, 2, 3, 4, 5, 6, 7, 8, 9
# first = solution(a)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(first)


# def func(a, b, *args):
#     return a, b, args
#
#
# print(func(1, 8))
# print(func(1, 2, 3, 4, 5, 6, 7))


# def print_score(student, *scores):
#     print("Student Name:", student)
#     for score in scores:
#         print(score)
#
#
# print_score("Irina", 5, 4, 3, 2, 5)
# print_score("Igor", 5, 4, 5, 3, 2, 5)
# print_score("Lev")


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(d=9))


# def intro(**data):
#     for k, v in data.items():
#         print(k, '->', v)
#     print()
#
#
# intro(name="Irina", surname="Reznikova", age=22)
# intro(name="Igor", surname="Berukov", email='igor@mail.ru', age=25, phone="+7909999-46-89")


# def db(**kwargs):
#     my_dict.update(kwargs)
#     # print("внутри функции:", id(my_dict))
#
#
# my_dict = {"one": "first"}
# # print(id(my_dict))
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
# # print(id(my_dict))
# print(my_dict)


# def func(a, b, c, *args, d, e, **kwargs):
#     return kwargs, d, a, b, c, args, e
#
#
# print(func(5, 9, 7, 8, 4, 3, 2, 1, k1=22, k2=31, e=100, d=55, k3=11, k4=91))


# name = "Tom"

# print("глобальная область видимости: ", id(name))


# def hi():
#     global name
#     name = "Sam"
#     # print("локальная область видимости: ", id(name))
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# print(name)
# hi()
# bye()
# print(name)
# print("глобальная область видимости внизу: ", id(name))

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5

# x = 4
#
#
# def add_five(a):
#     # x = 2
#
#     def add_some():
#         # x = 1
#         print("x =", x)
#         return a + x
#
#     return add_some()
#
#
# print(add_five(5))


# sum = 5
#
# lst = [9, 5, 8, 7, 6]
# print(sum(lst))  # 5([9, 5, 8, 7, 6])

# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)

# def outer(who):
#     def inner():
#         print("Hello,", who)
#
#     inner()
#
#
# outer("World!")


# def fun1():
#     a = 6  # 2
#
#     def fun2(b):  # b = 4
#         a = 4  # 5
#         print(a + b)  # 6  # 4 + 4 = 8
#
#     print("a:", a)  # 3  # a = 6
#     fun2(4)  # 4
#
#
# fun1()  # 1


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a:", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t  # 25 + 30 = 55  # 25 + 35 = 60
# print(c)
# x = 5
#
#
# def fn1():
#     x = 25  # 2  # x = 55
#
#     def fn2():
#         # x = 33  # 4
#
#         def fn3():
#             nonlocal x
#             x = 55  # 6
#
#         fn3()  # 5
#         print('fn2.x =', x)  # 7  # x = 55
#
#     fn2()  # 3
#     print("fn1.x =", x)  # 8  # x = 55
#
#
# fn1()  # 1


# def outer(a1, b1, a2, b2):
#     a = 0  # 1
#     b = 0  # 7
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         # print(a)
#         # print(b)
#
#     inner()
#     return [a, b]


# res = outer(2, 3, -1, 4)
# print(res)  # [1, 7]


# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# item1 = outer(5)
# print(item1(10))
#
# item2 = outer(5)
# print(item2(1))

# print(outer(5)(20))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         # nonlocal a, b
#         # c.append(4)
#         # a += 1
#         # b += "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0  # 2  # 3
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res2()
#
# res1()

# lambda (анонимные функции)

# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func('a', 'b'))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))
# print((lambda x, y=5: x ** 2 + y ** 2)(2))
# print((lambda x=2, y=5: x ** 2 + y ** 2)())
# print((lambda x=2, y=5: x ** 2 + y ** 2)(y=10))

# print((lambda *args: args)(1, 2, 3, 4, 5))


# y = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for i in y:
#     print(i("abc__"))


# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(5)
# print(f(10))
#
#
# def outer1(n):
#     return lambda x: x + n
#
#
# f1 = outer1(5)
# print(f1(10))
#
#
# outer2 = lambda n: lambda x: x + n
#
# f2 = outer2(5)
# print(f2(10))
#
#
# print((lambda n: lambda x: x + n)(5)(10))

# print((lambda n: lambda x: lambda y: x + n + y)(2)(4)(6))

# def func(item):
#     return item[1]
#
#
# d = {'b': 3, 'c': 1, 'a': 2}  # {'c': 1, 'a': 2, 'b': 3}
# print(d)
# lst = list(d.items())  # [('b', 3), ('c', 1), ('a', 2)]
# print(lst)
# # lst.sort(key=lambda item: item[1])
# lst.sort(key=func)
# print(lst)
# d1 = dict(lst)
# print(d1)

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res1 = sorted(players, key=lambda item: item['rating'])
# print(res1)
#
# res2 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res2)


# a = [
#     lambda x, y: x + y,
#     lambda x, y: x - y,
#     lambda x, y: x * y,
#     lambda x, y: x / y,
# ]
#
# print(a[0](5, 2))
# print(a[1](5, 2))
# print(a[2](5, 2))

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье')
# }
#
# d[6]()

# print((lambda a, b: a if a > b else b)(15, 23))


# print((lambda a, b, c: a if (a < b and a < c) else (b if b < c else c))(28, 29, 25))


# map(func, *iterables)

# def mult(t):
#     return t * 2


# lst1 = [2, 8, 12, -5, -10]
#
# # lst2 = list(map(mult, lst1))
# lst2 = list(map(lambda t: t * 2, lst1))
# print(lst2)  # [4, 16, 24, -10, -20]

# t = (2.88, -1.75, 100.55)
# # t2 = tuple(map(lambda x: int(x), t))
# t2 = tuple(map(int, t))
# print(t2)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)


# num = ['1', '2', '3', '4', '5']
# print(list(map(int, num)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)


# t = ('abcd', 'abc', 'asdfg', 'def', 'grt')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)


# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# # res = list(map(lambda s: s + 5, b))
# print(res)


# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# # m = list(map(lambda x: x ** 2, [1, 3, 5, 7, 9]))
# print(m)
# n = [x ** 2 for x in range(10) if x % 2]
# print(n)


# import random
#
# my_list = [random.randint(1, 40) for i in range(20)]
#
# print(my_list)
# # print(list(filter(lambda num: (num >= 10) and (num <= 20), my_list)))
# print(list(filter(lambda num: 10 <= num <= 20, my_list)))


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test())


# def my_decorator(func):
#     def wrap():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#     return wrap
#
#
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print("*" * 30)
#         func()
#         print("=" * 30)
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, I am func "func_test"')
#
#
# @my_decorator
# def hello():
#     print('Hello, I am func "hello"')
#
#
# func_test()
# hello()
# test = my_decorator(func_test)
# test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0  # 1
#
#     def wrap(arg1, arg2):
#         nonlocal count
#         count = count + 1
#         fn(arg1, arg2)
#         print("Вызов функции: ", count, "\n", "*" * 20, sep="")
#
#     return wrap
#
#
# @cnt
# def hello(a, b):
#     print("Hello,", a, "\nHello,", b)
#
#
# hello("Python", "JavaScript")
# hello("one", "two")
# hello()

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args", args)
#         print("kwargs", kwargs)
#         fn(*args, **kwargs)
#     return wrap
#
#
# @args_decorator
# def print_data(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_data("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_data("Владимир", "Екатерина", "Виктор")
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def multiply(arg):
#     """Параметры декоратора"""
#     def test(fn):
#         """Параметр - функция"""
#         def wrap(x):
#             """ Параметры функции"""
#             return fn(x) * arg
#         return wrap
#     return test
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# print(int('100', 2))  # 4
# print(int('100', 8))  # 64
# print(int('100', 10))  # 100
# print(int('100', 16))  # 256
#
# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12
#
#
# print(0b10010)
# print(0o22)
# print(0x12)
# print(0b10010 + 0o22 + 0x12 + 18)


# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)  # Python => Pytton
# # print(e * 3)
# # print('y' in e)
# # print('y1' in e)
# # print(e[-6])
# # print(e[:4])
# # print(e[2:])
# # print(e[::-1])
# e = e[:3] + 't' + e[4:]
# print(e)

# def changeCharToStr(s, c_old, c_new):
#     s2 = ""
#     i = 0
#
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = changeCharToStr(str1, "N", "P")
# print("str1 =", str1)
# print("str2 =", str2)

# print("Привет")
# print(u"Привет")

# print("C:\\folder\\file.txt\\")
# print(r"C:\folder\file.txt\\"[:-1])
# print(R"C:\folder\file.txt" + "\\")


# name = "Дмитрий"
# age = 25
# print(f"Меня зовут {name}. Мне {age} лет.")
# m = 2.58976415
# print(f"Число: {round(m, 2)}")
# print(f"Число: {m:.3f}")

# x = 10
# y = 5

# print("x = ", x, ", y = ", y, sep="")
# print(f"{x = }, {y = }")

# print(f"{x} x {y} / 2 = {x * y / 2}")
# num = 74
# print(f"{num}")

# dir_name = "my_doc"
# file_name = "data.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)

# s = """
# Многостро'чный' "новый"
# текст
# """
# print(s)
#
# s1 = '''
# Многострочный
#
#         текст
# '''
# print(s1)
#
# s2 = "Тек\nст"
# print(s2)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(sum.__doc__)
# print(min.__doc__)
# print(len.__doc__)


# from geometry import pi


# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     print("Hello")
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord("a"))  # 97
# print(ord("й"))  # 1081

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break
#
# print(chr(1104))

# s = "Test string for me"
# arr = [ord(x) for x in s]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(1048))
# print(chr(8364))

# print("apple" == "Apple")  # 97 == 65
# print("apple" > "Apple")  # 97 > 65
#
# print(ord("a"))
# print(ord("A"))

# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     result = ""
#     for i in range(random_length):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print("Ваш случайный пароль:", random_password())


# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.
# print(s)
# print(s.count("h"))  # возвращает количество точных вхождение подстроки в строку
# print(s.count("h", 1, -4))
# print(s.find("Python", 10, -20))  # ищет в строке подстроку и возвращает ее индекс, если совпадение не найдено,
# # то возвращает
# # "-1"
# print(s.find("l1"))
# print(s.rfind("l1"))
#
# print(s.index("l"))  # ищет в строке подстроку и возвращает ее индекс, если совпадение не найдено, возвращает
# # исключение ValueError
# print(s.rindex("l"))


# _s = input('Введите два слова через пробел: ')  # один два
# first = _s[:_s.find(" ")]
# second = _s[_s.find(" ") + 1:]
# print(second + " " + first)

# print(s.startswith("hello"))  # возвращает True, если строка начинается с указанной подстроки
# print(s.find("I am"))
# print(s.startswith("I am", 14))
#
# print(s.endswith("on."))  # возвращает True, если строка заканчивается указанной подстрокой
# print(s.endswith("lo", 3, 5))

# print("abc123".isalpha())
# print("abcABC".isalpha())  # определяет состоит ли строка только из букв
# print("".isalpha())
# print('123'.isdigit())  # определяет состоит ли строка только из цифр
# print('123.234'.isdigit())
#
# print("abc123".isalnum())   # определяет состоит ли строка только из букв и цифр
# print("abcA123".isalnum())

# print("abc".islower())  # определяет, являются ли буквенные символы строки строчными
# print("!abc456A".islower())
#
# print("!456A".isupper())  # определяет, являются ли буквенные символы строки в верхнем регистре

# print('py'.center(10, "-"))  # выравнивает строку по центру
# print('py'.center(11, "-"))

# удаляют пробельные символы слева или справа
# print("     py".lstrip())
# print("py     ".rstrip())
# print("    py     ".strip())
#
# print("https://www.python.org".lstrip())
# print("https://www.pythons.org".lstrip("/:pths").rstrip(".org"))
# print("https://www.pythons.org".strip("/:pths.org"))


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1)
# print(str1.replace("Nython", "Python", 2))

# s1 = "-"
# seq = ("a", "b", "c")
# print(s1.join(seq))
# print("..".join(['1', '2']))  # объединение итерируемой последовательности (состоит из строковых значений) в строку
# print(":".join("Hello"))

# print(s.split())
# print('www.python.org.ru'.split(".", 2))  # делит строку на список, состоящий из подстрок
# print('www.python.org.ru'.rsplit(".", 2))


# a = input("-> ").split()
# print(a)


# a = input("Введите ФИО: ").split()
# print(a)
# print(a[0], a[1][0] + ".", a[2][0] + ".")
#
# d = [[1, 2, 3], [4, 5, 6]]
# print(d[1][0])


# a = input("Введите коды символов через пробел: ").split()
# print(a)
#
# b = list(map(int, a))
# print(b)


# Регулярные выражения

# import re
#
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r"\."
# print(re.findall(reg, s))   # возвращает список, содержащий все совпадения с шаблоном
#
# print(re.search(reg, s))  # возвращает месторасположение первого совпадения с шаблоном
# print(re.search(reg, s).span())  # (6, 16)
#
# print(re.search(reg, s).start())  # 6
# print(re.search(reg, s).end())  # 16
#
# print(re.search(reg, s).group())  # совпадения

# print(re.match(reg, s))  # возвращает месторасположение совпадения с шаблоном, но только вначале строки
# print(re.split(reg, s))  # возвращает список, в котором строка разбита по шаблону
#
# print(re.sub(reg, "!", s, 1))  # поиск и замена


# import re

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 198765 Hel_lo[-World] 2000010 002000"
# reg = r"[204]"
# reg = r"[0-4]"
# reg = r"[12][0-9][0-9][0-9]"
# reg = r"[А-яЁё]"
# reg = r"^\w+\s\w+"
# reg = r"\w+\s\w+$"
# print(re.findall(reg, s))

# print(ord('Ё'))
# print(ord('А'))
#
# print(ord('Я'))
# print(ord('а'))
#
# print(ord('я'))
# print(ord('ё'))

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15Е21:59. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# req = r"[0-2][0-9]:[0-5][0-9]"
# print(re.findall(req, st))

# d = "Цифры: 7, +17, --42, 0013, 0.3"
# print(re.findall(r"[+-]?\d+[.\d]*", d))

# st = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r"#.*", "", st))  # Дата рождения: 05.03.1987


# st = '05-03-1987 # Дата рождения'
# print('Дата рождения:', re.sub(r'\s#.*', '', st))
# # print('Дата рождения: ', re.sub(r'#.*', '', st).replace('-', '.'))
# print('Дата рождения:', re.sub('-', '.', re.sub(r'#.*', '', st)))

# st = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# req = r"\w+\s*=\s*[^;]+"
# print(re.findall(req, st))


# st = '05-03-1987 # Дата рождения'
# print('Дата рождения:', re.sub(r'-', '.', re.search(r'\d{2}-\d{2}-\d{4}', st).group()))
# print(re.search(r'\d{2}-\d{2}-\d{4}', st).group())


# st = "12 сентября 2021 года 235541541564156"
# req = r"\d{2,4}"
# print(re.findall(req, st))

# st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# req = r'\+?7\d*'
# print(re.findall(req, st))
#
# st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# req = r'\+?7\d{10}'
# print(re.findall(r"[+]?7\s?\d{3}\s?\d{3}-?\d{2}-?\d{2}", st))
# print(re.findall(req, st))

# def valid_login(name):
#     return re.findall(r"^[A-Za-z0-9_-]{6,16}$", name)  # 6-16,  англ. буквы, _, -, [0-9]
#
#
# print(valid_login("Python_master"))
# print(valid_login("Python@Python"))

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))
# print(re.findall(r"\w+", "12 + й", flags=re.A))
# print(re.findall(r"\w+", "12 + й", re.A))

# text = "hello world"
# # print(re.findall(r"\w+", text))
# print(re.findall(r"\w\+", text, re.DEBUG))

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r'я'
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one
# two
# """
# # print(re.findall(r'one.\w+', text))  # one\ntwo
# # print(re.findall(r'one.\w+', text, re.DOTALL))  # one\ntwo
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, re.MULTILINE))

# print(re.findall(r"""
# [a-z.-]+   # part 1
# @          # @
# [a-z.-]+   # part 2
# """, 'test@mail.ru', re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# reg = "(?mi)^python"
# print(re.findall(reg, text))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))
#
# # *?, +?, ??
# # {m,n}?, {,n}?, {m,}?
#
# st = "12 сентября 2021 года 235541541564156"
# req = r"\d{2,}?"
# print(re.findall(req, st))

# s = "<p>Изображение <img width='300' src  = 'bg.jpg' alt='картинка'> - фон страницы <img src  = 'bg.jpg' " \
#     "alt='картинка' width='300' ></p>"
# # reg = r'<img.*?>'
# reg = r"<img\s+[^>]*src\s*=\s*[^>]+>"
# print(re.findall(reg, s))


# text = "Python (в русском языке встречаются названия пито́н[16] или па́йтон[17]) — высокоуровневый язык " \
#        "программирования общего назначения с динамической строгой типизацией " \
#        "и автоматическим управлением памятью[18][19]."
#
# # print(re.findall(r'\[\d+]', text))
# print(re.findall(r'\[.*?]', text))

# s = "Петр, Ольга и Виталий отлично учатся!"
# # reg = 'Петр|Виктор|Ольга'
# # print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0, float, int"
# # reg = r'\w+\s*=\s*\d[.\w]*'
# # reg = r'int\s*=\s*\d[.\w]*|float\s*=\s*\d[.\w]*'
# # reg = r'(?:int|float)\s*=\s*\d[.\w]*'  # ['int = 4', 'float = 4.0f']
# # reg = r'((int|float)\s*=\s*(\d[.\w]*))'
# reg = r'(int|float)\s*=\s*\d[.\w]*'
# print(re.findall(reg, s))
# print(re.search(reg, s).group())

# (?:...) - эта группирующая скобка является не сохраняющей

# s = '127.0.0.1'
# # s = '127.168.255.255'
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(\d{1,3}.){3}\d{1,3}'
#
# print(re.findall(reg, s))
# print(re.search(reg, s).group())

# s = "5 + 7*2 - 4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# a = '01-12-2021'
# pattern = '(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(pattern, a))
# print(re.search(pattern, a).group())

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r'([0-9]+)\s(\D+)'  # ['2024 году. И я их найду в', '2024', 'году. И я их найду в']
# print(re.findall(reg, s))
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))


# s = "<p>Изображение <img src=\"bg.jpg\"> - фон страницы </p>"
# # reg = r"<img\s+[^>]*src\s*=(['\"])(.+?)\1>"
# reg = r"<img\s+[^>]*src\s*=(?P<q>['\"])(.+?)(?P=q)>"
# print(re.findall(reg, s))

# (?P<name>...)  (?P=name)

# s = "Самолет прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024."  # 23.10.2024
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))

# s = "yandex.com and yandex.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\2", s, re.IGNORECASE))

# Рекурсия

# def elevator(n):  # 0
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)  # 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = int(input("На каком Вы этаже: "))  # 5
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):  # [9]
#     if len(lst) == 1:
#         print(lst, "=> lst[0]", lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, "=> lst[0]", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7 +
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# def to_str(n, base):  # n = 15
#     convert = "0123456789ABCDEF"
#     if n < base:  # 15 < 16
#         return convert[n]  # convert[15] => 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # convert[14] => 'E'
#
#
# print(to_str(254, 16))
# print(to_str(18, 2))
# print(to_str(18, 8))
# print(to_str(18, 16))


# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(names)
#
#
# # print(names[0])
# # print(isinstance(names[0], list))
# # print(names[1])
# # print(isinstance(names[1], list))
# # print(names[1][1])
# # print(isinstance(names[1][1], list))
# # print(names[1][1][0])
# # print(isinstance(names[1][1][0], list))
# def count_item(lst):
#     count = 0
#     for item in lst:
#         if isinstance(item, list):
#             count += count_item(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_item(names))

# def remove(text):  # ""
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":  # False or True => True
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])  # 'HelloWorld'
#
#
# print(remove(" Hello\tWorld "))

# Файлы

# Текстовые
# Бинарные

# f = open(r'D:\Python313\313\test.txt', 'r')  # , mode='r'
# f = open('test.txt', 'r')
# print(*f)
# print(f)
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)


# f = open('test.txt', 'r')
# print(f.read(3))
# print(f.read())  # считываем файл полностью
# f.close()


# f = open('test1.txt', 'r')
# print(f.readline())  # считали одну строку из файла
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()


# f = open('test1.txt', 'r')
# # print(f.readlines(16))  # считали все данные из файла и вернули список строк
# print(f.readlines())
# f.close()


# f = open('test1.txt', 'r')
# count = 0
# for line in f:
#     print(line)
#     count += 1
# f.close()
# print("count =", count)


# f = open('test1.txt', 'r')
# print(len(f.readlines()))
# f.close()

# f = open("xyz.txt", "w")
# f.write("Hello\nWorld!\n")
# f.close()

# f = open("xyz.txt", "a")
# f.write("New text.\n")
# f.close()

# f = open("xyz.txt", "w")
# line = ['This is line 1\n', 'This is line 2\n']
# f.writelines(line)
# f.close()

# def negative_numbers(a):  # []
#     if not a:
#         return 0
#     else:
#         count = negative_numbers(a[1:])  #
#         if a[0] < 0:
#             count += 1  # 3
#         return count
#
#
# lst = [-2, 3, 8, -11, -4, 6, -7, -3]
# print(negative_numbers(lst))


# def negative_number(n):
#     if not n:
#         return 0
#     count = 0
#     if n[0] < 0:
#         count += 1
#     return count + negative_number(n[1:])
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(negative_number(lst))

# f = open('xyz.txt', 'w')
# lst = [str(i) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + "\t")
# f.close()

# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# f.close()

# f = open("text2.txt", "r")
# rl = f.readlines()  # ['Замена строки в текстовом файле;\n', 'изменить строку в списке;\n', 'записать список в файл;\n']
# f.close()
#
# print(rl)
# rl[1] = "Hello World\n"
# print(rl)  # ['Замена строки в текстовом файле;\n', 'Hello World\n', 'записать список в файл;\n']
#
# f = open("text2.txt", "w")
# f.writelines(rl)
# f.close()


# filename = "text2.txt"
# f = open(filename, "r")
# rl = f.readlines()
# f.close()
#
# print(rl)
#
# pos = int(input("Введите индекс строки для удаления: "))
# if 0 <= pos < len(rl):
#     rl.pop(pos)
# else:
#     print("Индекс введен неверно")
#
# print(rl)
#
# f = open(filename, "w")
# f.writelines(rl)
# f.close()

# source = 'text2.txt'
#
#
# def input_index():
#     file = open(source, 'r')
#     read_text = file.readlines()
#     file.close()
#     index = int(input('Введите номер строки: '))
#     if index not in range(len(read_text)) or index < 1:
#         print('Убедитесь что введен корректный номер строки и повторите попытку')
#         input_index()
#     else:
#         return read_text, index - 1
#
#
# t, i = input_index()
#
# f = open(source, 'w')
# del t[i]
# f.writelines(t)
# f.close()


# with open("filename.txt", "w") as f:
#     f.write("Замена строки в текстовом файле;\nИзменить строку в списке;\nЗаписать список в файл\n")
#
# with open("filename.txt", "r") as f1:
#     lines = f1.readlines()
# while True:
#     index_to_remove = int(input("Введите индекс строки для удаления: "))
#     if 0 <= index_to_remove < len(lines):
#         lines.pop(index_to_remove)
#         break
#
# with open("filename.txt", "w") as f:
#     f.writelines(lines)

# def input_index():
#     file = open('text2.txt', 'r')
#     read_text = file.readlines()
#     file.close()
#     index = int(input('Введите номер строки: '))
#     if index not in range(1, len(read_text) + 1) or index < 1:
#         print('Убедитесь что введен корректный номер строки и повторите попытку.')
#         return input_index()
#     else:
#         return read_text, index - 1
#
#
# t, i = input_index()
#
# f = open('text2.txt', 'w')
# del t[i]
# f.writelines(t)
# f.close()

# f = open("test.txt", "r")
# print(f.read(3))
# print(f.tell())  # возвращает текущую позицию уловного курсора в файле
# print(f.seek(1))  # переместил условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open("test.txt", "a+")
# print(f.write("I am learning Python"))
# print(f.tell())
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()

# with open("test.txt", "w+") as f:
#     print(f.write('01234\n56789'))
#
# with open("test.txt", "r") as f:
#     for line in f:
#         print(line[:3])

# file_name = "res_1.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return " ".join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))  # '[4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]'
#
# with open(file_name, "r") as f:
#     nums = f.read()
#
# print(nums)  # "4.5 2.8 3.9 1.0 0.3 4.33 7.777"
#
# nums_list = list(map(float, nums.split()))
# print(nums_list)
# print(sum(nums_list))
# print(len(nums_list))
# print("Done!")

# def longest_worlds(file):
#     with open(file, 'r') as text:  # , encoding="utf-8"
#         w = text.read().split()
#         max_length = len(max(w, key=len))  # длина самого длинного слова
#         print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_worlds('words.txt'))

# one = 'one.txt'
# two = 'two.txt'
# # text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# #
# # with open(one, "w") as f:
# #     f.write(text)
#
# with open(one, 'r') as fr, open(two, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)

# Модуль OS и OS.PATH

# import os
# import os.path


# print(os.getcwd())  # путь к текущей директории
#
# print(os.listdir())  # список директорий и файлов
#
# print(os.listdir(".."))

# os.mkdir("folder1")  # создание папки

# os.makedirs("nested1/nested2/nested3")  # создание папки с промежуточными директориями

# os.rmdir("folder1")  # удаление папки

# os.remove("xyz.txt")  # удаление файла

# os.remove("folder/test.txt")
# os.rmdir("folder")

# os.rename("nested1", "test")  # переименовали папку

# os.rename("words.txt", "test/words_new.txt")  # переименовали файл и переместили в заданную директорию

# os.renames("two.txt", "folder/file.txt")  # переименовали файл и переместили в заданную директорию, при этом может
# создать промежуточные директории

# for root, dirs, files in os.walk('test', topdown=False):
#     print("Root:", root)
#     print("Subdirs:", dirs)
#     print("Files:", files)

# os.mkdir('Test_folder')
# for i in range(1, 4):
#     with open(f'file{i}.txt', 'w') as file:
#         ...
# os.mkdir('Test_folder/Inner_test_folder1')
# for i in range(4, 9):
#     with open(f'Test_folder/Inner_test_folder1/file{i}.txt', 'w') as file:
#         ...
# os.mkdir('Test_folder/Inner_test_folder2')
# for i in range(9, 15):
#     with open(f'Test_folder/Inner_test_folder2/file{i}.txt', 'w') as file:
#         ...

# for root, dirs, files in os.walk('Test_folder', topdown=False):
#     print("Root:", root)
#     print("Subdirs:", dirs)
#     print("Files:", files)

# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 50)
#
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена")
#
#     print("-" * 50)
#
#
# remove_empty_dirs("test")
#
#
# print(os.listdir("test/folder1"))


# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 50)
#
#     for root, dirs, files in os.walk(root_tree, topdown=False):
#         os.rmdir(root)
#         print(f"Директория {root} удалена")
#
#     print("-" * 50)
#
#
# remove_empty_dirs("test")

# print(os.path.split(r"D:\Python313\313\test\nested2\nested3\words_new.txt"))
# print(os.path.dirname(r"D:\Python313\313\test\nested2\nested3\words_new.txt"))
# print(os.path.basename(r"D:\Python313\313\test\nested2\nested3\words_new.txt"))
#
# print(os.path.join('313', r'D:\Python313', 'test', 'words_new.txt'))

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         open(file_path, "w").close()

# files_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
# for file in files_with_text:
#     with open(file, "w") as f:
#         f.write(f"Какой-то текст для файла расположенного по пути: {file}")


# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f212.txt

# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print("-" * 50)
#
#
# print_tree("Work", False)
# print_tree("Work", True)

# print(os.path.exists(r"D:\Python313\313\test\nested2\nested3\words_new.txt"))  # проверяет существование пути

# print(os.path.isfile(r"D:\Python313\313\test\nested2\nested3\words_new.txt"))  # проверяет, что указанный путь
# # является правильным путем к файлу
#
# print(os.path.isdir(r"D:\Python313\313\test\nested2\nested3"))  # проверяет, что указанный путь
# является правильным путем к папке

# import time

# path = 'main.py'
# # print(os.path.getsize(path))  # возвращает размер файла в байтах (FileNotFoundError)
# # print(os.path.getsize(path) // 1024)  # размер в килобайтах
#
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getatime(path))))  # возвращает время последнего
# # доступа к файлу (в секундах)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getctime(path))))  # возвращает время создание файла
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getmtime(path))))  # возвращает время последнего
# изменения файла


# file_path = r"test\nested2\nested3\text21.txt"
#
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     print(f"{name} ({dirs}) - последний доступ к файлу: {os.path.getatime(file_path)}")
# else:
#     print(f"Файл {file_path} не существует")
# try:
#     dirs, name = os.path.split(file_path)
#     print(f"{name} ({dirs}) - ") # последний доступ к файлу: {os.path.getatime(file_path)}")
# except FileNotFoundError:
#     print(f"Файл {file_path} не существует")

# print(os.path.getatime(file_path))

# import os
#
# dir_name = 'test'
# objs = os.listdir(dir_name)
# print(objs)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     # print(p)
#     if os.path.isfile(p):
#         print(f"{obj} - file - {os.path.getsize(p)} bytes")
#     elif os.path.isdir(p):
#         print(f"{obj} - dir")

# OOP

# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 24
# print(p1.x)
# print(p1.y)
# print(p1.__dict__)
# print(id(p1))
#
# p2 = Point()
# p2.x = 10
# print(p2.x)
# print(p2.y)
# print(p2.__dict__)
# print(id(p2))
#
# print(id(Point))
#
# print(isinstance(p1, Point))
# print(isinstance(p2, Point))

# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):  # def set_coord(p2):
#         self.x = x  # p2.x = 10
#         self.y = y  # p2.y = 30
#         print(self.__dict__)  # print(p2.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 24
# p1.set_coord(5, 24)
# Point.set_coord(p1, 5, 24)
#
# p2 = Point()
# # p2.x = 10
# # p2.y = 30
# p2.set_coord(10, 30)


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.city = city
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.address = address
#
#     def set_address(self, address):  # устанавливаем адрес
#         self.address = address
#
#     def get_address(self):  # получаем адрес
#         return self.address
#
#     def set_name(self, name):  # устанавливаем имя
#         self.name = name
#
#     def get_name(self):  # получаем имя
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_address("ул. Ленина, 56")
# print(h1.get_address())
# h1.set_name("Юлия")
# print(h1.get_name())


# class Person:
#     skill = 10  # статическое свойство
#     count = 0  # 2
#
#     def __init__(self, name, surname):
#         self.name = name  # динамическое свойства
#         self.surname = surname
#         # print("Инициализатор класса", self)
#         Person.count += 1
#
#     # def __del__(self):
#     #     print("Удаление экземпляра", self)
#     #
#     # def print_info(self):
#     #     print("Данные сотрудника:", self.name, self.surname)
#     #
#     # def add_skill(self, k):
#     #     self.skill += k
#     #     print("Квалификация сотрудника:", self.skill, end="\n\n")
#
#
# p1 = Person("Виктор", "Резник")
# # p1.print_info()
# # p1.add_skill(3)
# # del p1
# # p1 = 5
#
#
# p2 = Person("Анна", "Долгих")
# # p2.print_info()
# # p2.add_skill(2)
#
# p3 = Person("Анна", "Долгих")
# print(p2.count)
#
# print(Person.count)
# print(p1.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#
#     def __del__(self):
#         print(self.name, "выключается!")
#
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid3 = Robot('HP-2PO')
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
# del droid1
# del droid2
# del droid3
#
# print("Численность роботов:", Robot.k)

# class Point:
#     __slots__ = ("__x", "__y", "z")
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         # self.x = x
#         # self.y = y
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def get_coord(self):  # получить
#         return self.__x, self.__y
#
#     def set_coord(self, x, y):  # установить
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата", x, "должна быть числом")
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координата", y, "должна быть числом")
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# p1.set_x(20.6)
# p1.set_y(30.4)
# print(Point.__check_value(8))
# print(p1.get_coord())
# p1.set_coord(100, 200)
# print(p1.get_coord())
# p1.__x = 100
# p1.y = "abc"
# print(p1.x, p1.y)
# print(p1.get_x())
# print(p1.get_y())
# print(p1.__dict__)
# print(Point.__dict__)
# print(p1._Point__x)
# p1._Point__x = "asd"
# print(p1.__dict__)

#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __get_x(self):
#         return self.__x
#
#     def __get_y(self):
#         return self.__y
#
#     def __set_x(self, x):
#         self.__x = x
#
#     def __set_y(self, y):
#         self.__y = y
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# # print(p1.get_x())
# # print(Point.__dict__)
# p1.x = 100
# print(p1.x)
# del p1.x
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if not isinstance(x, (int, float)):
#             raise TypeError("Устанавливаемое значение должно быть числом")
#             # print("Устанавливаемое значение должно быть числом")
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     def __get_y(self):
#         return self.__y
#
#     def __set_y(self, y):
#         self.__y = y
#
#     # x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# # print(p1.get_x())
# # print(Point.__dict__)
# p1.x = 100
# print(p1.x)
# # del p1.x
# print(p1.__dict__)


# class KgToPounds:
#
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#     def print_data(self):
#         print(self.kg, "кг => ", end="")
#         print(self.to_pounds(), "фунтов")
#
#
# weight = KgToPounds(12)
# weight.print_data()
# weight.kg = 41
# weight.print_data()
# weight.kg = "десять"
# weight.print_data()


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())
# print(p2.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))

# class Tools:
#     @staticmethod
#     def maximum(*my_list):
#         return max(my_list)
#
#     @staticmethod
#     def minimum(my_list):
#         return min(my_list)
#
#     @staticmethod
#     def middle(my_list):
#         return sum(my_list) / len(my_list)  # среднее арифметическое
#
#     # @staticmethod
#     # def factorial(number):
#     #     if number == 1:
#     #         return 1
#     #     else:
#     #         return Tools.factorial(number - 1) * number
#
#     @staticmethod
#     def factorial(number):
#         fact = 1
#         for i in range(1, number + 1):
#             fact *= i
#         return fact
#
#
# print(f'Максимальное число: {Tools.maximum(3, 5, 7, 9)}')
# print(f'Минимум число: {Tools.minimum([3, 5, 7, 9])}')
# print(f'Среднее арифметическое: {Tools.middle([3, 5, 7, 9])}')
# print(f'Факториал числа {5}: {Tools.factorial(5)}')

# from geometry import sqrt
#
#
# class Square:
#     __count = 0
#
#     @staticmethod
#     def square_triangle1(a, b, c):
#         Square.__count += 1
#         p = (a + b + c) / 2
#         return sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def square_triangle2(a, b):
#         Square.__count += 1
#         return 0.5 * a * b
#
#     @staticmethod
#     def square_area(a):
#         Square.__count += 1
#         return a * a
#
#     @staticmethod
#     def square_rectangle(a, b):
#         Square.__count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Square.__count
#
#     def print_info(self):
#         print(self, "Hello")
#
#
# area = Square()
# area.print_info()
# area1 = Square()
# Square.print_info(area1)
# print('Площадь треугольника по формуле Герона:', area1.square_triangle1(3, 4, 5))
# print('Площадь треугольника через основание и высоту:', Square.square_triangle2(6, 7))
# print('Площадь квадрата:', Square.square_area(7))
# print('Площадь прямоугольника:', Square.square_rectangle(2, 6))
# print('Количество подсчетов площади:', Square.get_count())

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day  # 23
#         self.month = month  # 10
#         self.year = year  # 2024
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))  # 23 10 2024
#         date1 = cls(day, month, year)   # date1 = Date(23, 10, 2024)
#         return date1  # Date(23, 10, 2024)
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     '30.12.2023',
#     '30-12-2020',
#     '01.01.2024',
#     '12.31.2020'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         print(date.string_to_db())
#     else:
#         print("Неправильная дата или формат строки с датой")


# date2 = Date.from_string("23.10.2024")  # date2 = Date(23, 10, 2024)
# print(date2.string_to_db())
# date3 = Date.from_string("25.12.2023")
# print(date3.string_to_db())

# string_date = "23.10.2024"
# day, month, year = map(int, string_date.split("."))
# day, month, year = 23, 10, 2024
# print(day, month, year)  # 23 10 2024
# date = Date(day, month, year)
# print(date.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         uer_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счёта: {uer_val} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снять!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print('Информация о счете:')
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_eur()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_percent()
# print()
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
#
# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         # ['В', 'о', 'л', 'к', 'о', 'в', 'И', 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
#         # letters = "".join(re.findall("[a-zа-яё-]", fio, re.IGNORECASE))  # ВолковИгорьНиколаевич
#         # for s in f:
#         #     if len(s.strip(letters)) != 0:
#         #         raise TypeError("В ФИО можно использовать только буквы и дефис")
#         # for s in f:
#         if re.findall(r'[^a-zа-яё\s-]', fio, re.IGNORECASE):
#             raise ValueError('Ошибка')
#
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or not 14 < old < 120:  # old < 14 or old > 120
#             raise TypeError("Возраст должен быть целым числом в диапазоне от 14 до 120 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#
# p1 = UserData("Волков Игорь Николаевич", 96, "1234 567890", 80.8)
# p1.fio = "Волков Игорь Викторович"
# print(p1.fio)
# p1.old = 26
# print(p1.old)
# p1.weight = 90.5
# print(p1.weight)
# p1.password = "9876 543210"
# print(p1.password)


# class Point:  # class Point(object):
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#
# print(issubclass(Point, object))
# print(issubclass(Point, int))


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#         print("Инициализатор базового класса Prop")
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         super().__init__(*args)
#         # Prop.__init__(self, *args)
#         print("Переопределенный инициализатор Line")
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")


# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")


# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
# print(line.get_width())

# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()

# DRY (Don't Repeat Yourself) - не повторяйся!!!


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         self.width = width
#         self.height = height
#         super().__init__(color)
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Некорректное значение ширины")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Некорректное значение высоты")
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольника = ", end="")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# # rect.width = 90
# print(rect.area())


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целочисленными значениями")
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.set_coord(Point(15, 45), Point(100, 200))
# line.draw_line()
#
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.set_coord(Point(55.5, 45.6), Point(100, 200))
# rect.draw_rect()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, size, frame, color):
#         super().__init__(width, height)
#         self.size = size
#         self.frame = frame
#         self.color = color
#
#     def show_rect(self):
#         super().show_rect()
#         # print(f'Толщина линий: {self.size}\nРамка: {self.frame}\nЦвет: {self.color}')
#         print(f'Рамка: {self.size} {self.frame} {self.color}')
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px", "solid", "red")
# shape2.show_rect()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f'Прямоугольник:\nширина {self.width}\nВысота {self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.background = background
#
#     def show_rect_with_background(self):
#         print(f'Прямоугольник с фоном {self.background}:\nширина {self.width}\nВысота {self.height}')
#
#
# shapel = RectFon(400, 200, "yellow")
# shapel.show_rect_with_background()

# class Vector(list):
#     # def __init__(self, lst):
#     #     super().__init__()
#     #     self.lst = lst
#
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(sum(v))
# print(v)
# print(type(v))


# Перегрузка методов

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp=None, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Координата sp должна быть целочисленным значением")
#         if sp is None:
#             if ep.is_int():
#                 self._ep = ep
#             else:
#                 print("Координата ep должна быть целочисленным значением")
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целочисленными значениями")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
# line.set_coord(Point(15, 45), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(55, 55))
# line.draw_line()
# line.set_coord(ep=Point(90, 20))
# line.draw_line()


# Абстрактные методы

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#     ...
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()

# Абстрактные классы

# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):  # Абстрактный класс
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     # def move(self):
#     #     super().move()
#     #     print("Ферзь перемещен на e2e4")
#     pass
#
#
# # q = Chess()
# q = Queen()
# q.draw()
# # q.move()

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#     def show(self):
#         print(f"= {self.convert_to_rub():.2f} RUB")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=' ')
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#
#
# # d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# n = Dollar(20)
# n.print_value()
# n.show()
# # print(Dollar.__dict__)
#
# d += e
# for elem in e:
#     elem.print_value()
#     # print(f"= {elem.convert_to_rub():.2f} RUB")
#     elem.show()

# for elem in e:
# elem.print_value()
# elem.show()


# Интерфейсы

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild")
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()

# def outer():
#     a = 5
#
#     def inner():
#         b = 10
#         print(a)
#
#     inner()
#     print(b)
#
#
# outer()


# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def static_method():
#         print("Статический метод")
#
#     def outer_method(self):
#         print("Метод в наружном классе")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Вложенный класс", MyOuter.age, self.obj.name)
#             MyOuter.static_method()
#             self.obj.outer_method()
#
#
# out = MyOuter('внешний')
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light Green"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# # outer.lg.display()
# g = outer.lg
# g.display()
# class Intern:
#     def __init__(self):
#         self.name = "Smith"
#
#     def display(self):
#         print("Name:", self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = "Alba"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Employee()
# outer.show()
# d1 = outer.intern
# d1.display()
# d2 = outer.head
# d2.display()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("Outer")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Inner")
#
#         class InnerClass:
#
#             def show(self):
#                 print("InnerClass")
#
#
# outer = Outer()
# outer.show()
#
# # inner1 = outer.inner
# # inner1.show()
#
# # inner2 = inner1.inner_inner
# inner2 = outer.inner.inner_inner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         # self.os = self.OS()
#         # self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# comp = Computer()
# # my_os = comp.os
# # my_cpu = comp.cpu
# my_os = Computer.OS()
# my_cpu = Computer.CPU()
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = [Cat("Пушок")]
# # cat = Cat("Пушок")
# print(cat)

# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(1, 2, 3)
# print(len(p))

# import geometry
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = geometry.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p = Point(1, 2)
# print(p.length)
# p.length = 20
# print(p.length)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt1 = Point(1, 2)
# pt2 = Point2D(1, 2)
# print("pt1 =", pt1.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())

# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z',
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt1 = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# print(pt3.x, pt3.y, pt3.z)


# Множественное наследования

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is player")
#
#
# class Dog(Animal, Pet):
#
#     def bark(self):
#         print(self.name + " is barking")
#
#
# dog = Dog("Buddy")
# dog.bark()
# dog.play()
# dog.sleep()


# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#     def hi(self):
#         print("A")
#
#
# class AA:
#     def __init__(self):
#         print("Инициализатор класса АA")
#
#     def hi(self):
#         print("AA")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#     # def hi(self):
#     #     print("B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#     # def hi(self):
#     #     print("C")
#
#
# class D(B, C):
#     def __init__(self):
#         C.__init__(self)
#         B.__init__(self)
#         print("Инициализатор класса D")
#
#
# d = D()
# d.hi()
# print(D.mro())
# print(D.__mro__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#
# class Pos(A):
#     def __init__(self, sp: Point, ep: Point, color="red", width=1):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         Styles.__init__(self, color, width)
#         # super().__init__(color, width)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()
# print(Line.mro())


# Миксины

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="sublog.txt")
#
#
# subclass = MySubClass()
# subclass.display("Строка будет отображаться и запишется в файл")


# class Goods:
#     def __init__(self, name, weight, price):
#         print("Инициализатор Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#         super().__init__()
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Инициализатор MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
#
# n2 = NoteBook("HP", 1.5, 35000)
# n2.save_sell_log()


# Перегрузка операторов
# 24 * 60 * 60 = 86400 - число секунд в одном дне

# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __lt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('правый операнд должен быть типом Clock')
#         return self.sec < other.sec
#
#     def __le__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('правый операнд должен быть типом Clock')
#         return self.sec <= other.sec
#
#     def __gt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('правый операнд должен быть типом Clock')
#         return self.sec > other.sec
#
#     def __ge__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('правый операнд должен быть типом Clock')
#         return self.sec >= other.sec
#
#     # def __getitem__(self, item):
#     #     if not isinstance(item, str):
#     #         raise ValueError("Ключ должен быть строкой")
#     #
#     #     if item == "hour":
#     #         return (self.sec // 3600) % 24
#     #     if item == "min":
#     #         return (self.sec // 60) % 60
#     #     if item == "sec":
#     #         return self.sec % 60
#     #
#     #     return "Неверный ключ"
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError('Ключ должен быть строкой')
#         hour_, min_, sec_ = self.get_format_time().split(':')
#         time_key = {
#             'hour': hour_,
#             'min': min_,
#             'sec': sec_,
#         }
#         try:
#             return time_key[item]
#         except KeyError:
#             return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         if key == "min":
#             self.sec = s + 60 * value + h * 3600
#         if key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# # c2 = Clock(100)
# print(c1.get_format_time())
# print(c1["hour"], c1["min"], c1["sec"])
# c1["hour"] = 11
# c1["min"] = 25
# c1["sec"] = 50
# print(c1["hour"], c1["min"], c1["sec"])
# print(c1.get_format_time())
# print(c2.get_format_time())
#
# print(f'c1 < c2: { c1 < c2}')
# print(f'c2 > c1: { c2 > c1}')
# print(f'c1 >= c2: { c1 >= c2}')
# print(f'c2 <= c1: { c2 <= c1}')
# c1 = Clock(100)
# c2 = Clock(200)
# # c4 = Clock(300)
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c4.get_format_time())
# c3 = c1 + c2 + c4
# print(c3.get_format_time())
# c2 += c1
# print(c2.get_format_time())
# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")

# if c1 != c2:
#     print("Время разное")
# else:
#     print("Время равно")


# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)  # [5, 5, 3, 4, 5]
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # 10 + 1 - 5 = 6
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         if key not in range(len(self.marks)):
#             raise IndexError('Индекс за пределами')
#         del self.marks[key]
#
#
# s1 = Student("Сергей", 5, 5, 3, 4, 5)
# # print(s1.name)
# # print(s1.marks[2])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)

# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(['M', 'F'])) for _ in range(randint(1, 5))]  # range(0, 1)
#         else:
#             raise TypeError("Type are not supports!")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# cat3 = Cat("Murzik", 4, "M")
# print(cat1)
# print(cat2)
# # print(cat3)
# print(cat1 + cat2)

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())

# class Point3D:
#     RIGHT = "Правый операнд должен быть типом Point3D"
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f"{self.x}, {self.y}, {self.z}"
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
#
#     def __eq__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return self.x == other.x and self.y == other.y and self.z == other.z
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         elif item == 'x':
#             return self.x
#         elif item == 'y':
#             return self.y
#         elif item == 'z':
#             return self.z
#         else:
#             print("Неверный ключ")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if key == 'x':
#             self.x = value
#         elif key == 'y':
#             self.y = value
#         elif key == 'z':
#             self.z = value
#         else:
#             print("Неверный ключ")
#
#
# pt1 = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# # pt2 = Point3D(12, 15, 18)
# print("Координаты 1-й точки:", pt1)
# print("Координаты 2-й точки:", pt2)
# pt3 = pt1 + pt2
# print(f"Сложение координат: ({pt3})")
# print(f"Равенство координат: {pt1 == pt2}")
#
# print(f"x1 = {pt1['x']}, x2 = {pt2['x']}")
# print(f"y1 = {pt1['y']}, y2 = {pt2['y']}")
# print(f"z1 = {pt1['z']}, x2 = {pt2['z']}")
#
# pt1['x'] = 20
# pt2['y'] = 20
# pt2['z'] = 20
# print()
# print(f"x1 = {pt1['x']}, x2 = {pt2['x']}")
# print(f"y1 = {pt1['y']}, y2 = {pt2['y']}")
# print(f"z1 = {pt1['z']}, z2 = {pt2['z']}")


# Функторы

# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c2 = Counter()
# c2()
#
# c1()

# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(self.__chars)
#
#
# s1 = StripChars("?:!.; ")
# print(s1(" Hello World!!!! "))
#
#
# def strip_chars(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#
#     return wrap
#
#
# s2 = strip_chars("?:!.; ")
# print(s2(" Hello World!!!! "))


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print("Перед вызовом функции")
#         self.func()
#         print("После вызова функции")
#
#
# @MyDecorator
# def function():
#     print("Текст функции")
#
#
# function()


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, x, y):
#         return f"Перед вызовом функции\n{self.func(x, y)}\nПосле вызова функции"
#
#
# @MyDecorator
# def function(a, b):
#     return a * b
#
#
# print(function(2, 5))


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, x, y):
#         return self.func(x, y) ** 2
#
#
# @Power
# def my_func(a, b):
#     return a * b
#
#
# print(my_func(2, 3))


# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             return f"Перед вызовом функции ({self.name})\n{func(*args, **kwargs)}\nПосле вызова функции"
#
#         return wrap
#
#
# @MyDecorator("два параметра")
# def function(a, b):
#     return a * b
#
#
# @MyDecorator("три параметра")
# def function1(a, b, c):
#     return a * b * c
#
#
# print(function(2, 5))
# print(function1(2, 5, 2))


# class Power:
#     def __init__(self, num):
#         self.num = num
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             return f'Результат: {func(*args, **kwargs) ** self.num}\n'
#
#         return wrap
#
#
# @Power(2)
# def my_func(a, b):
#     return a * b
#
#
# print(my_func(2, 2))


# class Power:
#     def __init__(self, num):
#         if not isinstance(num, int):
#             raise ValueError('Степень должна быть целым положительным числом')
#         self.num = num
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             return f'Результат: {func(*args, **kwargs) ** self.num}\n'
#
#         return wrap
#
#
# @Power(3)
# def function(a, b):
#     return a * b
#
#
# print(function(2, 2))

# Декорирование методов

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()

# def decorator(arg):
#     class Wrapper(arg):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Инициализатор ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))


# Дескрипторы  (__get__, __set__, __delete__, __set_name__)

# class String:
#     def __init__(self, value=None):
#         print(f"Инициализатор String: {value}")
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{value} должно быть строкой")
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     if not isinstance(value, str):
#     #         raise ValueError(f"{value} должно быть строкой")
#     #     else:
#     #         self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     if not isinstance(value, str):
#     #         raise ValueError(f"{value} должно быть строкой")
#     #     else:
#     #         self.__surname = value
#
#
# p = Person("Ivan", "Petrov")
# p.surname.set(54)

# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Ivan", "Petrov")
# p.surname = 5
# print(p.name)
# print(p.surname)
# print(p.__dict__)


# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f"Координата {coord} должно быть целым числом")
#
#     def __set_name__(self, owner, name):
#         self.__name = "coord_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.__name]
#         return getattr(instance, self.__name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.__name] = value
#         setattr(instance, self.__name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# p1.x = 20
# print(p1.x)
# print(p1.__dict__)


# Метаклассы

# a = 5
# print(type(a))
# print(type(int))


# class MyList(list):
#     def get_length(self):
#         return len(self)
#
#
# lst = MyList()
# lst.append(5)
# lst.append(8)
# print(lst, lst.get_length())
#
#
# MyList1 = type(
#     "MyList1",
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
# lst1 = MyList1()
# lst1.append(5)
# lst1.append(8)
# print(lst1, lst1.get_length())
#
# print(MyList.__dict__)
# print(MyList1.__dict__)

# import geometry.rect
# import geometry.sq
# import geometry.trian

# from geometry import rect, sq, trian
#
#
# # import geometry  # работать не будет
# # from geometry import *
#
# def run():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == '__main__':
#     run()

# from car.electrocar import ElectroCar
#
# e_car = ElectroCar("Tesla", "T", 2018, 99000)
# e_car.show_car()
# e_car.description_battery()

class PayrollSystem:
    def calculate(self, employees):
        print("Расчет заработной платы:")
        print("=" * 50)
        for employee in employees:
            print(f"Заработная плата: {employee.id} - {employee.name}")
            print(f"- Проверить сумму: {employee.calculate_payroll()}")
            print()


class Employee:
    def __init__(self, id_employee, name):
        self.id = id_employee
        self.name = name


class SalaryEmployee(Employee):
    """Административные работники, с фиксированной зарплатой"""

    def __init__(self, id_employee, name, weekly_salary):
        super().__init__(id_employee, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    """Сотрудники с почасовой оплатой"""

    def __init__(self, id_employee, name, hours_worked, hour_rate):
        super().__init__(id_employee, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
payroll_system = PayrollSystem()
payroll_system.calculate([
    salary_employee,
    hourly_employee
])
