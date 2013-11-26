def checkPal(word):
    '''
    returns true if word is palindrome
    returns false otherwise
    '''
    word = word.lower()
    if word == word[::-1]:
        return True
    return False