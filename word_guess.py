import random
attempts = 10

word_bank = ["python", "java", "node", "coddex", "syntax", "modules", "string", "integer", "hypelink", "stylesheet"]

word = random.choice(word_bank)

guessedWord = ["_"] * len(word)

while attempts > 0:
    print("\nCurrent word: " + " ".join(guessedWord))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Great guess!")
    else:
        attempts -= 1
        print("Wrong guess! Attempts left: " + str(attempts))

    if "_" not in guessedWord:
        print("\nCongrats! You guessed the word: " + word)
        break

else:
    print("\nYou\ 've run out of attemtps! The word was: " + word)

