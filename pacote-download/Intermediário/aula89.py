# dir, hasattr e getattr em python
string = 'Alysson'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
    print(string)