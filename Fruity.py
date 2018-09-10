#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 15:41:03 2018c

@author: shivanshu
"""

import re
import random
from openpyxl import load_workbook




def intro():
    print("""

                        ~~ WELCOME TO ~~


       ______   ______     __  __     __     ______   __  __                    
      /\  ___\ /\  == \   /\ \/\ \   /\ \   /\__  _\ /\ \_\ \                   
      \ \  __\ \ \  __<   \ \ \_\ \  \ \ \  \/_/\ \/ \ \____ \                  
       \ \_\    \ \_\ \_\  \ \_____\  \ \_\    \ \_\  \/\_____\                 
        \/_/     \/_/ /_/   \/_____/   \/_/     \/_/   \/_____/                 

 ______   __  __     ______        ______     ______     __    __     ______    
/\__  _\ /\ \_\ \   /\  ___\      /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   
\/_/\ \/ \ \  __ \  \ \  __\      \ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\   
   \ \_\  \ \_\ \_\  \ \_____\     \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\ 
    \/_/   \/_/\/_/   \/_____/      \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/

    """)


instruction = """
              Welcome to Fruity: The Game. This is one of the many number guessing
              games out there, but it packs it's own flavour and punch. In this game,
              the computer thinks up a 3 digit number with no repeating digits.
              Your task is to guess the number in a certain number of guesses.
              The number of guesses according to difficulty are:

              Easy (e) --- 10 guesses.
              Medium (m) --- 8 guesses.
              Hard (h) --- 6 guesses.

              To help you with this task, the computer provides you with clues
              after each guess. Here's what each clue means:

              Mangoes! --- One digit is correct but in the wrong position.
              Bananas! --- One digit is correct and in the right position.
              Pineapples! --- None of the digits are correct.

              If these clues aren't enough, you can also type 'hint' to get
              a hint about the secret number. But you can only use one hint
              per game.

              But wait, there's more! If you want even more fun, you
              just have to type 'fact' and the computer will serve up
              a sweet and juicy fact about fruits right onto your screen.

              Also, you can type 'instructions' any time you want to see
              these instructions again.

              That's all you need to know to play this game.
              Happy Guessing!

              """

def instructions():
    # Asks player whether they want to read the instructions or not.
    while True:
        print("")
        response = input("Would you like to read the instructions?(y/n)")
        if response == 'y' or response == 'yes':
            print(instruction)
            break

        elif response == 'n' or response == 'no':
            break

        else:
            print("Please provide a valid response")


def chooseDiff():
    """
    Asks player to set difficulty.
    Returns maximum nuber of guesses (int).
    """
    while True:
        print("")
        diff = input("Please choose your difficulty level (e/m/h)")
        if diff == "e":
            maxGuess = 10
            print("")
            print('You have 10 guesses.')
            return maxGuess
        elif diff == "m":
            maxGuess = 8
            print("")
            print('You have 8 guesses.')
            return maxGuess
        elif diff == "h":
            maxGuess = 6
            print("")
            print('You have 6 guesses.')
            return maxGuess
        else:
            print("Please provide a valid response.")



class secretNum():
    # The secret number is an object of type secretNum.

    def __init__(self):
        self.value =''


    def getValue(self):
        """
        Sets a random value to the secretNum object and returns it
        as a string
        """
        numbers = list(range(10))
        random.shuffle(numbers)
        for i in range(3):
            self.value += str(numbers[i])
        return self.value



class hint():
    """
    Used when the user asks for a hint.
    """
    def __init__(self):

        self.divisible = "The number is divisible by"
        self.between = "The number lies between"

    def getHint(self, secretNumber):
        """
        Returns either the divisibility of the secret number by 2, 3 or 5
        or the range in which the secret number lies.
        Returns type str.
        """
        secretNumber = int(secretNumber)
        if secretNumber % 5 == 0:
            return self.divisible + " 5"

        elif secretNumber % 3 == 0:
            return self.divisible + " 3"

        elif secretNumber % 2 == 0:
            return self.divisible + " 2"

        elif 0 <= secretNumber < 301:
            return self.between + " 0 and 300"

        elif 301 <= secretNumber < 601:
            return self.between + " 301 and 600"

        else:
            return self.between + " 601 and 999"


class fact():
    def __init__(self):
        self.value = ''
        self.book = load_workbook('Facts.xlsx')
        self.sheet = self.book['Sheet1']

    def getFact(self):
        """
        Gets a random fact from Facts.xlsx
        """

        x = random.randint(0, 29)

        for column in self.sheet.columns:
            self.value = column[x].value
            return self.value


class clue(list):

    def __init__(self):
        list.__init__(self)

    def getClues(self, guess, secretNumber):
        """
        Returns the clues if the user guesses a number.
        Calls getHint() if the user asks for a hint.
        Calls getFact() if the user asks for a fact.

        """

        if guess == secretNumber:
            return "Congrats! You got it!"

        elif guess == "hint":

            global hintCount
            if hintCount == 0:
                hint1 = hint()
                hintCount += 1
                return hint1.getHint(secretNumber)

            elif hintCount == 1:

                return "You can have only one hint per game you greedy human."

        elif guess == "fact":
            fact1 = fact()
            return fact1.getFact()

        elif guess == "instructions":
            return (instruction)

        else:
            pattern = re.compile('\d\d\d')
            if not pattern.fullmatch(guess):
                return "Guess should be a 3 digit number with no repeating digits."

            else:
                for i in guess:
                    if guess.count(i)>1:
                        return "Guess should not have repeating digits."


            self.clear()
            for i in range(3):

                if guess[i] == secretNumber[i]:
                    self.append("Bananas!")

                elif guess[i] in secretNumber:
                    self.append("Mangoes!")

            if len(self) == 0:
                self.append("Pineapples!")

            global numGuess
            numGuess += 1

            self.sort()
            return ' '.join(self)


class score():

    def __init__(self):
        self.value = 800


    def getScore(self, numGuess, clues):
        """
        Returns a score on the basis of how close to the
        number the player got and how many guesses it took.

        numGuess: an integer
        clues: an array
        returns: an integer
        """

        self.value -= numGuess * 100
        #-100 for every wrong guess.

        global hintCount
        if hintCount == 1:
            self.value -= 150
            #-150 for taking a hint.

        if guess == secretNumber:
            self.value += 300
            #+300 for getting it right.


        else:
            #Partial points.
            for clue in clues:

                if clue == "Pineapples!":
                    self.value -= 200  #-200 for not getting anything right.
                    return self.value

                if clue == "Mangoes!":
                    self.value += 50   #+50 for each correct digit wrong position.

                if clue == "Bananas!":
                    self.value += 100  #+100 for each correct digit correct position.

        return self.value


def playAgain():
    """
    Asks the user whether they want to play again.
    Returns a boolean.
    """

    while True:
        print("")
        response = input("Do you want to play again?(y/n)")
        if response == 'y' or response == 'yes':
            return True
        elif response == 'no' or response == 'n':
            return False
        else:
            print("Please provide a valid response.")


# Execution of the game:
intro()
instructions()

while True:
    maxGuess = chooseDiff()
    numGuess = 0
    hintCount = 0
    clue1 = clue()
    score1 = score()
    secretNum1 = secretNum()
    secretNumber = secretNum1.getValue()

    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("I have thought up a number. You have", str(maxGuess), "guesses to get it.")

    while numGuess < maxGuess:
        guess = input("Guess Number-" + str(numGuess + 1) + ":")

        print(clue1.getClues(guess, secretNumber))
        print("")
        if guess == secretNumber:
            break

    if numGuess == maxGuess:
        print("Sorry, you ran out of guesses.")
        print("The secret number was", secretNumber+".")


    scoreValue = score1.getScore(numGuess, clue1)
    print("Your score is " + str(scoreValue)+".")
    print("")

    if not playAgain():
        break
