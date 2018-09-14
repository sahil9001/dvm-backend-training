				#SILHOUETTE - A Simple story based game using OOP concepts as an assignment for DVM
								#Author - Divyansh Agarwal

import sys
from random import randint  #to generate a random integer
from textwrap import dedent
import time
import re
import os #for clearing the screen
from colorama import init, Fore, Style #for printing colored text in the terminal

										#MAIN MENU
print('''
			  ______   ______  __        __    __   ______   __    __  ________  ________  ________  ________ 
 			/      \ /      |/  |      /  |  /  | /      \ /  |  /  |/        |/        |/        |/        |
			/$$$$$$  |$$$$$$/ $$ |      $$ |  $$ |/$$$$$$  |$$ |  $$ |$$$$$$$$/ $$$$$$$$/ $$$$$$$$/ $$$$$$$$/ 
			$$ \__$$/   $$ |  $$ |      $$ |__$$ |$$ |  $$ |$$ |  $$ |$$ |__       $$ |      $$ |   $$ |__    
			$$      \   $$ |  $$ |      $$    $$ |$$ |  $$ |$$ |  $$ |$$    |      $$ |      $$ |   $$    |   
 			 $$$$$$  |  $$ |  $$ |      $$$$$$$$ |$$ |  $$ |$$ |  $$ |$$$$$/       $$ |      $$ |   $$$$$/    
			/  \__$$ | _$$ |_ $$ |_____ $$ |  $$ |$$ \__$$ |$$ \__$$ |$$ |_____    $$ |      $$ |   $$ |_____ 
			$$    $$/ / $$   |$$       |$$ |  $$ |$$    $$/ $$    $$/ $$       |   $$ |      $$ |   $$       |
 			 $$$$$$/  $$$$$$/ $$$$$$$$/ $$/   $$/  $$$$$$/   $$$$$$/  $$$$$$$$/    $$/       $$/    $$$$$$$$/ 
                                                                                                  
     ''')

print(dedent('''
									WELCOME TO THE GAME!

			You are an explorer and in your journey you lost track and were trapped by someone in a haunted
			house in the dark forest. The person who trapped you likes to play games and has set one up for 
			you too in the house.The game requires you to complete certain 'tasks' in the house in order to 
			obtain the key that locks the main door of the house which is the only exit out of the house. 
			**CAUTION**: It is rumored that there lives an old fat beast in the house that goes by the name
			'Pudge'. Pudge is constantly hungry for human meat and has healing powers, so plan your actions
			acordingly.
			'''))

#Definitions of all Classes:

class Levels:   #base class for all the 5 levels in the game
	init()		#to filter ANSI escape sequences

class Intro(Levels): #Level 1
	def enter(self):
		print(Fore.RED + '** LEVEL 1 **', Style.RESET_ALL)
		print(dedent('''
					You find yourself in a small room with complete darkness. There is no power in the house.
					At the moment, you have a video camera with nightvision mode and a desert eagle with 2 bullets.
					You try to turn on the camera but it doesn't work. The batteries are dead!
					In the room there's a wooden table with a drawer, a bookshelf and a TV. Also,there is
					a bunch of random stuff scattered on the floor. To proceed, you need to have some sort of vision.
					'''))
		print('What do you do to get batteries?')
		action = input('>')

		bookshelf  = re.match(r'[a-zA-Z ]{0,}bookshelf[a-zA-Z]{0,}', action)
		floor = re.match(r'[a-zA-Z ]{0,}floor[a-zA-Z]{0,}', action)
		drawer = re.match(r'[a-zA-Z ]{0,}drawer[a-zA-Z]{0,}', action)
		tv = re.match(r'[a-zA-Z ]{0,}tv[a-zA-Z ]{0,}', action)

		if floor:
			print(dedent('''
						->You bend over and check the floor to find random tech magazines and related articles 
						scattered on the floor but nothing remotely close to camera batteries. 
						'''))
			return 'intro'

		elif drawer:
			print(dedent('''
						->You open the drawer and take a look inside. There is a lighter and a tv remote.
						What do you do? 
						'''))
			drawer_action = input('>')

			remote = re.match(r'[a-zA-Z ]{0,}remote[a-zA-Z ]{0,}', drawer_action)
			lighter = re.match(r'[a-zA-Z ]{0,}lighter[a-zA-Z ]{0,}', drawer_action)

			if remote:
				print('''
						Luckily, the batteries used in the remote also work for the camera.
						The camera is up and running!
						You use the camera to explore the adjacent rooms and reach the "CONTROL ROOM" which contains 
						a computer that looks like a master computer of the house. But to power it up, you need to go to
						the basement and reset the generator. Courageously, you decide to do that right away.
					''')
				return 'basement'

			elif lighter:
				print('''
					You pick up the lighter but it doesn\'t work. Try something else!
					''')
			
			else:
				print('You can\'t quite do that!')
				return 'intro'

		elif bookshelf:
			print(dedent('''
						You go and check the bookshelf. The shelves are very dirty. You look closely and find
						some of the finest works by Douglas Adams but no batteries.
						'''))
			return 'intro'
		elif tv:
			print('''
				There is no power, you n00b. How can you turn on the tv? -_-
				  ''')
			return 'intro'

		else:
			print('Try something else.')
			return 'intro'
