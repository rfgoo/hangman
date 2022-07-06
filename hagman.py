from py_random_words import RandomWords

word = RandomWords().get_word()
letters = ["_"]*len(word)
failed = []
lives = 0


def lose():
    print("LOOOOOSER")
    print("The secret word is: ", word)


def win():
    print("You've won!!!")
    print("The secret word is: ", word)


while True:
    print(lives, "/6")

    if lives == 6:
        lose()
        break

    print("Wrong guesses", ', '.join(failed))
    print(''.join(letters))
    guess = input("what's your guess: ")

    while guess in failed or guess in letters:
        guess = input("what's your guess:")

    if len(guess) > 1:
        if guess != word:
            lose()
            break
        else:
            win()
            break

    if guess not in word:
        lives += 1
        failed.append(guess)

    for i in range(len(word)):
        if word[i] == guess:
            letters[i] = guess

    if ''.join(letters) == word:
        win()
        break
