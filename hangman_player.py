import hangmancreater

hangman = hangmancreater.Hangman('d:\\wordlist.txt')
hangman.choose_the_word()
hangman.fill_the_word_status()
while True:
    hangman.get_word_status()
    hangman.guess_the_letter()

    if(hangman.attempts_remaining == 0):
        print("Out of attempts. Your word was {} . Game Over!".format(hangman.chosen_word))
        break

    elif(hangman.chosen_word == ''.join(hangman.word_status)):
        print("hurrah! You won the game")
        break
