for i in range(0,3):
    print(f"Apel {i}")
    for j in range(0,3):
        print(f"Pisang {j}")
        for k in range(0,3):
            print(f"jeruk {k}")

for m in range(0,10):
    print(f"mangga {m}")
    if m > 2:
        break
print("selesai \n")
for n in range(0,10):
    if n % 2 == 0:
        continue
    print(f"anggur {n}")

