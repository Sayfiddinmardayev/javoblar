# class Fan:
#     def __init__(self,fan_nomi):
#         self.fan_nomi = fan_nomi

#     def teach(self):
#         return f"{self.fan_nomi} fanidan dars beriladi "

#     def exam(self):
#         return f"{self.fan_nomi} fanidan imtihon olinmoqda "

#     def homework(self):
#         return f"{self.fan_nomi} fanidan uyfa vazifa berildi "

# fan = Fan("Matematia")
# print(fan.teach())
# print(fan.exam())
# print(fan.homework())



# class Talaba:
#     def __init__(self, ism, yosh):
#         self.ism = ism  
#         self.yosh = yosh  

#     def get_info(self):
#         return f"{self.ism} {self.yosh} yoshda"
    
#     def set_info(self,ism,yosh):
#         self.ism = ism
#         self.yosh = yosh

#     def get_name(self):
#         return self.ism

#     def set_name(self, ism):
#         self.ism = ism

#     def get_age(self):
#         return self.yosh

#     def set_age(self, yosh):
#         self.yosh = yosh

#     def study(self):
#         return f"{self.ism} universitetda o'qiydi."

# talaba = Talaba("Ali", 21)
# print(talaba.get_info())
# talaba.set_info("Karim",22)
# print(talaba.get_info())
# print(talaba.get_name())
# talaba.set_name("Vali")
# print(talaba.get_name())
# print(talaba.study())


# class Odam:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         return f"Bu  {self.name}."

# class Muallim(Odam):
#     def uqituvchi(self):
#         return f"{self.name} - o'qituvchi."

# class Shifokor(Odam):
#     def shifokor(self):
#         return f"{self.name} - shifokor."

# 
# muallim = Muallim("Ozod")
# shifokor = Shifokor("Dilnoza")
# print(muallim.info())
# print(muallim.uqituvchi())
# print(shifokor.info())
# print(shifokor.shifokor())