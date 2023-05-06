arquivo=open("palavra.txt","w")
arquivo.write("banana")
arquivo.write("melancia")
arquivo.close()
arquivo=open("palavra.txt","a")
arquivo.write("morango\n")
arquivo.write("manga\n")

arquivo=open("palavra.txt", "r")
arquivo.read()
linha= arquivo.readline()

for linha in arquivo:
    print(linha,end="\n")