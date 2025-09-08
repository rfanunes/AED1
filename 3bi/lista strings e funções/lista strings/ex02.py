#Crie uma função `estatisticas_texto(texto)` que receba uma string e retorne uma lista com:
#- número de palavras,
#- número de caracteres,
#- tamanho médio das palavras,
#- a palavra mais longa.
#Exemplo:
#Entrada: "Python é divertido"
#Saída:
#[['palavras', 'caracteres', 'tamanho_medio', 'mais_longa'], [3, 17, 5.6, 'divertido'}]]

entrada = 'python é divertido'.lower().split()
lista = [['palavras', 'caracteres', 'tamanho_medio', 'mais_longa']]
def estatisticas_texto(texto):
    i = 0 #indice começa no 0
    carac = 0 #carac começa no 0
    mais_longa = ''
    quant_palavra = len(texto) #a quantidade de palavras na lista eh igual o len
    for i in texto: #pra cada palavra do texto
        carac += len(i) #aumenta o caracteres
        if len(i) > len(mais_longa): #se o numero da palavra for maior que o numero da mais longa
            mais_longa = i #substitui
        tamanho_medio = round(carac / quant_palavra, 2) #faz a conta pro tamanho medio
    lista.append([quant_palavra, carac, tamanho_medio, mais_longa]) #add tudo na lista
    return lista #retorna a lista
print(estatisticas_texto(entrada))  