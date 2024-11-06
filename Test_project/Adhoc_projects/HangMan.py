import random

def guessWord(randomWord, correctGuess):
    #Make randomWord a list so we can iterate and return the index
    correctWordList = []
    for w in randomWord:
        correctWordList.append(w)

    #change the correctGuess '_' to a list
    correctGuessList = []
    for w in correctGuess:
        correctGuessList.append(w)
    #print("corectGuessList:", correctGuessList)

    correctUserWord = ''
    allGuessList = []

    while correctUserWord != randomWord:
        print(f"List of letters entered: {allGuessList}")
        userGuess = input("Please enter a single letter: ").lower()
        
        if userGuess not in allGuessList:
            allGuessList.append(userGuess)       
        else:
            print(f"Please enter a new letter not already guessed.")
        index = 0
        for w in correctWordList:
            if userGuess == w:
                correctGuessList[index] = userGuess
                correctUserWord = ''.join(correctGuessList) 
            index +=1
        print(correctUserWord, '\n')        

    print(f"Congratulations you have guessed the word: {correctUserWord}")    


def main():
    randomWordList = ['charcter']
    randomWord = random.choices(randomWordList, k = 1)
    randomWordlen = len(randomWord[0])
    word = ''.join(randomWord)
    correctGuess = randomWordlen*'_'
    print(f"Guess the mystery word: {correctGuess}")
    
    guessWord(word, correctGuess)


main()