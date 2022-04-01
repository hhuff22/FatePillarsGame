from pymongo import MongoClient
client = MongoClient()
db = client["project1"]
charDataColl = db["characters"]

class FireMage:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = level * 100
        self.experience = 0
        self.className = "Fire Mage"
        self.spellList = ["Fireball", "Firestorm"]

    def gainExperience(self, expAmount):
        print(f'You gain {expAmount} experience points.')
        self.experience += expAmount
        if self.experience >= 100:
            self.level += 1
            print('Level up!')
            print(f'Level: {self.level}')

    def takeDamage(self, baseDamage):
        print(f'You take {baseDamage} damage.')
        self.health = self.health - baseDamage
        print(f'Remaining health: {self.health}.')

    def spell1(self, currEnemy):
        print("")
        print(f'You cast Fireball, immolating {currEnemy.name}!')
        currEnemy.takeDamage(10)
        self.gainExperience(20)

    def spell2(self, currEnemy):
        ("")
        print(f'You cast Firestorm, enshrouding {currEnemy.name} in cinders!')
        currEnemy.takeDamage(15)
        self.gainExperience(25)

class IceMage:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = level * 100
        self.experience = 0
        self.className = "Ice Mage"
        self.spellList = ["Ice Shards", "Polar Ray"]

    def gainExperience(self, expAmount):
        print("")
        print(f'You gain {expAmount} experience points.')
        self.experience += expAmount
        if self.experience >= 100:
            self.level += 1
            print('Level up!')
            print(f'Level: {self.level}')

    def takeDamage(self, baseDamage):
        print(f'You take {baseDamage} damage.')
        self.health = self.health - baseDamage
        print(f'Remaining health: {self.health}.')

    def spell1(self, currEnemy):
        ("")
        print(f'You cast Ice Shards, pelting {currEnemy.name} with shards!')
        currEnemy.takeDamage(7)
        self.gainExperience(20)

    def spell2(self, currEnemy):
        ("")
        print(f'You cast Polar Ray, freezing {currEnemy.name} and reducing their attack!')
        currEnemy.takeDamage(5)
        self.gainExperience(25)

class LightningMage:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = level * 100
        self.experience = 0
        self.className = "Lightning Mage"
        self.spellList = ["Electrocute", "Static Discharge"]

    def gainExperience(self, expAmount):
        print("")
        print(f'You gain {expAmount} experience points.')
        self.experience += expAmount
        if self.experience >= 100:
            self.level += 1
            print('Level up!')
            print(f'Level: {self.level}')

    def takeDamage(self, baseDamage):
        print(f'You take {baseDamage} damage.')
        self.health = self.health - baseDamage
        print(f'Remaining health: {self.health}.')

    def spell1(self, currEnemy):
        ("")
        print(f'You cast Electrocute, sizzling {currEnemy.name}!')
        currEnemy.takeDamage(7)
        self.gainExperience(20)

    def spell2(self, currEnemy):
        ("")
        print(f'You cast Static Discharge, stunning {currEnemy.name}!')
        currEnemy.takeDamage(5)
        self.gainExperience(25)

class SullenWoman:
    def __init__(self):
        self.name = "Sullen Woman"
        self.health = 100

    def takeDamage(self, baseDamage):
        print(f'The {self.name} takes {baseDamage} damage.')
        self.health = self.health - baseDamage

    def flourish(self, currPlayer):
        ("")
        print(f'The {self.name} flourishes, cutting at your flesh!')
        currPlayer.takeDamage(20)

currentPlayer = ""
currentEnemy = ""
playerClass = ""

def loadScreen():
    print("")
    print("Welcome to Pillars of Fate~")
    print("")
    print("[1] - New Game")
    print("[2] - Load Game")

    gameChoice = input()
    global currentPlayer
    if int(gameChoice) == 1:
        intro()
    elif int(gameChoice) == 2:
        print("")
        print("Saved Characters:")
        for doc in charDataColl.find({}):
            print(doc["name"])
        print("")
        print("Select a character")
        selectedChar = input()
        for doc in charDataColl.find({}):
            if doc["name"] == selectedChar:
                if doc["class"] == 'FireMage':
                    currentPlayer = FireMage(doc["name"], doc["level"])
                    campaignStart()
                elif doc["class"] == 'IceMage':
                    currentPlayer = IceMage(doc["name"], doc["level"])
                    campaignStart()
                elif doc["class"] == 'LightningMage':
                    currentPlayer = LightningMage(doc["name"], doc["level"])
                    campaignStart()

        print("Character not found!")
        quit()
    else:
        print("Enter either 1 or 2")

