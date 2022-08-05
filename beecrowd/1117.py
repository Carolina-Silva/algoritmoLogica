media = 0
conta = 0
total = 0
while conta < 2:
    n = float(input())
    if n >= 0 and n <= 10:
        total = total + n
        conta += 1
    else:
        print("nota invalida")
media = total/2
print("media = %.2f" %media)