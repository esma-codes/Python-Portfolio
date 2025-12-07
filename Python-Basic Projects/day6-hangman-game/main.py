import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=len(stages)-1

word_list=["aardvark","baboon","camel"]

chosen_word=random.choice(word_list)
#print(chosen_word)

#placeholder
display="_"*len(chosen_word)
print(display)


game_over=False
correct_letters=[]

while not game_over:
    guess=input("Enter a letter : ").lower()

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            game_over = True
            print("You lose!")
    else:
        new_display=""

        for letter in chosen_word:
            if letter==guess:
                new_display+=letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                new_display+=letter
            else:
                new_display+="_"
        display=new_display
        print(display)

    if "_" not in display:
        game_over=True
        print("You Win!")

