con = 0
nPositivo = 0
while (con < 6):
    n = float(input())
    if n>0:
        nPositivo = nPositivo+1
    con = con+1
print("%i valores positivos" % nPositivo)