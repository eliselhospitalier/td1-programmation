def longest_word(letters):
    #list containing every french word
    french_words = [] 
    f = open("frenchssaccent.dic", 'r')
    for ligne in f:
        french_words.append(ligne[0 : len(ligne)-1])
    f.close()
    
    #making a list with all possible words containing the letters
    possible_words = []
    for word in french_words:
        remaining_letters = []
        remaining_letters.extend(letters)
        test = True
        i = 0
        while test == True and i <= len(word)-1:
            if word[i] in remaining_letters:
                #removing one occurence of the letter within the remaining ones
                remaining_letters.remove(word[i])
            else:
                test = False
            i += 1
        if test == True:
            possible_words.append(word)
    
    #finding the longest word amonst all possible words
    if possible_words == []:
        return ('no possible words')
    else:
        longest_word = possible_words[0]
        max_length = len(longest_word)
        for word in possible_words:
            if len(word) > max_length:
                longest_word = word
                max_length = len(longest_word) 
        return longest_word
            
    
    