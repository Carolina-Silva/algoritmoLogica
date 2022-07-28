sal = float(input())
por28 = 0 
por18 = 0
por8 =0
if sal <= 2000.00:
    print("Isento")
else:
    if sal > 4500.00:         
        sob28 = sal - 4500.00
        sal -= sob28
        por28 = sob28 * 0.28
    if sal >= 3000.01:
        sob18 = sal - 3000.01
        sal -= sob18
        por18 = sob18 * 0.18
    if sal >= 2000.01:
        sob8 = sal - 2000.01
        sal -= sob8
        por8 = sob8 * 0.08
    por_total = por28 + por18 + por8 
    print("R$ %.2f" %por_total)