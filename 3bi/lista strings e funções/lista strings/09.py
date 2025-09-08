entrada = "Programacao".upper()

def vogais_unicas(texto):
    vogais = ['A','E','I','O','U'] #lista de vogais
    saida = '' #onde vou contatenar
    for i in texto: #percorre cada letra do texto
        if i in vogais and i not in saida: #se a letra estiver na lista das vogais E nao estiver ainda na saida
            saida += i #contatena a letra
    return len(saida) #retorna o valor de saida
print(vogais_unicas(entrada))