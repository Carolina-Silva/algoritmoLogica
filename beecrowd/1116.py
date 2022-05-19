n = int(input())
cont = 0
while cont < n:
    x, y = map(float,input().split(" "))
    if y != 0:
        v= x/y
        print(v)
    else:
        print("divisao impossivel")
    cont += 1