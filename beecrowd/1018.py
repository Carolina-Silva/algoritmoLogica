N = int(input())
print (N)
cem = N // 100
N = N % 100
cinq = N // 50
N = N % 50
vin = N // 20
N = N % 20
dez = N // 10
N = N % 10
cin = N // 5
N = N % 5
dois = N//2
N = N % 2
print("%i nota(s) de R$ 100,00" % cem)
print("%i nota(s) de R$ 50,00" % cinq)
print("%i nota(s) de R$ 20,00" % vin)
print("%i nota(s) de R$ 10,00" % dez)
print("%i nota(s) de R$ 5,00" % cin)
print("%i nota(s) de R$ 2,00" % dois)
print("%i nota(s) de R$ 1,00" % N)