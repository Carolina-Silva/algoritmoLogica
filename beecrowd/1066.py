i = 0
par = 0
imp = 0
pos = 0
neg = 0
for i in range(5,0,-1):
    n = int(input())
    if n%2 == 0:
        par += 1
    if n%2 != 0:
        imp += 1
    if n > 0:
        pos += 1
    if n < 0:
        neg += 1
print("%i valor(es) par(es)" %par)
print("%i valor(es) impar(es)" %imp)
print("%i valor(es) positivo(s)" %pos)
print("%i valor(es) negativo(s)" %neg)