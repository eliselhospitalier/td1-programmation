#exercise 4



def score(word): #returns the score of word
    
    #dictionary with each letter's score
    alphabet = {'a':1, 'e':1, 'i':1, 'l':1, 'n':1, 'o':1, 'r':1, 's':1, 't':1, 'u':1, 'd':2, 'g':2, 'm':2, 'b':3, 'c':3, 'p':3, 'f':4, 'h':4, 'v':4, 'j':8, 'q':8, 'k':10, 'w':10, 'x':10, 'y':10, 'z':10}
    
    score = 0
    for letter in word:
        if letter in alphabet:   #if the joker is used, its score is 0
            score += alphabet[letter]
    return score


def max_word(list_of_words):  #returns the word with the highest score and its index in the list
    maxi = score(list_of_words[0])
    max_word = list_of_words[0]
    index = 0
    for i in range(1, len(list_of_words)):
        if score(list_of_words[i]) > maxi:
            maxi = score(list_of_words[i])
            max_word = list_of_words[i]
            index = i
    return max_word, index


def best_word(letters):  #searchs the best possible word with these letters

    #list containing every french word
    french_words = [] 
    f = open("frenchssaccent.dic", 'r')
    for ligne in f:
        french_words.append(ligne[0 : len(ligne)-1])
    f.close()
    
    #chekcing that there is no more than one joker
    number_joker = 0
    for letter in letters:
        if letter == '?':
            number_joker += 1
    if number_joker > 1:
        return 'trop de jokers'
    
    
    #making a list with all possible words containing the letters
    possible_words = []
    possible_letters_used = []
    for word in french_words:
        remaining_letters = []
        remaining_letters.extend(letters)   #copy of the list letters
        used_letters = '' #letters that are actually used (including joker)
        test = True
        i = 0
        while test == True and i <= len(word)-1:
            if word[i] in remaining_letters:
                #removing one occurence of the letter within the remaining ones
                remaining_letters.remove(word[i])
                used_letters = used_letters + word[i]
            else:
                if '?' in remaining_letters:
                    remaining_letters.remove('?')
                    used_letters = used_letters + '?'
                else:
                    test = False
            i += 1
        if test == True:
            possible_words.append(word)  
            possible_letters_used.append(used_letters)
    
    #instead of looking for the longest word, we search the highest scoring one
    best, index = max_word(possible_letters_used) #the scores are calculated with the eventual joker
    return possible_words[index], score(best)