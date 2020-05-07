lista = ['arroz', 'feijão', 'carne']

for i in lista:
    print(i)

for num, item in enumerate(lista):
    print("{} está na posição {}".format(item,num))    




############## break ##################
lista = ["java","C","C++","php","ruby","python","go"]


for i in lista:
    if i == "python":
        print("Parou!")
        break
    else: 
        print(i," Ainda não")





############ Continue ##################
servidores = ["cassandradb", "dremio", "mongodb", "redis","ldap","web","proxy","mysql"]  

# O continue trata uma exeção em uma lista

for i in servidores:
    if i == "web":
        print("Esta atualização não pode ser executada no {}".format(i))
        continue
    print("Servidor %s atualizado!"%i)