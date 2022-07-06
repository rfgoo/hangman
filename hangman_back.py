from py_random_words import RandomWords


def lose():
    return False


def win():
    return True


class Hangman:
    def __init__(self):
        self.word = RandomWords().get_word()
        self.letters = ["_"]*len(self.word)
        self.failed = []
        self.lives = 0

    def play(self, attempt):

        if attempt in self.failed or attempt in self.letters:
            return None
    
        if len(attempt) > 1:
            if attempt != self.word:
                return lose()
            else:
                return win()
    
        if attempt not in self.word:
            self.lives += 1
            self.failed.append(attempt)

        if self.lives == 6:
            return lose()

        for i in range(len(self.word)):
            if self.word[i] == attempt:
                self.letters[i] = attempt
    
        if ''.join(self.letters) == self.word:
            return win()
