def fact(n):
    '''
    find the factorial of n
    '''
    if n == 1:
        return 1
    else:
        return n * fact(n-1)