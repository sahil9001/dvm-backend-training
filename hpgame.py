from time import sleep
from sys import exit

#Definition of a base class 'scene'

class scene(object):

    def __init__(self):
        self.description=""
        self.opponent="no opponent is assigned to this scene "
        self.spell=""
        self.opt_spell=['expelliarmus','winguardiumleviosa','aquamenti','alohomora','ascendio','finestra','stupify','difindo','incendio','avada_kedavra']
        self.spell_set={'expelliarmus':"To unarm the other opponent",
                        'winguardiumleviosa':"Spell used for levitating objects",
                        'aquamenti':"Produces a fountain or jet of water from the wand tip",
                        'alohomora':"Used to open and unlock doors",
                        'ascendio':"Lifts the caster high into the air",
                        'finestra':"Used for shattering glass",
                        'stupify':"Ssed to make target unconcious",
                        'difindo':"Used to cut everything",
                        'incendio':"fire making Charm",
                        'avada_kedavra':"To kill him....!!!"
                        }


    def action(self):
        pass

    def prline(self):

        print("\n****---------------------------------------------------------------****")



#subclasses of the class scene

class introduction(scene):
#introduction scene of the g@me

    def __init__(self):
        self.description=""
        super(introduction,self).__init__()


    def rules(self): #function to display rules of the game

        self.prline()
        print("\n\tRULES OF THE GAME ")
        print("""

    1.) In each and every scene you will face an opponent
        who is willing to kill you and you have to defeat
        him to move forward.

    2.) For each and every opponent you'll be given a set
        of spells and you have to use only one of them to
        defeat him.

    3.) Hints would be given to defeat an opponent so that
        you can logically defeat the opponent using spells.

    4.)Try to use a wrong spell and just watch the results..!!!

              """)

        print("\n\n")
        input("\n\tPress Enter to continue")

        self.prline()
        print("\n\tINTRODUCTION TO SPELLS THAT CAN BE USED.")
        print("\n")


        for spell in self.opt_spell:               #loop to display spells and their function
            print("\n    {} : {} ".format(spell,self.spell_set[spell]))




    def action(self):

        while 1:
            print("""

                  In front of you there is a sealed door
                  and you need to open this using a spell !!

                  ***Enter the spell to open the door***

                 """)
            self.spell=input("    => ")

            if self.spell.lower()=='alohomora':

                print("\n\n    ****_____The Door Opens____****\n\n")

                break

            else:

                print("\n\n    If you don't even know how to open a door... how would you defeat wizards..!!??\n")


        return "girls_bathroom"


class girls_bathroom(scene):
#scene where you'll face 'troll'

    def __init__(self):

        self.opponent="troll"
        self.description=["Trolls generally reach a height of about twelve feet and weigh up to a tonne.",
        "Troll whiskers have magical properties, and are sometimes used as wand cores.",
        "Their feet have two toes, both with giant toenails.",
        "They are dangerously violent and incredibly aggressive,",
        "and they engage in unpredictable behaviour, comparable to giants.",
        "They are also incredibly low in intelligence."]

        self.opt_spell=["winguardiumleviosa"]

    def action(self):

        sleep(2)
        self.prline()
        print("""

                  Did you hear that..?? .
                  is that Hermoine..??
                  she's in trouble...!!!
                  we need to go there....girls washroom...!!

                      """)
        sleep(1)

        print("""

              Ohh..!! this is a monster called troll...!!
              He is holding a log of wood in his hands
              use some spell to beat him with that log

              """)
        sleep(1)

        for line in self.description:
            print("    ",line)


        sleep(1)
        print("""

                Use any of the following spells
                finestra | stupify | imperio | winguardiumleviosa

                (choose wisely..!! hint - if that log can be lifted in air it would drop on him only)

                """)
        self.spell=input("****Enter the spell****  =>  ")

        sleep(1)
        if self.spell.lower() in self.opt_spell:

            print("\n    That was a clever move....the log he was holding \n    fell on his head and he is unconcious now  ")
            return "dungeons"

        else:

            print("\n\n    You used a wrong spell...He banged you with the log that he was holing \n    and you are dead..!!!")
            return "death"



class dungeons(scene):
#scene where you'll face 'Quirrell'

    def __init__(self):

        self.opponent="Quirrel"
        self.description=["Quirrell is a young man with light blue eyes and very pale skin"
                          ,"he is wearing a purple turban"
                          ,"Poor Quirrell is easily manipulated, and had pretty much no backbone."
                          ,"He is completely submitted to Lord Voldemort"]

        self.opt_spell=["incendio"]

    def action(self):

        sleep(2)
        self.prline()
        print("""

              You are in Dungeons and professor Quirrel is standing in front of you .


              """)

        for line in self.description:
            print("   ",line)

        sleep(1)
        print("""

                @QUIRREL ~ "I met him...you know who,, when I traveled around the world. A foolish young
                              man I was then, full of ridiculous ideas about good and evil.
                                He(Lord Voldemort) showed me how wrong I was. There is no good
                              and evil, there is only power, and those too weak to seek it
                                 Join me Potter or else i would kill you..!!"

              """)

        sleep(1)
        print("""
                  Use any of the following spells
                  incendio | stupify | imperio | difindo

                  (choose wisely..!! hint - he can be defeated with fire)

                  """)
        self.spell=input("****Enter the spell**** =>  ")

        sleep(1)
        if self.spell.lower() in self.opt_spell:

            print("\n\n    Well done..!!! You just burned Prof.QUIRREL....I see you are a nice wizard")
            return "forbidden_for"

        else:

            print("\n\n    You used a wrong spell...you are defeated.....!!!")
            return "death"



