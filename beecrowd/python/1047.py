hi,mi,hf,mf =map(int,input().split(" "))
ht = hf - hi
if ht < 0 :
    ht += 24
mt = mf - mi
if mt < 0 :
    mt += 60
    ht -= 1
    if ht < 0:
        ht += 24
if mt == 0 and ht == 0:
    ht = 24
print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(ht,mt))