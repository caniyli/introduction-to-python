############################################
#                                          #
#              Hangman Game                #
#                                          #
############################################

import random as rand

class Hangmangame :
    def __init__(self):

        words_list = ["kedi","resim","kaşık","çatal","bıçak","yemek", "masa", "sandalye", "televizyon", "monitör", "klavye", "fare", "köpek", "kahve","bardak","şişe","kablo","kalem","kitap","bilim","hoparlör","kasa","telefon","gözlük"]
        self.words_list = words_list
        guesses = []
        self.guesses = guesses
        self.turns = 5
        return None

    def randomword(self):

        word = rand.choice(self.words_list)
        self.word = word
        display = []
        for letter in word:
            display.append('_')
        self.display = display

    def disp(self):

        hangman = ['''
              ---------
              |        |
              |        O
              |       \|/
              |        |
              |       / \ 
            ------
        ''',
        '''
             ---------
             |        |
             |        O
             |       \|/
             |        |
             |       
           ------
        ''',
        '''
             ---------
             |        |
             |        O
             |       \|/
             |        
             |       
           ------
        ''',
        '''
             ---------
             |        |
             |        O
             |        |
             |        
             |       
           ------
              ''',
        '''
            ---------
            |        |
            |        O
            |       
            |        
            |       
          ------
        ''',
        '''
            ---------
            |        |
            |        
            |       
            |        
            |       
          ------
                         '''
                   ]
        print((hangman[self.turns]))
        self.hangman = hangman
        for i in range(len(self.display)):
            print(self.display[i],end='')
        print()


    def play(self):

        guess = ''
        guess = input("Lütfen bir harf tahmin ediniz").lower()

        if len(guess)>1:
            print("Lütfen sadece 1 harf giriniz")

        elif guess in self.guesses:
            print("Bu harrfi daha önce tahmin ettiniz")

        elif guess in self.word:
            self.guesses.append(guess)
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    self.display[i] = guess

        else:
            self.guesses.append(guess)
            self.turns-=1

    def win(self):

        checkword = ''
        for i in self.display:
            checkword+=i

        if checkword == self.word:
            print("Tebrikler oyunu kazandınız bilinen kelime {}".format(self.word))
            return True
        else:
            return False

    def loss(self):

        if(self.turns==0):
            print(f'Aradıgınız kelime = {self.word}. Oyunu kaybettiniz')
            return True
        else:
            return False

game = Hangmangame()
game.randomword()
game.disp()
while True:
    game.play()
    game.disp()

    if game.win():
        break
    if game.loss():
        break










