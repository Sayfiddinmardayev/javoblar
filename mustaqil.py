# bu yerda bitta matn nechta marta takrorlanganini aniqlab beradigan dastur
# from collections import Counter
# count_words = lambda text: dict(Counter(text.split()))
# text = input(">>>")
# result = count_words(text)
# print(result)


# bu yerdxa ro'yxatdagi sonlani toq va juft larga ajratib beradigan dastur
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# grouped_numbers = {
#     'even': list(filter(lambda x: x % 2 == 0, numbers)),
#     'odd': list(filter(lambda x: x % 2 != 0, numbers))
# }
# print(grouped_numbers)

# bu yerda n ta fibonachi sonlarni chiqaradigan dastur
# import functools
# n = int(input("n ga qiymat kiriting = "))
# # Lambda funksiyasi yordamida fibonacci sonlar ro'yxatini hosil qilish
# fibonacci = lambda x: functools.reduce(lambda acc, _: acc + [acc[-1] + acc[-2]], range(x-2), [0, 1])
# fibonacci_sequence = fibonacci(n)
# print(fibonacci_sequence)


# fruits = ["olma", "banan", "anor", "shaftoli"]
# n = lambda x: sorted(x)
# sorted_fruits = n(fruits)
# upper_fruits = list(map(str.upper, sorted_fruits))
# print(upper_fruits)

# 1-usul
# m = lambda x : x % 2 == 0
# print(m(int(input(">>> "))))

# 2-usul
# Juft sonni tekshirish
# is_even = lambda x: x % 2 == 0
# Toq sonni tekshirish
# is_odd = lambda x: x % 2 != 0
# Foydalanuvchidan son kiritish
# number = int(input("Sonni kiriting: "))
# Natijani chop etish
# print(f"{number} juft: {is_even(number)}")
# print(f"{number} toq: {is_odd(number)}")



# n = int(input("son kiriting = "))
# kv = lambda x: x*x
# print(f"{n} ning kvadrati = {kv(n)}")


# n = [15, 84, -15, -84, 56]
# m = list(filter(lambda x: x > 0, n))
# print(m)


# import math
# a = lambda x, y: max(x,y)
# print(a(87,4))


# words = ["or","ekvador", "kema", "ilk","akvarium"]
# a = lambda x: len(x)
# # So'zlar ro'yxatini tartiblang
# sorted_words = sorted(words)

# # Lambda funksiyasi so'z uzunligini hisoblash uchun
# modified_lengths = list(map(a, sorted_words))
# # map funksiyasini qo'llab, lambda funksiyasini har bir so'zga qo'llash
# print(sorted_words)


# x = lambda a: '_'.join(reversed(a))
# print(x("Sayfiddin"))


# people = [
#     {'name': "Ali", 'age': 17},
#     {'name': "Bilol", 'age': 19},
#     {'name': "Qodir", 'age': 25},
#     {'name': "Jalol", 'age': 15}
# ]
# # Lambda funksiyasi yoshni 18 dan kattaligi bo'yicha tekshirish uchun
# a = lambda y: y['age'] > 18
# # Filtrlangan odamlarni chiqarish
# x = list(filter(a, people))
# print("18 dan katta", x)


# list1 = [1,2,3]
# list2 = [4,3,2]
# list3 = lambda a,b: a + b
# add = list(map(list3,list1,list2))
# print(add)


# year = int(input("Yil kiriting >>> "))
# a = lambda x:(x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)  
# if a(year):
#     print("kabisa")
# else:
#     print("kabisa emas")


# names = input(("So'z kiritng >>> "))
# words = names.split()
# # words = ["or","ekvador", "kema", "ilk","akvarium","va"]
# a = lambda x: len(x)
# # So'zlar ro'yxatini tartiblang
# sorted_words = sorted(words, key=lambda x: x[1])
# # Lambda funksiyasi so'z uzunligini hisoblash uchun
# modified_lengths = list(map(a, sorted_words))
# # map funksiyasini qo'llab, lambda funksiyasini har bir so'zga qo'llash
# print(sorted_words)


# number = int(input("Son kiriting >>> "))
# a = lambda x: x**0.5
# print(a(number))


# fruits = ["olma", "banan", "anor", "shaftoli","nok"]
# n = filter(lambda x: len(x) == 4, fruits)
# result = list(n) 
# print(result)


# import math
# a = lambda x, y: min(x,y)
# print(a(87,4))




# def juft(x):
#     return x % 2 == 0

# def toq(y):
#     return y % 2 != 0

# juft_sonlar = list(filter(juft, sonlar))
# print(sonlar)
# print("Juft sonlar = ",juft_sonlar)
# toq_sonlar = list(filter(toq, sonlar))
# print("Toq sonlar = ",toq_sonlar)

