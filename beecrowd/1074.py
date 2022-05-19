conta = 0
casos = int(input())
while conta < casos:
    n = int(input())
    if n%2 ==0 and n > 0:
        print("EVEN POSITIVE")
    elif n%2==1 and n>0:
        print("ODD POSITIVE")
    elif n%2==1 and n<0:
        print("ODD NEGATIVE")
    elif n%2 ==0 and n < 0:
        print("EVEN NEGATIVE")
    elif n == 0:
        print("NULL")
    conta +=1