import random

print("Пограємо у гру!")
x=random.randrange(1, 151, 1)
j=0

for i in range(6):
    y = int(input("Введіть число від 1 до 150: "))
    if y>x and i!=5:
        print("Число має бути меншим")
    elif y<x and 1!=5:
        print("Число має бути більшим")
    elif y == x:
        print(f"Ви перемогли з {i+1} разу! :)")
        j=1
        break

if j!=1:
    print(f"Це було число {x}. Ви програли :( . Спробуйте наступного разу.")

def test_function(file):
    dct={}

    for l in dt:
        kk=l.rstrip("\n")
        kl = kk.rsplit(":")
        k = kl[0]
        v = kl[1]
        dct.update({k:v})
    dt.close()
    return dct