#soal 1
limit = int(input("Masukkan batas bilangan: "))
if limit % 2 == 0:
    print(f"{limit} adalah bilangan genap")

else:
    print(f"{limit} adalah bilangan ganjil")


#soal 2
def Sn(Un):
    i = 0
    out = 0
    while i <= Un: 
        out = out + i
        i += 1
    print(f"Sn dari Un dan b=1 adalah: {out}")

Sn(limit)


#soal 3
angka = int(input("Masukkan angka"))
tabel = int(input("Tabel perkalian"))

def tabelX(a,b):
    i = 1
    out = 0
    while i <= tabel:
        out = angka * i
        print(f"{angka} x {i} = {out}")
        i = i +1

tabelX(angka,tabel)