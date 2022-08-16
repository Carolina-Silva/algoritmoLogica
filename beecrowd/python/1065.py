con = 0
nPares = 0
while (con < 5):
    n = float(input())
    if n%2==0:
        nPares = nPares+1
    con = con+1
print("%i valores pares" % nPares)