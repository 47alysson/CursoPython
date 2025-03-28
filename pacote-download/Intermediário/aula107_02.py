# Considerando duas listas de inteiros ou floats (lista A e lista B)
# Some os valores nas listas retornando uma nova lista com os valores somados:

# se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.
    
# Exemplo:
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

# Resultado:
# lista_soma = [2,4,6,8]

lista_soma = list((zip(lista_a, lista_b)))

lista_soma1 = [x +y for x, y in lista_soma]

lista_soma2 = map(sum,lista_soma)

print(lista_soma1, list(lista_soma2))
