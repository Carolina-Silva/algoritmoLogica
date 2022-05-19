i, f = map(int,input().split(" "))
if i < f:
    duracao = f - i
else:
    duracao = (24-i)+f
print("O JOGO DUROU %i HORA(S)" %duracao)