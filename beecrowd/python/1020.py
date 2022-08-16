n = int(input())
a = n // 365
n = n % 365
m = n // 30
n = n % 30
d = n // 1
print("%i ano(s)" %a)
print("%i mes(es)" %m)
print("%i dia(s)" %d)