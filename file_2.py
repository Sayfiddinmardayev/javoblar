# 1-topshiriq
# i = 1
# filenomi = 'teachers.txt'
# with open('teachers.txt', 'w') as f:
    
#     while i <= 5:
#         a = f.write(input(f"{i}  F.I.O kiriting = ")+'\n',)
#         if i != 5:
#             i += 1
#             continue
#         elif i ==  5:
#             break
    
    
# with open(filenomi, 'r') as f:
#     b = f.read()
#     print(b)

# 2-topshiriq
# import pickle

# a = (input("F.I.O kiriting = ")+'\n')
# b = (input("Manzilini kiriting = ")+'\n')

# with open('student', 'wb') as f:
#     pickle.dump(a, f)
#     pickle.dump(b, f)
# with open('student', 'rb') as f:
#     Name = pickle.load(f)
#     Address = pickle.load(f)

# print(Name)
# print(Address)

# 3-topshiriq
# from mpmath import mp

# pi_str = str(mp.pi)

# def tkun_in_pi(tkun):
#     """Bu funksiya tug'ilgan kunning pi tarkibida mavjud yoki yo'qligini tekshiradi."""
#     return tkun in pi_str

# # Misol uchun tug'ilgan kuningizni kiritishingiz kerak
# tkun = (input("Tug'ulgan kuningizni kiritng = "))

# if tkun_in_pi(tkun):
#     print("Tug'ilgan kuningiz pi soni tarkibida mavjud.")
# else:
#     print("Tug'ilgan kuningiz pi soni tarkibida mavjud emas.")


# 4-topshiriq
# filenomi = "new_file.txt"
# with open(filenomi, 'w+') as f:
# # with open('new_file.txt', 'w') as f:
#     f.write("Mardayev Sayfiddin\n")
#     f.write('0950')
    
    
# filenomi = "new_file.txt"
# with open(filenomi, 'a') as f:
#     b = input("matn kiriting >>> ")
#     f.write('\n'+b)
#     f.write('\nsalom')
#     f.write('\nxayr')
#     f.write('\nAssalom')

# with open('new_file.txt','r') as f:
#     a = f.read()
#     print(a)
