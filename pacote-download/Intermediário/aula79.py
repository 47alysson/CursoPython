# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add (letra.lower()) #converte para minúsculo

    if 'l' in letras:
        print('Parabéns')
        break
    print(letras)
