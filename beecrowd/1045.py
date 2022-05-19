a, b, c = map(float,input().split(" "))
lista = [a,b,c]
lista.sort(reverse=True)
a = lista[0]
b = lista[1]
c = lista[2]
if a>=b+c:
    print("NAO FORMA TRIANGULO")
else:
    if a*a == b*b + c*c:
        print("TRIANGULO RETANGULO")
    elif a*a > b*b + c*c:
        print("TRIANGULO OBTUSANGULO")
    elif a*a < b*b + c*c:
        print("TRIANGULO ACUTANGULO")
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or c == a:
        print("TRIANGULO ISOSCELES")