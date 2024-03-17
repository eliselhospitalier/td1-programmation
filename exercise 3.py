#exercise 3



def score(word): #returns the score of word
    
    #dictionary with each letter's score
    alphabet = {'a':1, 'e':1, 'i':1, 'l':1, 'n':1, 'o':1, 'r':1, 's':1, 't':1, 'u':1, 'd':2, 'g':2, 'm':2, 'b':3, 'c':3, 'p':3, 'f':4, 'h':4, 'v':4, 'j':8, 'q':8, 'k':10, 'w':10, 'x':10, 'y':10, 'z':10}
    
    score = 0
    for letter in word:
        score += alphabet[letter]
    return score


def max_word(list_of_words):  #returns the word with the highest score
    maxi = score(list_of_words[0])
    max_word = list_of_words[0]
    for word in list_of_words:
        if score(word) > maxi:
            maxi = score(word)
            max_word = word
    return max_word


def best_word(letters):  #searchs the best possible word with these letters
    #begining is the same as exercise 2
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
    
    #instead of looking for the longest word, we search the highest scoring one
    return max_word(possible_words), score(max_word(possible_words))

        