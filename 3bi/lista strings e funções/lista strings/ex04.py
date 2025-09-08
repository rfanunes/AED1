entrada = "abcabcbb"

def maior_substring_unica(texto):
    substring_atual = []
    maior_encontrada = [] 
    for i in texto: #vai passar cada letra na entrada 
            if i in substring_atual: #se a letra ja existir na lista
                substring_atual = [i] #reseta pq quero as strings unicas, PEGA A LETRA Q CAUSOU O RESET
            else: #se nao, adiciona  na lista
                 substring_atual.append(i)
            if len(substring_atual) > len(maior_encontrada): #se a lista da substring for maior q a lista da maior encontrada
                maior_encontrada = substring_atual #atualiza a lista 
    return maior_encontrada #retorna a lista
print(maior_substring_unica(entrada))