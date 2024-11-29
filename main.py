

a = 1
b = 2
c =3
result = 0
if a != b and a!=c:
    result = result + a + b + c
elif a == b:
   print(c)
else:
   print(b)

mevalar = {'olma': 12000, 'banan': 25000, 'gilos': 20000, 'shaftoli': 16000, 'uzum': 23000}

eng_arzon_meva = min(mevalar, key=mevalar.get)
eng_arzon_narx = mevalar[eng_arzon_meva]

print(f"'{eng_arzon_meva}': {eng_arzon_narx}") 
for meva, narx in mevalar.items():
    print(f"{meva} - {narx}") 

ismlar = ['Akmal', 'Abror', 'Behruz', 'Husan', 'Xurshid']

yangi_dict = {ism: index + 1 for index, ism in enumerate(ismlar)}

print(yangi_dict)  

students = {'Akmal': 11, 'Abror': 9, 'Behruz': 13, 'Husan': 12, 'Xurshid': 10}


yoshlar = sorted(students.values())

print(", ".join(map(str, yoshlar))) 



