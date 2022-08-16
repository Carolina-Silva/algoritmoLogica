lista = []
for i in range(100):
    n = int(input())
    lista.append(n)
maior_n = max(lista)
pos_n = lista.index(maior_n) +1
print(maior_n) 
print(pos_n)