# i = 0
# while i < 5:
#     print(i, end = ' ')
#     i += 1
#     if i == 3:
#         break
# else:
#     print(0)
# output:0 1 2


# while True: print(eval(input(">>> ")))


# y = int(input("y = "))
# for i in range(y):
#     for j in range(y - i - 1):
#         print(" ", end=" ")
#     for k in range(i * 2 + 1):
#         print("$", end=" ")
#     print()


# while True:
#     a = input("Birinchi so'zni kiriting = ")
#     b = a[len(a)-1]
#     c = input(b + " harfiga so'z kiriting = ")
#     print(b)
#     if c[0] == b:
#         print("to'g'ri")
#         print(a, end=' ' + c)
#     else:
#         print("noto'g'ri")
    

# import time, random
# from itertools import cycle

# cars = "nexia = ","damas = ","tiko = "
# c = random.choice(cars)
# nums = 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1

# for i in range(10):
#     n = random.choice(nums)
#     m = [(c + "" + str(n), n)]
#     r = cycle(m)
#     x, y = next(r)
#     print(x)
#     time.sleep(y)
# print("finish") 


# bu yerda o'zimiz qo'lda txt fayl yaratdik va ichiga ham ma'lumot yozdik
# file_name = 'test'
# big_num = None

# try:
#     with open("test.txt", 'r') as f:
#         for line in f:
#             numbers_str = line.split(',')
#             for num_str in numbers_str:
#                 try:
#                     son = int(num_str.strip())
#                     if big_num is None or son > big_num:
#                         big_num = son
#                 except ValueError:
#                     pass
# except FileNotFoundError:
#     print(f"file topilmadi {file_name}")
# if big_num is not None:
#     print(f"fayl ichidagi eng katta son: {big_num}")
# else:
#     print("Fayl ichida sonlar mavjud emas yoki fayl bo'sh")



# def count_letters(file_name):
#     count = 0
#     letters = []
#     with open("mustaqil.txt", 'r') as f:
#         words = f.read().split()
#         for word in words:
#             if len(word) == 2:
#                 count += 1
#                 letters.append(word)
#     return count, letters

# file_name = input("Fayl nomini kiriting = ")
# n, add = count_letters(file_name)
# print(f"Faylda {n} ta ikki harfli so'z bor")

# for word in add:
#     res = []
#     res.append(word)
#     print(res, end=" ")


# def my():
#     """
#     salom

#     """
# print(my.__doc__)

# arab raqamidan rim raqamiga o'tkazib beradi
# def arabic_to_roman(num):
#     val = [
#         1000, 900, 500, 400,
#         100, 90, 50, 40,
#         10, 9, 5, 4,
#         1
#         ]
#     syms = [
#         "M", "CM", "D", "CD",
#         "C", "XC", "L", "XL",
#         "X", "IX", "V", "IV",
#         "I"
#         ]
#     roman_num = ''
#     i = 0
#     while num > 0:
#         for _ in range(num // val[i]):
#             roman_num += syms[i]
#             num -= val[i]
#         i += 1
#     return roman_num

# # Example usage
# arabic_number = int(input("Enter an Arabic number: "))
# print(f"The Roman numeral for {arabic_number} is {arabic_to_roman(arabic_number)}")

# from mpmath import mp

# # Pi sonini kerakli darajada aniqlikda olish uchun
# mp.dps = 100000  # Bu misolda 100000 raqamni olish uchun (zarur bo'lsa ko'proq raqam qo'yishingiz mumkin)
# pi_str = str(mp.pi)

# # Pi sonining dastlabki 100 raqamini chop etish
# print(pi_str[:101])  # 3 va nuqta ham hisobga olinadi


# --------------------------erghtyhjm----------------------------------

# x = [1, 2, 3, "a","i", "e", "b",  "w", '!', "@", "u", "&", "😶", "(❁´◡`❁)"]
 
# vowels_set = ["a", "e", "o", "u", "i"]
# consonants_set = ["b", "w",  "c"]
# numbers_set = '1234567890'

# vowels = []
# consonants = []
# symbols = []
# numbers = []

# for i in x.copy():
#     q = str(i)
#     if i in vowels_set:
#         a = vowels.append(q)
#         x.remove(i)
#     if i in consonants_set:
#         consonants.append(i)
#         b = x.remove(i)
#     if str(q) in numbers_set:
#         l = x.index(i)
#         t = x.pop(l)
#         numbers.append(t)
# print("vowels", vowels)
# print("consonants", consonants)
# print("numbers", numbers)
# print("symbol", x)


# a = input(">>> ").split()
# kv = (lambda i: i >= 0, a)
# print(kv)

# ----------------------------lknbhgmn-------------------------------------------------------