class forbidden_for(scene):
    #scene where you'll face 'Aragog'
    def __init__(self):
        self.opponent="aragog"

        self.description=["Aragog is a massive, dark, hairy brown/black Acromantula",
                          "with the ability to communicate with humans.",
                          " His size dwarfed that of his offspring and he possessed eight eyes that were milky",
                          " white and totally blind, possibly due to his advanced age."]

        self.opt_spell=["ascendio","stupify"]

    def action(self):

        sleep(2)
        self.prline()
        print("""

               You are now entering the forbidden forest.
               Ohh..!! aragog is there....Do you know about  aragog..??
               let me tell you..

               """)

        for line in self.description:
            print("    ",line)

        sleep(1)
        print("""

                 @ARAGOG ~ "Go? I think not. My sons and daughters do not harm Hagrid upon my
                         command, but I cannot deny them fresh meat when it wanders so willingly
                         into our midst. Good-Bye, Friend of Hagrid."

               """)

        sleep(1)
        print("""

                  Use any of the following spells
                  aquamenti | stupify | ascendio | alohomora


                  (choose wisely..!! hint - you can make him unconcious)

               """)
        self.spell=input("****Enter the spell**** =>  ")

        if self.spell.lower() in self.opt_spell:

            sleep(1)
            print("\n\n    Well done you can now pass through the forbidden forest")

            return "chamber_of_sec"

        else:

            print("\n\n    You used a wrong spell and now u'll be served on the dinning table of ARAGOG..!!!")
            return "death"




class chamber_of_sec(scene):
#scene where you'll face 'Basilisk'
    def __init__(self):

        self.opponent = "Basilisk"
        self.description=["Basilisk is a giant serpent which can instantly kill anyone who looks into their eyes",
                           "you have to avoid looking into his eyes else you'll die"]

        self.opt_spell=["incendio","difindo"]

    def action(self):

        sleep(2)
        self.prline()
        print("""

               You are now going to enter in the CHAMBER OF SECRETS,
               here you will face "Basilisk"

               """)

        for line in self.description:
            print("   ",line)

        sleep(1)
        print("""

                @Basilisk ~ "Come... Come to me... Let me rip you... Let me tear you...
                              Kill... time to kill... so hungry... for so long.

                                     I SMELL BLOOD! I SMELL BLOOD!"

             """)

        sleep(1)
        print("""
                  Use any of the following spells
                  incendio | stupify | ascendio | difindo)

                  (choose wisely..!! hint - he's afraid of fire and can be killed using sharp object)

                  """)
        self.spell=input("****Enter the spell****  => ")

        sleep(1)
        if self.spell.lower() in self.opt_spell:

            print("\n\n    Well done..!!! you have defeated Basilisk")

            return "room_of_req"

        else:

            print("\n\n    You used a wrong spell and Basilisk is now ready to EAT you..!!!")

            return "death"



class room_of_req(scene):
#scene where you'll face 'Draco malfoy'

    def __init__(self):

        self.opponent = "Draco Malfoy"
        self.description=["Draco Malfoy a tall and slender boy with sleek platinum"
                          ,"blond hair, pale skin, cold grey eyes and sharp features",
                          "He eventually became downright evil when he joined Voldemort's side"]
        self.opt_spell=["aquamenti","stupify"]


    def action(self):

        sleep(2)
        self.prline()
        print("""

              DRACO MALFOY...!!!!!
              What is he doing in the ROOM OF REQ
              He would definitely try to stop u
              But wait he is injured...you should help him

                 """)

        sleep(1)
        for line in self.description:
            print("    ",line)

        sleep(1)
        print("""

                @MALFOY ~ "I don't want your help! Don't you understand?
                            I have to do this! I have to kill you...
                           or he's gonna kill me"

             """)

        sleep(1)
        print("""

              Use any of the following spells
              incendio | stupify | ascendio | aquamenti)

              (choose wisely..!! hint - you can make him unconcious or a stream of water can help you to fool him)

                """)

        self.spell=input("****Enter the spell**** => ")

        sleep(1)
        if self.spell.lower() in self.opt_spell:

            print("\n\n    Well done..!!! you can now move forward")

            return "central_stairs"

        else:

            print("\n\n    You used a wrong spell and now malfoy Killing you with his deadly spells..!!!")

            return "death"





