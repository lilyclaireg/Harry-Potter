
"""
Author:         Lily Claire Gibson-Grossmann
Date:           4/19/2024
Assignment:     Role Play Game (RPG) Project: The Knock Off Harry-Potter Game
Course:         CPSC1051
Lab Section:    SECTION 01

CODE DESCRIPTION: This is a Harry Potter game where you are Harry and Ginny's child who is going to Hogwarts.
Your time starts off great getting settled and sorted into your house! Things take a turn when Hagrid is trapped by a troll and needs your help.
In the game you will learn spells to prepare for battle, and then battle the troll to save Hagrid. 

GITHUB LINK: https://github.com/lilyclaireg/Harry-Potter

"""

# Class 'room' that creates a room object
class Room:
    # Initializes room
    def __init__(self, username, userdescription, userexits):
        self.name = username
        self.description = userdescription
        self.exits = userexits
    # Returns name
    def get_name(self):
        return self.name
    # Returns description
    def get_description(self):
        return self.description
    # Returns exits in an array form
    def get_exits(self):
        return self.exits
    # Returns exits as a string 
    def list_exits(self):
        exit_string = ""
        for i in range(len(self.exits)):
            exit_string += self.exits[i]
            exit_string += "\n"
        return exit_string
    # Returns string representation of room
    def __str__(self):
        stringDes = "Current Room Name: "
        stringDes += self.get_name()
        stringDes += "\nDescripton: "
        stringDes += self.get_description()
        return stringDes
    
# Class map creates map object
class Map:
    #INitializes map, adds rooms, and returns rooms
    def __init__(self):
        self.map = {}
    def add_room(self, room):
        self.map[room.get_name().lower()] = room
    def get_room(self, room_name):
        return self.map.get(room_name)

# Player class that sets and returns name
class Player:
    def __init__(self):
        self.name = ""
    def set_name(self, username):
        self.name = username
    def get_name(self):
        return self.name
    
# Inheritance of player class (a player with a house is a player) that sets and returns the house name
class PlayerHouse(Player):
    def __init__(self):
        Player.__init__(self)
        self.house_name = ""
    def set_house_name(self, name):
        self.house_name = name
    def get_house_name(self):
        return self.house_name

