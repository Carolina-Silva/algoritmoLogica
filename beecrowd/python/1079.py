i = 1
conta = int(input())
while i <= conta:
    a, b, c = map(float,input().split(" "))
    m = (a*2 + b*3 + c*5)/10
    print("%.1f" %m)
    i+=1