# **************************************************************************************************

class Basement(Levels): #Level 2
	def enter(self):
		print(Fore.GREEN + '** LEVEL 2 **', Style.RESET_ALL)
		print(dedent('''
					You slowly walk to the lobby and reach the main hall. There is a photo of Douglas Adams hanging
					above the dining table. You find and use the stairs to reach the basement. Using your camera, 
					you see that there is complete darkness and water up to shin level everywhere. Possible 
					assumption could be that there is be a pipe leaking somewhere in the basement. You make your 
					way to the generator room. There is a big generator present. Also present in the room are an 
					almirah, an old empty coffin and a bed. (Maybe someone even sleeps here. Who knows!?) Suddenly,
					you hear a loud and scary voice in the stairs that lead to the basement. It's the beast that 
					lives in this house. The voice is getting louder. Pudge is coming to get you!
					He is now roaming outside the generator room and you see him coming in the room.
					What do you do now?
					'''))

		action = input('>')

		shoot = re.match(r'[a-zA-Z ]{0,}shoot[a-zA-Z ]{0,}',action)
		hide_under_bed = re.match(r'[a-zA-Z ]{0,}hide (under|under the) bed[a-zA-Z ]{0,}',action)
		hide_in_coffin = re.match(r'[a-zA-Z ]{0,}hide (in|inside|in the|inside the) coffin[a-zA-Z ]{0,}',action)
		hide_in_almirah = re.match(r'[a-zA-Z ]{0,}hide (in|inside|in the|inside the) almirah[a-zA-Z ]{0,}',action)
		hide_behind_generator = re.match(r'[a-zA-Z ]{0,}hide (behind|behind the) generator[a-zA-Z ]{0,}',action)
		run = re.match(r'[a-zA-Z ]{0,}run[a-zA-Z ]{0,}',action)

		if run:
			print('''
				->In an attempt to escape, you try and run through the water but make awful lot of noise.
				 This gets the attention of Pudge and infuriates him further. He gets hold of you and 
				 beats you to death.
				 ''')
			return 'death'

		elif action == 'hide':
			print('Be specific where you want to hide')
			return 'basement'

		elif shoot:
			print(dedent('''
						->The beast gets wounded by the bullet, fumbles a bit but recovers quickly
		 				and outrageously slaughters you. The beast quickly heals from the 2 shots of
		 				desert eagle since he has healing powers. Didn't you read the intro properly?
		 				'''))
			return 'death'

		elif hide_behind_generator:
			print('''
				You go and hide behind the generator. Unknowingly, you step on a loose wire that was faulty due 
				to the water leaking. You get a high voltage shock and die.
				 ''')
			return 'death'

		elif hide_in_almirah:
			print('''
				You hide inside the almirah and close the door. When Pudge approaches the almirah,
				he is able to hear your heavy breath sounds. He immediately breaks the almirah and kills you.''')
			return 'death'

		elif hide_in_coffin:
			print('''
				You hide inside the coffin, lock it and avoid Pudge when he enters the room. After he is gone,
				you can't get out of the coffin since the lock stopped working. (Remember that the coffin
				was old.) You are now trapped inside forever.
				''')
			return 'death'

		elif hide_under_bed: #leads to next level
			print('''
				You quickly go under the bed and hide. Pudge is lazy enough to not check under the bed and you
				safely avoid him when he enters the room. After a few minutes, he goes back. Now, you just have
				to reset the generator.
				''')
			return 'generator_reset'
		else:
			print('Uh-huh, you can\'t do that.')
			return 'basement'
# **************************************************************************************************

class GeneratorReset(Levels): #Level 3
	def enter(self):
		print(Fore.CYAN + '** LEVEL 3 **', Style.RESET_ALL)
		print(dedent('''
					For resetting the generator, there are three switches numbered : '42', '73', '28'.
					Out of these three, only one switch will actually reset the generator and the other 
					two will set off a loud alarm in the house. You have to choose the correct switch number.
					**HINT**: Remember the path to this room. Hopefully, you know the trivia behind it.
					'''))
		guess = int(input('>'))

		if guess == 42: #correct switch number = 42 (Answer to everything)
			print(dedent('''
						Hmm, seems like you know the answer to everything. (Geddit?)
						You chose the right switch and the generator gets reset. The power is back on! You now 
						go back to the control room. But beware, Pudge may return because you still make 
						little noises while going back.
						'''))
			return 'control_room'

		elif guess == 73 or guess == 28: #incorrect choices
			print('BZZZZZZ! Wrong choice! You set off the alarm. The beast quickly comes back and kills you.')
			return 'death'

		else:
			print('Invalid switch number.')
			return 'generator_reset'
# **************************************************************************************************

