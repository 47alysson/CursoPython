# isinstance - para saber se objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0,1,2], (1,2), {0,1}, {'nome':'Alysson'},
]

for item in lista:
    if isinstance(item, set):
        print('Set')
        item.add(5)
        print(item,isinstance(item, set))

    elif isinstance(item, str):
        print('Str')
        print(item.upper())
    
    elif isinstance(item, (float,int)):
        print('Num')
        print(item *2)

    else:
        print('Outro')
        print(item)