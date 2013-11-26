def countVowels(word):
    '''
    takes in a string
    returns the amount of vowels and the sum of the place in the alphabet
    '''
    word.lower()
    vowelList = ['a','e','i','o','u']
    vowelNumber = {'a':1,'e':5,'i':9,'o':15,'u':21}
    vowels = 0
    vowelWorth = 0
    for i in word:
        if i in vowelList:
            vowels += 1
            vowelWorth += vowelNumber.get(i)
    return (vowels,vowelWorth)
    
word = raw_input('Please enter a string: ')
print countVowels(word)