# 1-topshiriq

# class Avto:
#     def __init__(self, model, nomi, rangi, narxi, yili):
#         self.model = model
#         self.nomi = nomi
#         self.rangi = rangi
#         self.narxi = narxi
#         self.yili = yili

#     def info(self):
#         return f"{self.model} kompaniyasining {self.rangi} {self.nomi} avtomobili {self.yili}-yili {self.narxi} so'mga baholandi "
    

# avto1 = Avto("Chevrolrt","malibu",'qora',120_000_000,2020)
# avto2 = Avto("Hummer", "H2",'sariq',150_000_000,20219)
# print(avto1.info(),'\n',avto2.info())


# 2-topshiriq
class Avtosalon:
    def __init__(self, model, nomi, rangi, narxi, yili):
        self.model = model
        self.nomi = nomi
        self.rangi = rangi
        self.narxi = narxi
        self.yili = yili

    def info(self):
        return f"{self.model} kompaniyasining {self.rangi}rangli {self.nomi} avtomobili {self.yili}-yili chiqqan {self.narxi} so'm li bo'lishi kerak "

model = input("Kompaniya nomini kiriting = ")
nomi = input("Mashina nomini kiriting = ")
rangi = input("Mashina rangini kiritng = ")
narxi = int(input("Narxi qancha = "))
yili = int(input("Yili nechchi = "))

avto1 = Avtosalon(model, nomi, rangi, narxi, yili)

print(avto1.info())