TB = input("Masukkan Tinggi Badan (dalam cm): ")
BB = input("Masukkan Berat Badan (dalam kg): ")
TB = float(TB)
BB = float(BB)
BMI = BB / ((TB / 100) ** 2)
print("Nilai BMI anda adalah: ", BMI)
if BMI < 18.5:
    print("Anda termasuk dalam kategori kekurangan berat badan")
elif 18.5 <= BMI < 24.9:
    print("Anda termasuk dalam kategori berat badan normal")
elif 25 <= BMI < 29.9:
    print("Anda termasuk dalam kategori kelebihan berat badan")
elif BMI >= 30:
    print("Anda termasuk dalam kategori obesitas")
