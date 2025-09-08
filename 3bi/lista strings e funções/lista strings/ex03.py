string = str(input("Digite algo aí: "))
n = int(input("Digite um número ai: "))


def cifrando(frase):
    variavel = '' #variavel vazia onde vou contatenar
    for i in frase: #percorre o indice(numero) da frase
        variavel += chr(ord(i) + n) #soma o indice (numero) do ord + o numero pra deslocamento
        #e transforma esse numero do ord pra letra, com o chr, e adiciona na variavel vazia
    return variavel #retorna a variavel
print(cifrando(string))