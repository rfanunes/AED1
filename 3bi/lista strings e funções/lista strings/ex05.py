entrada = "banana uva abacaxi pera morango anseio".split()
#AAHAHAHAHAHAHHA

def ordenar_palavras(frase):
    ordenando = [] #vazio
    while frase: #enquanto a lista frase nao for vazio 
        mais_longa = frase[0] #pega a  primeira palavra da lista de frases E atualiza cada loop!
        for i in frase: #percorre cada palavra na lista de palavras 
            if len(i) > len(mais_longa): #se a palavra atual for maior que a variavel
                mais_longa = i #atualiza o mais_longa
            elif len(i) == len(mais_longa): #se ambas tiverem msm tamanho
                if mais_longa > i: #ve quem eh maior q a outra pela ordem alfabetica
                    mais_longa = i #dai atualiza
        ordenando.append(mais_longa) #coloca na lista a mais longa
        frase.remove(mais_longa) #remove da LISTA DE FRASE a mais longa
    return ordenando #retorna a lista
print(ordenar_palavras(entrada))

#obs: se nao usar o len, ele SEMPRE vai comparar strings em ordem alfabetica qnd usar apenas o i!
#obs2: teste de mesa feito 
