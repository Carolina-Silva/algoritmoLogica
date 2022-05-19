x, y = map(int,input().split(" "))
codi = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}
total = codi[x]*y
print("Total: R$ %.2f" % total)