#try, except, else e finaly

try:
    print('Abrir arquivo')
    #8/0

except ZeroDivisionError:
    print('Dividiu zero')

else:
    print('Não deu erro')
finally:
    print('Fechar arquivo')
    