class central_stairs(scene):
#scene where you'll face 'Nagini'

    def __init__(self):

        self.opponent="Nagini"

        self.description=["Oh yay!!!, another creepy creature who eats humans. And this one's a snake.",
                          " Voldemort's pet is pretty evil, as she eats a ton of his victims",
                          "He is one of the most dangerous creature in Hogwarts",
                        "Do not allow him to even touch you or grab you"]
        self.opt_spell=["difindo","incendio"]


    def action(self):

        sleep(2)
        self.prline()
        print("""

              Now you're heading towards central stairs..!!!


               """)


        sleep(1)
        for line in self.description:
            print("    ",line)


        sleep(1)
        print("""

              Use any of the following spells
              alohomora | incendio | aquamenti | difindo)

              (choose wisely..!! hint - snakes are afraid of fire and sharp objects)

              """)

        self.spell=input("****Enter the spell**** => ")

        sleep(1)

        if self.spell.lower() in self.opt_spell:

            print("\n\n    Well done..!!! You just defeated one of the most \n    dangerous creature of Hogwarts..")

            return "entrance_courtyard"

        else:

            print("\n\n    You used a wrong spell...You know where are you..??")
            print("\n    In Nagini's Stomach..!!!")
            return "death"

class entrance_courtyard(scene):
#scene where you'll 'face lord Voldemort'

    def __init__(self):

        self.opponent="Lord Voldemort"

        self.description=["Voldemort as having pale skin, a chalk-white, skull-like face,",
                          "snake-like slits for nostrils, red eyes and cat-like slits for",
                           "pupils, a skeletally thin body and long, thin hands with",
                           "unnaturally long fingers.",
                           "He is the most powerful Dark Wizard of all time and the Dark",
                            "Lord of the Death Eaters; who aims to take over the wizarding",
                            "world and shape it following his supremacist views."]

        self.opt_spell=["avada_kedavra"]




    def action(self):

        sleep(2)
        self.prline()
        print("""

              You are Heading towards Entrance Courtyard and you know
              Who is waiting for you there....""")

        sleep(2)

        print("\n    The most Destructive Wizard of the World")
        sleep(2)
        print("\n    The most powerful Wizard who killed your parents ")
        sleep(2)
        print(" \n    Yess...!!! You're right it's LORD VOL....\n\n")
        sleep(2)

        for line in self.description:
            print("    ",line)
            sleep(1)

        sleep(2)

        print("""

              @VOLDEMORT ~ "Don't you turn your back on me, Harry Potter!
                            I want you to look at me when I kill you!
                            I want to see the light leave your eyes!'"

             """)

        sleep(2)

        print("""

                        "Harry Potter... the Boy Who Lived... came to die"

                """)
        sleep(1)
        print("""

               Use any of the following spells
               incendio | stupify | avada_kedavra | finestra)

            (choose wisely..!! hint - he can be only killed with a special spell that i never gave you in options
                               But this time it's given in the options try to recall the spells)

              """)
        self.spell=input("****Enter the spell**** => ")
        sleep(1)

        if self.spell.lower() in self.opt_spell:

            print("\n    Well done..!!! You just just saved this world from massive destruction")
            print("\n    You just killed LORD VOLDEMORT ")

            sleep(2)
            print("\n    You are the best wizard in this WORLD..!!!  ")

            print("\n\n        CONGRATULATIONS YOU WON THE GAME..!!  \n\n")
            self.prline()
            exit(1)


        else:

            print("\n    You used a wrong spell...How absent minded you are.....\n    You don't even remember which spells you USED \n    VOLDEMORT will become an unstoppalbe evil wizard \n    and cause a lot of destruction..!!!")
            return "death"


class death(scene):
#death scene
    def action(self):
        sleep(2)
        self.prline()
        print("""
                   You are knocked out. When you come to, you are a silvery misty version of yourself
                             looking down at your own limp body. You are a ghost.

              """)

        print("""

                                              GAME OVER
                                            YOU ARE DEAD..!!!
              """)

        sleep(1)
        print("\n    You are sent to Smeltings,   Sorry!!! \n\n\n")
        self.prline()
        exit(1)



class play(object):

    def __init__(self):


        self.current_sc=introduction()
        self.next_sc=''
        self.scene_plot={
                   'girls_bathroom':girls_bathroom(),
                   'dungeons':dungeons(),
                   'forbidden_for':forbidden_for(),
                   'chamber_of_sec':chamber_of_sec(),
                   'room_of_req':room_of_req(),
                   'central_stairs':central_stairs(),
                   'entrance_courtyard':entrance_courtyard(),
                   'death':death(),
                   }



    def letsplay(self):

        self.current_sc.rules()

        while self.current_sc!=0:


            self.next_sc=self.scene_plot[self.current_sc.action()]
            self.current_sc=self.next_sc


player=play()

player.letsplay()
