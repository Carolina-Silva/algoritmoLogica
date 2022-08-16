X1, Y1 = map(float,input().split(" "))
X2, Y2 = map(float,input().split(" "))
D = pow(pow(X2-X1,2) + pow(Y2-Y1,2),1/2)
print("%.4f" % D )