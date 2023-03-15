import random
# library used used to choose random words 
name = input("What is your name?")
# User's name will be taken 
print ("Good Luck", name)

words = ["name", "rainbow", "reverse", "science", "gaming", "machine", "computer", "hunting", "python", "mathematics", "player", "geeks", 
         "question","water", "condition", "board", "learn", "weather", "programming", "calculator", "structure", "practice", "desktop"
          , "hollow" ]
# Fuction will choose one random word from the list
word = random.choice(words)

print ("Guess the character:")

guesses = ''

#any number of turns
turns = 10

while turns > 0 :
    # counts number of times user is failed
    failed = 0
    # characters from the input word taking one at a time
    for char in word:
        # comparing the the gueesses with the chosen word from the list
        if char in guesses:
            print (char)
        else:
            print ('*')
            #for every failure one will be incremented
            failed += 1

    if failed == 0:
    # If there is no failed word anymore than the user wins and 'You win' is printed
        print ("You win!")
        # the correct word is printed
        print ("The word is:", word )
        break
    # if the user enters wrong alphabet again the character is asked
    guess = input("Guess the character!:")
    
    #Every input character is stored in  guesses
    guesses += guess
    # Check the input in the word
    if guess not in word:
    # If input is not in the word chosen, number of turns gets decreased and 'Wrong' is printed     
        turns -= 1
        print('Wrong')
        #the number of turns left will get printed
        print ('You have', +turns, "more guesses only")
        
        # If turns get 0 'You loose gets printed'
        if turns == 0:
            print ('You loose!')