class ControlRoom(Levels): #Level 4
	def enter(self):
		print(Fore.RED + '** LEVEL 4 **', Style.RESET_ALL)
		print(dedent('''
					You have managed to get the power on and the master computer working ; but sadly, its password protected.
					Luckily though, there's a simple game you can play and win to get the password. The game is called
					High-Low. The rules of the game are:
					-The password is a number between 1 and 100 (both inclusive) and you have to guess it.
					-You get 6 tries. After each try, you'll be told whether your guess was higher or lower
					than the actual password.
					-If you succeed, all the files of the computer will be available to you.
					Meanwhile you hear the loud noises of Pudge approaching the control room from the lobby.
					Fortunately, the door is locked so he is stuck at breaking the lock.
					HURRY! or else Pudge will open the lock.
					'''))

		password = randint(1,100)
		guess = int(input('Enter guess: '))
		tries = 0

		while guess != password and tries < 5:

			if guess > password:
				print('Go lower')
			else:
				print('Go higher')

			tries += 1
			guess = int(input('Enter guess: '))

		if guess == password:
			print(dedent('''
						Password guessed correctly! You now have access to all the files in the computer.
						You use admin privileges to enable the high voltage shock wire on the control room door.
						This zaps the beast and he is rendered motionless and finally falls to the ground.
						'''))
			return 'last_task'
		else:
			print(dedent('''
						OOPS!	
						You couldn't guess the password correctly. Meanwhile, Pudge manages to break the 
						lock and enter the control room. He breaks the computer and swallows you alive.
						'''))
			return 'death'
# **************************************************************************************************

class LastTask(Levels): #Level 5(Final)
	def enter(self):
		print(Fore.GREEN + '** FINAL LEVEL **', Style.RESET_ALL)
		print(dedent('''
					Now that you've dealt with the beast, you focus on finding things in the computer that'll help
					you escape. You come across a hidden folder that requires elementary cipher techniques to open.
					On bypassing, you find a text file in the folder that says 'Last Task'.
					The file read:
					Congrats on making it till here. I want to end on a funny note, so I'll just ask you one last
					question and then I'll tell you where the key is. 

					Identify the person from the following figure:






				






					'''))
		time.sleep(10)
		print('*HINT*: There have been memes made on this!')
		answer = input('Your answer >')

		if answer == 'john cena' or answer == 'John Cena':
			print(Fore.GREEN + 'YOU WON!', Style.RESET_ALL)
			print(dedent('''
						Congrats on completing the tasks. You have proved yourself.
						To get the key, go to the corner in the control room that is exactly opposite to the door.
						Then, go to the tile at coordinate (4,2), turn it around and you'll find the key. 
						Good game, well played!
						'''))
			return 'credits'
		else:
			print('Oops! You came close to obtaining the key but failed in the last task.')
			return 'death'
# **************************************************************************************************

class Credits: #Displays credits after player wins the game
	def enter(self):
		print(dedent('''
					Thanks for playing!
					Made by : DIVYANSH AGARWAL
					Testing Credits : Hamza, Ayush
					Feedback at : f20180791@pilani.bits-pilani.ac.in
					'''))
# **************************************************************************************************

class Death(Levels): #Handles what happens when user fails in the game
	list_of_msgs = [
					'Git gud and retry!',
					'Better luck next time!',
					'GG, not so well played.',
					'Even my grandma plays better than you!',
					'Try again, loser!',
					'Tu pakka BPharm ka hoga'
				]
	def enter(self):
		print(Fore.RED + Death.list_of_msgs[randint(0,len(self.list_of_msgs)-1)], Style.RESET_ALL) #Prints a random
																								   #death msg from
																								   #list_of_msgs
		print('')
		action = input('Play again? (y/n) :')
		if action == 'y' or action == 'Y':
			os.system('cls')
			game.play()
		else:
			exit(1)
# **************************************************************************************************

class GameEngine: #Runs the game and navigates to different levels 
	
	def __init__(self, game_map):
		self.game_map = game_map

	def play(self): #Starts the game
		current_level = self.game_map.opening_level()
		last_level = self.game_map.go_to_level('credits')

		while current_level != last_level:
			next_level = current_level.enter() #Fetches the next level to be run from enter() of current_level
			current_level = self.game_map.go_to_level(next_level)

		current_level.enter() #Runs the last level
# **************************************************************************************************

class Map:			#Map of the whole game including all the levels
	levels = {		#Dictionary of words used for referring to different levels
		
		'intro': Intro(),
		'basement': Basement(),
		'control_room': ControlRoom(),
		'last_task': LastTask(),
		'death': Death(),
		'engine': GameEngine,
		'credits': Credits(),
		'generator_reset': GeneratorReset()
	}

	def __init__(self, starting_level):
		self.starting_level = starting_level

	def go_to_level(self, level): 	#Runs the level that is passed as argument 
		val = Map.levels.get(level)
		return val

	def opening_level(self):        #Runs the opening level
		return self.go_to_level(self.starting_level)

map = Map('intro')
game = GameEngine(map)
game.play() #Starts the game














