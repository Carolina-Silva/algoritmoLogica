def lerMatriz(l, c):
    m = [0]*l
    for i in range(len(m)):
        m[i] = [0]*c
        for j in range(len(m[i])):
            m[i][j]= int(input)
    return m
def media(m):
    s = 0
    qtElem = 0
    for i in range(len(m)):
        for j in range(lem(m[i])):
            s = s + m[i][j]
            qdElem = qtElem + 1
    return s/ qtElem
def acimaMedia(matriz,media):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > media:
                print(matriz[i][j])
def main():
    m1 = lerMatriz(2,3)
    media1 = media(m1)
    acimaMedia = (m1,media1)
    m2 = lerMatriz(2,4)
    media2 = media(m2)
    acimaMedia = (m2,media2)
    
main()