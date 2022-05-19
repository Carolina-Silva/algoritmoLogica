n1, n2, n3, n4 = map(float,input().split(" "))
m = (n1*2 + n2*3 + n3*4 + n4*1)/10
print("Media: %.1f" % m)
if m>=7:
    print("Aluno aprovado.")
elif m<5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exa = float(input())
    mf = (exa+m)/2
    print("Nota do exame: %.1f" % exa)
    if mf>=5:
       print("Aluno aprovado.")
       print("Media final: %.1f" % mf)
    else:
        print("Aluno reprovado.")
        print("Media final: %.1f" % mf)