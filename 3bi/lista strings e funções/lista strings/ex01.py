#Exercício 01

#Implemente uma função recursiva `eh_palindromo(texto)` que receba uma string e retorne
#`True` se for palíndromo (desconsiderando espaços, acentos e diferenças entre
#maiúsculas/minúsculas) e `False` caso contrário.
#Exemplo:
#Entrada: "Socorram-me subi no onibus em Marrocos"
#Saída: True

'''

#SEM RECURSÃO


entrada = 'socorram me subi no onibus em marrocos'.lower().replace(" ", "")

nova_frase = ''

def eh_palindromo(texto):
    letra_invertida = texto[::-1] #a letra invertida é a frase sendo invertida
    nova_frase = letra_invertida #a letra invertida começa a contatenar
    if nova_frase == texto: #se a nova frase for igual ao texto
        return True #palindromo
    else: 
        return False #nao é palindromo
print(eh_palindromo(entrada))

'''

#COM RECURSÃO

entrada = 'socorram me subi no onibus em marrocos'.lower().replace(" ", "")

def eh_palindromo(texto):
    if len(texto) <= 1: #se o texto tiver 0 ou 1 letras, ja eh palindromo auto
        return True #retorna palindromo
    if texto[0] != texto[-1]: #texto[0] eh a primeira letra da string, e o [-1] eh o ultima letra (se for diferente)
        return False #retorna falso, nao eh palindromo
    return eh_palindromo(texto[1:-1]) #se chegou aq, eh pq a primeira letra e a ultima sao IGUAIS
#agr ignoramos as duas letras e repete com o "MIOLO" da string, ou seja, pega do segundo caract até o penultimo
#ex: ovo
# 'o' e 'o' sao iguais
#pega o miolo da string, ou seja 'v'
#agora entra na função, 'v' = 1 (soh tem um valor), ou seja, eh palindromo!
#ele compara AS PONTAS
print(eh_palindromo(entrada))
