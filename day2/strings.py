def countVowels(word):
    # list storing standard vowels known
    list = ['a','e','i','o','u']

    # list to store vowels from original word
    vowels = []

    # list to store letters of word already checked
    checked = []

    counter = 0
    
    # looping through the original word
    for letter in word:
        if not letter in checked:
            # getting vowels in word
            if (letter in list):
                vowels.append(letter)
            
            # getting count for duplicated letters
            i = word.count(letter)
            if (i > 1):
                counter = counter + 1

        checked.append(letter)
    
    str1 = ''.join(vowels)
    tuplex = str1, counter
    print(tuplex)

countVowels('dahdah')
countVowels('drink water')       
