#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 15:41:03 2018

@author: shivanshu
"""

import re
import random
from openpyxl import load_workbook

pattern = re.compile('\d\d\d')


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

              Also, you can type 'instructions' anytime you want to see
              these instructions again.

              That's all you need to know to play this game.
              Happy Guessing!

              """


def instructions():
    # Asks player whether they want to read the instructions or not.

    response = input("Would you like to read the instructions?(y/n)")
    if response == 'y' or response == 'yes':
        print(instruction)

    elif response == 'n' or response == 'no':
        pass

    else:
        print("Please provide a valid response")
        instructions()


def chooseDiff():
    """
    Asks player to set difficulty and
    sets number of guesses accordingly.
    """
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
        return chooseDiff()


class secretNum(str):
    # The secret number is an object of type secretNum.

    def __init__(self):
        self.value = ''

    def getValue(self):
        # Sets a random value to the secretNum object and returns it.
        numbers = list(range(10))
        random.shuffle(numbers)
        for i in range(3):
            self.value += str(numbers[i])
        return self.value


class hint(str):
    """
    Used when the user asks for help.
    """

    def __init__(self):

        self.divisible = "The number is divisible by"
        self.between = "The number lies between"

    def getHint(self, secretNumber):
        """
        Returns either the divisibility of the secret number by 2, 3 or 5
        or the range in which the secret number lies.
        """
        secretNumber = int(secretNumber)
        if secretNumber % 5 == 0:
            return self.divisible + " 5"

        elif secretNumber % 3 == 0:
            return self.divisible + " 3"

        elif secretNumber % 2 == 0:
            return self.divisible + " 2"

        elif secretNumber >= 0 and secretNumber < 301:
            return self.between + " 0 and 300"

        elif secretNumber >= 301 and secretNumber < 601:
            return self.between + " 301 and 600"

        else:
            return self.between + " 601 and 999"


class fact(str):
    def __init__(self):
        self.value = ''

    def getFact(self):
        """
        Gets a random fact from Facts.xlsx
        """
        book = load_workbook('Facts.xlsx')
        sheet = book['Sheet1']
        x = random.randint(0, 29)

        for column in sheet.columns:
            self.value = column[x].value
            return (self.value)


class clue(list):

    def __init__(self):
        self.value = []

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

            if not pattern.fullmatch(guess):
                return "Please provide a valid response."

            self.value = []

            for i in range(3):

                if guess[i] == secretNumber[i]:
                    self.value.append("Bananas!")

                elif guess[i] in secretNumber:
                    self.value.append("Mangoes!")

            if len(self.value) == 0:
                self.value.append("Pineapples!")

            global numGuess
            numGuess += 1

            self.value.sort()
            return ' '.join(self.value)


def getScore(numGuess, clues):
    """
    Returns a score on the basis of how close to the
    number the player got and how many guesses it took.

    numGuess: an integer
    clues: an array
    returns: an integer
    """
    score = 800
    score -= numGuess * 100

    global hintCount
    if hintCount == 1:
        score -= 100

    for clue in clues:

        if clue == "Pineapples!":
            score -= 200
            return score

        if clue == "Mangoes!":
            score += 50

        if clue == "Bananas!":
            score += 100

        if guess == secretNumber:
            score += 200

    return score


def playAgain():
    """
    Asks the user whether they want to play again.
    Returns a boolean.
    """

    while True:
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
        print("The secret number was", secretNumber)

    score = getScore(numGuess, clue1.value)
    print("Your score is " + str(score))
    print("")

    play = playAgain()
    if not play:
        break
