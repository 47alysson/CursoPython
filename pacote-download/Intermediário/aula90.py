import sys
# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #tem __iter__ e __next__
generator = (n for n in range (100)) #com ()
lista = [n for n in range (100)] #com []

print (sys.getsizeof(generator))
print(sys.getsizeof(lista))

for n in generator:
    print(n)
    