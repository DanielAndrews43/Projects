def changeCalc(money):
    '''
    money = positive float
    
    returns least amount of coins to return
    [100s,50s,20s,10s,5s,1s,quarters,dimes,nickels,pennies]
    '''
    round(money,2)
    types = (100,50,20,10,5,1,.25,.1,.05,.01)
    amount = [0,0,0,0,0,0,0,0,0,0]
    if money <= 0:
        return
    for i in range(len(types)):
            startAmount = money
            money %= types[i]
            if money != startAmount:
                amount[i] = startAmount / types[i]
    print "Hundreds %d" % (amount[0])
    print "Fifties  %d"%(amount[1])
    print "Twenties %d"%(amount[2])
    print "Tens     %d"%(amount[3])
    print "Fives    %d"%(amount[4])
    print "Ones     %d"%(amount[5])
    print "Quarters %d"%(amount[6])
    print "Dimes    %d"%(amount[7])
    print "Nickels  %d"%(amount[8])
    print "Pennies  %d"%(amount[9])
