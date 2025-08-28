def calc(operasi, a, b):
    c = 0
    if operasi == "+":
        c = a+b
    elif operasi == "-":
        c = a-b
    elif operasi == "*":
        c = a*b
    elif operasi == "**":
        c = a**b
    elif operasi == "/":
        c = a/b
    elif operasi == "%":
        c = a%b
        
    print(c)

calc("*", 5, 6)

def segitiga(tinggi):
    for i in range(1, tinggi+1):
        print("*" * i)


segitiga(5)


def segwhile(a):
    i = 1
    while i <= a:
        print("*" * i)
        i += 1

segwhile(5)

print()

def segbalik(a):
    for i in range(a, 0, -1):
        print("*" * i)

segbalik(5)

for o in range(1, 9):
    print(" "* (9-o) + "*" * (2*o-1))
