f = [0,1,2,3,4]

'''
i = 0
while i < len(f):
    print(f[i])
    i+=1

for c in f:
    print(c)
'''

def fib(n):
    '''Print the fibonacci sequence'''
    a,b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

'''fib(10)'''

def func(foo, *args, **kwargs):
    print(args)
    print(args[0])
    print(kwargs['shop'])

func('foo', 1, 2, 3, shop='LIB')