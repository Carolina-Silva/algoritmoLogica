f = open("demofile.txt", "r")
arquivo = f.readline()
while arquivo != "":
    print("Linha Original")
    print(arquivo)
    arquivo = f.readline()
f.close()

f = open("demofile.txt", "r")
arquivo = f.readline()
while arquivo != "":
    print("Linha Original")
    print(arquivo)
    arquivo = f.readline()
f.close()

f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

# Abrir arquivo para gravação
#ler e guardar 5 textos digitados
#fechar arqivo
#abrir para leitura
#mostrar todo contetudo
#fechar arquivo
