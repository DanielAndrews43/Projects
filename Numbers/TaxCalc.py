def taxCost(cost, tax):
    '''
    cost = float cost of item
    tax = float tax % (AKA if its 7.5% enter 7.5)
    
    returns a duple with first item being the new cost and the second being tax
    paid
    '''
    tax = tax / float(100) * cost
    newCost = (cost + tax,tax)
    return newCost
    