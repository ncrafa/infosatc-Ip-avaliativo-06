
algumaCoisa=0
lista = [10,11,12,13]
def rotacion(lista, numero):
    algumaCoisa =int(input("insira um número positivo/negativo:"))
    if algumaCoisa >=0:
        for i in range(algumaCoisa):
            numeraDireita = lista.pop(-1)
            lista.insert(0, numeraDireita)
    else:
        for i in range(abs(algumaCoisa)):
            numeroEsquerda = lista.pop(0)
            lista.append(numeroEsquerda)
            return
rotacion(lista, algumaCoisa)
print (lista) 
    

