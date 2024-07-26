from modul import kvadratini_hisoblovchi

son = int(input("Iltimos, son kiriting: "))
daraja = kvadratini_hisoblovchi(son)
        
for daraja, natija in daraja.items():
    print(f"{son} ning {daraja} - darajasi  = {natija}")
