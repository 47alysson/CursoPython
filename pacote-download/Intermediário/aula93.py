# Try, except, else e finally

try:
    a = 18
    b = 0
    #print(b[0])
    #print('Linha 1'[1000])
    c = a / b    
    print('Linha 2')
except ZeroDivisionError as e:
    print('Dividiu por zero')
    print(e.__class__.__name__)
except NameError:
    print('Erro de nome')
except (TypeError,IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:',error)
    print('Nome:',error.__class__.__name__)
except Exception:
    print('Erro desconhecido')

print('Continuar')