def intro():
    print("")
    print("It's nighttime and thunder is roaring through the Morrison mansion.")
    print("The scene through your window is filled with furious winds blowing through the a dark glade.")
    print("Your uncle, who you're visiting from across the country, hasn't emerged from his room since dinner ended.")
    print("")
    print("Unable to sleep, you creep into the library down the hall.")
    print("The walls are lined with bookshelves, each filled to the ceiling with books -- the library is a grand wonder to behold.")
    print("Two distinctly decorated ornate books stand out among the rest, an orange book and a green one.")
    print("")
    print("[1] - Open the orange book.")
    print("[2] - Open the green book.")

    while True:
        orangeOrGreen = input()
        try:
            if int(orangeOrGreen) == 1 or 2:
                print("You turn the thick pages of the book but find that nothing is printed onto them.")
                print("")
                print("With a sudden flash, your surrounding are illuminated and you silently slip into a deep sleep.")
                break
            else:
                print("Enter either 1 or 2:")
        except:
            print("Value must be whole number 1 or 2:")

    print("You awaken in a dusty tomb dimly lit by a set of torches on either side of its walls.")
    print("")
    print("A piercing voice rumbles through your head.")
    print("Who are you?")

    playerName = input()

    print("After revealing your name, a surge of memories that are not your own fill you head.")
    print("You remember that this is the world of Celeron and you were one of a group of powerful magii...")
    print("That is, before you were defeated by the Lord of Lies and placed into an eternal slumber, trapped in the tomb of Verity.")
    print("")
    print("There is no telling what events have led to your awakening, but you know you must escape.")
    print("You begin to remember what abilities you wielded in the fight against corruption.")
    print("You were...")

    def setCurrentPlayer():
        global currentPlayer
        if playerClass == "Fire Mage":
            currentPlayer = FireMage(playerName, 1)
            print("")
            print("You are " + playerName + ", the Fire Mage.")
            campaignStart()
        elif playerClass == "Ice Mage":
            currentPlayer = IceMage(playerName, 1)
            print("")
            print("You are " + playerName + ", the Ice Mage.")
            campaignStart()
        elif playerClass == "Lightning Mage":
            currentPlayer = LightningMage(playerName, 1)
            print("")
            print("You are " + playerName + ", the Lightning Mage.")
            campaignStart()

    def chooseClass():
        global playerClass
        print("")
        print("Choose a class:")
        print("")
        print("[1] - Fire Mage")
        print("[2] - Ice Mage")
        print("[3] - Lightning Mage")
        chosenClass = input()

        if int(chosenClass) == 1:
            print("")
            print("Fire mages are the most powerful of their peers, unleashing searing hot flames to decimate their opponents.")
            print("")
            print("Will you choose this class?")
            print("")
            print("[1] - Yes")
            print("[2] - No")
            confirmClass = input()
            if int(confirmClass) == 1:
                playerClass = "Fire Mage"
                setCurrentPlayer()
                return
            elif int(confirmClass) == 2:
                chooseClass()
            else:
                print("Enter either 1 or 2:")
        elif int(chosenClass) == 2:
            print("")
            print("Ice mages control the battle by enfeebling their opponents while defeating them.")
            print("")
            print("Will you choose this class?")
            print("")
            print("[1] - Yes")
            print("[2] - No")
            confirmClass = input()
            if int(confirmClass) == 1:
                playerClass = "Ice Mage"
                setCurrentPlayer()
                return
            elif int(confirmClass) == 2:
                chooseClass()
            else:
                print("Enter either 1 or 2:")
        elif int(chosenClass) == 3:
            print("")
            print("Lightning mages possess the most cunning and are able to prevent opponents from taking turns.")
            print("")
            print("Will you choose this class?")
            print("")
            print("[1] - Yes")
            print("[2] - No")
            confirmClass = input()
            if int(confirmClass) == 1:
                playerClass = "Lightning Mage"
                setCurrentPlayer()
                return
            elif int(confirmClass) == 2:
                chooseClass()
            else:
                print("Enter either 1 or 2:")
        else:
            print("Enter either 1, 2, or 3:")

    chooseClass()

def nextAction():
    print("")
    print("[1] - Check status")
    print("[2] - Go forth")
    print("[3] - Save & Quit")
    nextChoice = input()

    if int(nextChoice) == 1:
        print("")
        print(currentPlayer.name)
        print("")
        print(f'Level {currentPlayer.level} {currentPlayer.className}')
        nextAction()
    elif int(nextChoice) == 2:
        print("")
        print("You venture forth into the darkness...")
        match campaignPart:
            case 0:
                Part1()
            case 1:
                Part2()
            case 2:
                Part3()
            case 3:
                Part4()
            case 4:
                Part5()
            case _:
                print("?")
    elif int(nextChoice) == 3:
        print("")
        previousCharData= { "name": currentPlayer.name }
        charDataColl.delete_one(previousCharData)
        currentCharData = {"class": type(currentPlayer).__name__, "name": currentPlayer.name, "level": currentPlayer.level}
        charDataColl.insert_one(currentCharData)
        quit()
    else:
        print("Enter either 1, 2 or 3")

def campaignStart():
    global campaignPart
    campaignPart = 0

    print("")
    print("The torchlight flickers, illuminating the dark tomb around you.")
    print("")
    print("Before you is a monumental stone door.")
    nextAction()

def Part1():
    global campaignPart
    campaignPart = 1
    print("pushing open the stone door to reveal a sprawling staircase.")
    print("")
    print("At the peak of the staircase you meet a sullen woman.")
    print("")
    print("She sternly says 'None are allowed to enter the Clocktower without express permission from the Lord of Lies.")
    print("'No matter. Your meaningless existence ends here.'")
    print("")
    print("The sullen woman brandishes her longsword, forcing you to defend yourself.")

    currentEnemy = SullenWoman()

    while True:
        print("")
        print("Choose a spell:")
        print("")
        print(f'1 - {currentPlayer.spellList[0]}')
        print(f'2 - {currentPlayer.spellList[1]}')
        spellChoice = input()
        match int(spellChoice):
            case 1:
                currentPlayer.spell1(currentEnemy)
            case 2:
                currentPlayer.spell2(currentEnemy)
            case _:
                print("?")

        if currentEnemy.health <= 0:
            break

        print("")
        print(f'The {currentEnemy.name} brandishes her sword.')
        currentEnemy.flourish(currentPlayer)

        if currentPlayer.health <= 0:
            print("You died...")
            print("")
            print("Game Saved.")
            previousCharData= { "name": currentPlayer.name }
            charDataColl.delete_one(previousCharData)
            currentCharData = {"class": type(currentPlayer).__name__, "name": currentPlayer.name, "level": currentPlayer.level}
            charDataColl.insert_one(currentCharData)
            loadScreen()

    print("You've killed the Sullen Woman...")

loadScreen()