sal = float(input())
if sal >= 0.00 and sal<=400.00:
    per = sal * 0.15
    sal = sal + per
    por = "15"
elif sal>= 400.01 and sal<= 800.00: 
    per = sal * 0.12
    sal = sal + per
    por = "12"
elif sal>= 800.01 and sal<= 1200.00:
    per = sal * 0.10
    sal = sal + per
    por = "10"
elif sal>= 1200.01 and sal<= 2000.00:
    per = sal * 0.07
    sal = sal + per
    por = "7"
elif sal > 2000.00:
    per = sal * 0.04
    sal = sal + per
    por = "4"
print("Novo salario: %.2f" %sal)
print("Reajuste ganho: %.2f" %per)
print("Em percentual: %s %%" %por)