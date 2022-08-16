clas1 = str(input())
if clas1 == "vertebrado":
    clas2 = str(input())
    if clas2 == "ave":
        clas3 = str(input())
        if clas3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else: 
        clas3 = str(input())
        if clas3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    clas2 = str(input())
    if clas2 == "inseto":
        clas3 = str(input())
        if clas3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else: 
        clas3 = str(input())
        if clas3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")