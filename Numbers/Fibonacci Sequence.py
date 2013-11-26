def fib(n):
    '''
    find the nth fibonacci number
    '''
    if n == 1 or n == 0:
        return n
    else:
        return fib(n-1) + fib(n-2)