def reverseString(oldStr):
    '''
    returns a reversed string
    '''
    return oldStr[::-1]
    
reverse = raw_input('Please enter a string: ')
print reverseString(reverse)