# Main
def main():
    # Initialzes player and map and creates necessary booleans
    map = Map()
    player = PlayerHouse()
    helpingHagird = False
    bedroomDone = False
    gardenDone = False
    dining_hallDone = False
    classroomDone = False
    validExit = False

    # Creates instances of the rooms I will use and adds them to the map
    bedroom = Room("Bedroom", "Your bedroom is made of grey stone, with touches of your house color bringing color to the room. Your bed and dresser take up most of the room, but you have a window overlooking all of Hogwarts.", ["Garden", "Dining Hall", "Classroom"])
    garden = Room("Garden", "The garden still looks like Harry remembers it... Pots, plants, and dirt covering all of the greenhouse! There is peace to the chaos, though.", ["Bedroom", "Dining Hall", "Classroom"])
    dining_hall = Room("Dining Hall", "The dining hall is lit by chandeliers made of candles, with tables lining all of the room! The professors tables are at the front of the hall, like the head of the table.", ["Bedroom", "Garden", "Classroom"])
    classroom = Room("Classroom", "The classroom is big, spacious, with high celings and papers flying (literally) everywhere! There is anything and everything you could imagine a classroom to need!", ["Bedroom", "Garden", "Dining Hall"])
    map.add_room(bedroom)
    map.add_room(garden)
    map.add_room(dining_hall)
    map.add_room(classroom)
    
    # Prints title and backgroud
    print("\n\t*** KNOCK OFF HARRY POTTER GAME ***")
    print("\t   Lily Claire Gibson-Grossmann\n\t     CPSC 1050 Final Project\n\t Clemson University, Dr. Adkins\n\n")
    print("Background: You are one of Harry and Ginny's kids. They have been wanting you to go to Hogwarts, but you never wanted to. Too much studying!")
    print("One day, you got into big trouble at school... Turns out you can't make your peers pay you to put a love spell on their crushes... Darn!")
    print("After talking with eachother, they decided Hogwarts is best for you so you can continue doing magic, but safely and legally.")

    # Prompts user for name and sets this to be their name
    print("Now, after getting onto Platform 9 3/4, you are on your way!\n\n")
    print("Hagrid: Welcome to Hogwarts! Today is your first day... Are you excited? Well, thats enough, this way! What is your name again? ")
    user_input = input().strip()
    user_input += " Potter"
    player.set_name(user_input)

    # Sorts the player in their house based on their answer to the sorting hat's question
    print(f"\nHagrid: Great to meet you, {player.get_name()}! Let's go to the dining hall so we can eat... and find out your house!")
    print("You and Hagrid enter the dining hall, and you sit next to some friends you met on the train. It is now time for the sorting hat ceremony.")
    print(f"\nHagrid: All right, first up is {player.get_name()}! How fitting.")
    print(f"Sorting Hat: Hello, {player.get_name()}. Hmm interesting, very interesting... What oh what could you be? I have a question for you! How do you want to be remembered: wise, kind, successful, or brave? ")
    user_answer = input().strip()
    while user_answer.lower() != "kind" and user_answer.lower() != "successful" and user_answer.lower() != "wise" and user_answer.lower() != "brave":
        print("Please enter 'wise', 'kind', 'successful', or 'brave': ", end = '')
        user_answer = input().strip()
    if user_answer.lower() == "kind":
        player.set_house_name("Hufflepuff")
    elif user_answer.lower() == "brave":
        player.set_house_name("Gryffindor")
    elif user_answer.lower() == "wise":
        player.set_house_name("Ravenclaw")
    elif user_answer.lower() == "successful":
        player.set_house_name("Slytherin")
    print(f"\nSorting Hat: Ahhh, I see! You are a {player.get_house_name()}!")
    print("Congrats! Now, it's time for bed... You go back to your bedroom.")

    # User can interact with their notebook; will use this in game regardless
    print("\nYou notice a book on your bed that wasn't there before. Do you want to open it?")
    open_notebook = input().strip()
    while open_notebook.lower() != 'yes' and open_notebook.lower() != 'no':
        print("Please enter 'yes' or 'no': ", end = '')
        open_notebook = input().strip()
    if open_notebook.lower() == 'no':
        print("The notebook opens on its own! It reads: ")
    else:
        print("You open the notebook. It reads: ")

    # Writes and reads to the spell notebook
    with open("spellnotebook.txt", "w") as spell_notebook:
        spell_notebook.write("Spell Notebook: ")
    with open("spellnotebook.txt", "r") as spell_notebook:
        notebookLines = spell_notebook.readlines()
        for i in range(len(notebookLines)):
            print(notebookLines[i])

    # Prompts user until the user has agreed to help save Hagrid (mission of game)
    print("\n\t\tTHE NEXT DAY")
    print(f"You see a note from Hagrid! It reads:\n\"Dear {player.get_name()}, Please help me! I'm locked in the girls bathroom on the first floor... There is a troll trying to get me! \nI've asked a friend owl to take this note to you. You need to learn 4 spells to help rescue me.\"")
    print("\nOh no, Hagrid needs your help. But that means you will miss your first day of class, what will your parents think?")
    while helpingHagird == False:
        print("Do you want to help Hagrid? (yes or no): ", end = '')
        choice = input().strip()
        if choice.lower() == "no":
            print("Oh no, the troll ends up eating Hagrid! AND your parents are disappointed in you for not helping a friend! Try again...")
        elif choice.lower() == "yes":
            print("Good choice!\n")
            helpingHagird = True
        else:
            print("Please type yes or no.")

    # While the player hasn't 'solved' all four rooms, the loop will execute
    current_room = bedroom
    while ((bedroomDone == False) or (gardenDone == False) or (dining_hallDone == False) or (classroomDone == False)):
        # Prints current room
        print(f'{current_room}')
        # User completes bedroom to learn lumos spell
        if bedroomDone == False and current_room == bedroom:
            while (bedroomDone == False):
                print("You see a spell on a piece of paper laying on your bed. Do you want to write it down?")
                write_down = input().strip()
                while write_down.lower() != 'yes' and write_down.lower() != 'no':
                    print("Please enter yes or no: ", end = '')
                    write_down = input().strip()
                if write_down.lower() == 'yes':
                    print("Good choice! You learned the spell 'lumos', which creates light with your wand!")
                    with open("spellnotebook.txt", "a") as spell_notebook:
                        spell_notebook.write("Lumos, ")
                    bedroomDone = True
                elif write_down.lower() == 'no':
                    print("Oh no... This spell is needed to help Hagrid! Please try again.")
                

        # User completes garden to learn confringo spell
        elif gardenDone == False and current_room == garden:
            while (gardenDone == False):
                print("You see a spell written on a piece of cloth by the Mandrakes. Do you want to write it down?")
                write_down = input().strip()
                while write_down.lower() != 'yes' and write_down.lower() != 'no':
                    print("Please enter yes or no: ", end = '')
                    write_down = input().strip()
                if write_down.lower() == 'yes':
                    print("Good choice! You learned the spell 'confringo', which creates an explosion at the enemy you're fighting!")
                    with open("spellnotebook.txt", "a") as spell_notebook:
                        spell_notebook.write("Confringo, ")
                    gardenDone = True
                elif write_down.lower() == 'no':
                    print("Oh no... This spell is needed to help Hagrid! Please try again.")
                

        # User completes dining hall to learn reparo spell
        elif dining_hallDone == False and current_room == dining_hall:
            while (dining_hallDone == False):
                print("You see a spell written on a leftover menu. Do you want to write it down?")
                write_down = input().strip()
                while write_down.lower() != 'yes' and write_down.lower() != 'no':
                    print("Please enter yes or no: ", end = '')
                    write_down = input().strip()
                if write_down.lower() == 'yes':
                    print("Good choice! You learned the spell 'reparo', which can repair objects, such as a broken wand!")
                    with open("spellnotebook.txt", "a") as spell_notebook:
                        spell_notebook.write("Reparo, ")
                    dining_hallDone = True
                elif write_down.lower() == 'no':
                    print("Oh no... This spell is needed to help Hagrid! Please try again.")
                

        # User completes classroom to learn expelliarmus spell
        elif classroomDone == False and current_room == classroom:
            while (classroomDone == False):
                print("You see a spell flying through the classroom as a paper plane. Do you want to write it down?")
                write_down = input().strip()
                while write_down.lower() != 'yes' and write_down.lower() != 'no':
                    print("Please enter yes or no: ", end = '')
                    write_down = input().strip()
                if write_down.lower() == 'yes':
                    print("Good choice! You learned the spell 'expelliarmus', which knocks your enemy's weapon out of their hand!")
                    with open("spellnotebook.txt", "a") as spell_notebook:
                        spell_notebook.write("Expelliarmus, ")
                    classroomDone = True
                elif write_down.lower() == 'no':
                    print("Oh no... This spell is needed to help Hagrid! Please try again.")
                
        
        # If all puzzles are done, it won't execute the branch to ask player which exit to choose
        validExit = False
        if (bedroomDone == True) and (gardenDone == True) and (dining_hallDone == True) and (classroomDone == True):
            validExit = True
        # If all puzzles are not done, it will ask the player which room to go to next
        while validExit == False:
            print("\nWhat room do you want to enter next?")
            print(current_room.list_exits())
            nextRoom = input().strip()

            # Validates response 
            while nextRoom.lower() != "bedroom" and nextRoom.lower() != "dining hall" and nextRoom.lower() != "garden" and nextRoom.lower() != "classroom":
                print("Please enter valid exit: ", end = '')
                nextRoom = input().strip()
            
            # Ensures that the room the player choose isn't already done 
            if nextRoom.lower() == "bedroom":
                if bedroomDone == False:
                    current_room = bedroom
                    validExit = True
                else:
                    print("You've already found the spell in the bedroom!")
            elif nextRoom.lower() == "dining hall":
                if dining_hallDone == False:
                    current_room = dining_hall
                    validExit = True
                else:
                    print("You've already found the spell in the dining hall!")
            elif nextRoom.lower() == "garden":
                if gardenDone == False:
                    current_room = garden
                    validExit = True
                else:
                    print("You've already found the spell in the garden!")
            elif nextRoom.lower() == "classroom":
                if classroomDone == False:
                    current_room = classroom
                    validExit = True
                else:
                    print("You've already found the spell in the classroom!")

    # Prints the updated notebook with all the spells
    print("\nYou found all of the spells! You open your notebook to now see: ")
    with open("spellnotebook.txt", "r") as spell_notebook:
        notebookLines = spell_notebook.readlines()
        for i in range(len(notebookLines)):
            print(notebookLines[i])
    
    # Mission to rescue hagrid; the user will be asked four questions and has to type the correct spell before going to the next question.
    # Once all the spells are used, hagrid is saved and the game is over!
    print("\n\tTIME TO RESCUE HAGRID!\nYou go to the bathroom to see Hagrid cornered by the TROLL! The troll turns and sees you!")
    print("Quick! Use the spell that will knock the troll's club out of his hand!")
    spell1 = input().strip()
    while spell1.lower() != "expelliarmus":
        print("That is not the spell! Try again: ")
        spell1 = input().strip()
    print("Great work! Now attack the troll with an explosion!")
    spell2 = input().strip()
    while spell2.lower() != "confringo":
        print("That is not the spell! Try again: ")
        spell2 = input().strip()
    print("Oh no! He fell and you heard a crash, but all the lights went out... Use a spell to create light!")
    spell3 = input().strip()
    while spell3.lower() != "lumos":
        print("That is not the spell! Try again: ")
        spell3 = input().strip()
    print("With light, you see you've killed the troll! Hagrid has been hurt, however. His arm is broken! Use a spell to help him!")
    spell4 = input().strip()
    while spell4.lower() != "reparo":
        print("That is not the spell! Try again: ")
        spell4 = input().strip()
    print("Aha! Hagrid's arm is healed, but it seems all of his bones are gone! He giggles, muttering 'fitting' to himself, but you're not sure what he means...")
    print("\n\t*** YOU SAVED HAGRID AND WON THE GAME ***\n\n")

# Runs main
if __name__ == "__main__":
    main()