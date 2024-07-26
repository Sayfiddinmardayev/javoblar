def studentInfo(FISH, Yunalishi, Fakultet, Universitet, Tyili ,  Kurs = None):
    student = {'Familiya ism sharifi': FISH,
            "Yo'nalishi": Yunalishi,
            'Fakulteti': Fakultet,
            'Universiteti': Universitet,
            "Tug'ulgan yili": Tyili ,
            'Kursi':  Kurs}
    return student

def talaba_kirit():
    students = []
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting:")
        FISH = input("Familiya ism sharifi: ")
        Yunalishi = input("Yo'nalishi: ")
        Fakultet = input("Fakulteti: ")
        Universitet = input("Universiteti: ")
        Tyili = input("Tug'ulgan yili: ")
        Kurs = int(input("Kursi: "))
        students.append(studentInfo(FISH, Yunalishi, Fakultet, Universitet, Tyili,Kurs))

        javob = input("Yana talaba qo'shasizmi? (yes/no)")
        if javob == "no":
            break
    return students

def yigish():
    davlatlar = []
    while True:
        davlat = {}
        davlat['nomi'] = input("Davlat nomi: ")
        davlat['poytaxti'] = input("Poytaxti: ")
        davlat['aholisi'] = input("Aholisi: ")
        davlat['maydoni'] = input("Maydoni (kvadrat kilometrda): ")
        davlatlar.append(davlat)
        
        yana = input("Yana  davlat qo'shmoqchimisiz? (yes/no): ")
        if yana.lower() != 'yes':
            break
    return davlatlar

def kvadratini_hisoblovchi(number):
    powers = {}
    for i in range(2, 11):
        powers[i] = number ** i
    return powers



# def info_cars(autoInfo):
#     print(f"{autoInfo['kompaniya'].title()}, "
#     f"{autoInfo['model'].title()}, "
#     f"{autoInfo['rangi'].title()}, "
#     f"{autoInfo['korobka']}, "
#     f"{autoInfo['yili']}-yil, $ {autoInfo['narxi']}")

def daraja_hisoblovchi(a, b):
    return a ** b

def ildiz(a):
    return a ** (1/2)

def kv(a):
    return a ** 2

def kub(a):
    return a ** 3

# def kv_kub(a):
    # return f"{a ** 2} - {a ** 3}"

