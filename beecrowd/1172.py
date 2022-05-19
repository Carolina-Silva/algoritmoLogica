x = [0]*10
for i in range(len(x)):
    x[i] = int(input())
i = 0
for i in range(len(x)):
    if x[i] <= 0:
        x[i] = 1
    print("X[%i] = %i" %(i,x[i]))