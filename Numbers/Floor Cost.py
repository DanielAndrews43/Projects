def floorCost(width, height):
    '''
    width and height are both floats of feet^2
    cost is price per foot^2
    returns total cost
    '''
    cost = float(raw_input('Enter the cost per square foot: '))
    return 'The total cost is %d$'%(height*cost*width)