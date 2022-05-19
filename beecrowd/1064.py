con = 0
nPositivo = 0
totalP =0
while (con < 6):
    n = float(input())
    if n>0:
        nPositivo = nPositivo+1
        totalP = totalP +n
    con = con+1
mP=totalP/nPositivo
print("%i valores positivos" % nPositivo)
print("%.1f" %mP)