# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas em ordem.
# Use todos os valores da menor lista.
# Ex:
# ['Salvador','Ubatuba','Belo horizonte']
# ['BA','SP','MG','RJ']
# Resultado
# [('Salvador', 'BA'),('Ubatuba', 'SP'),('Belo Horizonte', 'MG')]

# def zipper(l1,l2):
#     intervalo = min(len(l1),len(l2))
#     return[(l1[i], l2[i]) for i in range(intervalo)]

from itertools import zip_longest

l1= ['Salvador','Ubatuba','Belo horizonte']
l2= ['BA','SP','MG','RJ']

print(list(zip(l1,l2)))
print(list(zip_longest(l1,l2,fillvalue= 'Sem cidade')))
