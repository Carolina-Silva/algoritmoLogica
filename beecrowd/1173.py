n = int(input())
v = [0]*10
for i in range(len(v)):
    v[i] = n
    n = n * 2
    print("N[%i] = %i" %(i,v[i]))