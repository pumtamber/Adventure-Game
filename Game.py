import time
import random
list_item = []



def time_pause(a):
    print(a)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            time_pause("Sorry, I don't understand.")
    return response


def intro(option):
    time_pause("You find yourself standing in an open field, filled")
    time_pause("with grass and yellow wildflowers.")
    time_pause("Rumor has it that a " + option + " is somewhere around ")
    time_pause("here, and has been terrifying the nearby village.")
    time_pause("In front of you is a house.\n")
    time_pause("To your right is a dark cave.\n")
    time_pause("In your hand you hold your trusty (but not very ")
    time_pause("effective) dagger.\n")


def house(option):
    # Things that happen to the player in the house
    time_pause("You approach the door of the house.")
    time_pause("You are about to knock when the door opens")
    time_pause("and out steps a "+option+".")
    if "Sword of Ogoroth!" not in list_item:
        time_pause("You feel a bit under-prepared for this, ")
        time_pause("what with only having a tiny dagger.\n")
    while True:
        time_pause("Do you want to fight or run away?")
        time_pause("Press 1 to fight.")
        time_pause("Press 2 to Run away.")
        fight = valid_input("Please enter your input: \n", "1", "2")
        if fight == "1":
            if "Sword of Ogoroth!" in list_item:
                time_pause("As the " + option + " moves to attack,")
                time_pause("you unsheath your new sword.")
                time_pause("The Sword of Ogoroth shines brightly in ")
                time_pause("your hand as you brace yourself for the attack.")
                time_pause("But the " + option + " takes one look at ")
                time_pause("your shiny new toy and runs away!")
                time_pause("You have rid the town of the " + option + ". ")
                time_pause("You are victorious!\n")
                play_again(option)
            else:
                time_pause("You do your best...")
                time_pause("but your dagger is no match for the " + option + ".")
                time_pause("You have been defeated!\n")
                play_again(option)
                break
        if fight == "2":
            time_pause("You run back into the field. ")
            time_pause("Luckily, you don't seem to have been followed.\n")
            field(option)
            break


def cave(option):
    # Things that happen to the player in the cave
    time_pause("You peer cautiously into the cave.")
    time_pause("It turns out to be only a very small cave.")
    time_pause("Your eye catches a glint of metal behind a rock.")
    time_pause("You have found the magical Sword of Ogoroth!")
    time_pause("You discard your silly old dagger and ")
    time_pause("take the sword with you.")
    time_pause("You walk back out to the field.")
    list_item.append("Sword of Ogoroth!")
    field(option)


def field(option):
    # Things that happen to the player in the field
    time_pause("You find yourself in a dark dungeon.")
    time_pause("In front of you are two passageways.")
    time_pause("Enter 1 to knock on the door of the house.")
    time_pause("Enter 2 to peer into the cave.")
    game_choice = valid_input("Please enter your input: ", "1", "2")

    if game_choice == "1":
        house(option)
    elif game_choice == "2":
        cave(option)


def play_again(option):
    time_pause("Do you want play again?")
    time_pause("Press y for Yes.")
    time_pause("Press n for No.")
    playagain = valid_input("Please enter your input: ", "y", "n")
    if playagain == "y":
        intro(option)
        field(option)
    else:
        time_pause("Thank you for playing.")


random_choice = random.choice(["wicked fairie", "pirate", "dragon", "troll", "gorgon"])

intro(random_choice)
field(random_choice)
