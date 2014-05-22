import os
# This is the menu system for the game
# The plan is to create custom menus where needed


def display_title_bar():
    #clears the terminal screen, and displays a title bar
    os.system('cls' if os.name == 'nt' else 'clear')
    print "\t*******************************************"
    print "\t***  Welcome - The game is an adventure ***"
    print "\t*******************************************"


def main_menu_choice():
    print "\n[1] Start A New Game."
    print "[2] Continue Your Game."
    print "[3] Quit The Game."
    return raw_input("What would you like to do? ")


def travel_menu_choice():
    print "\n[1] Enter 1 to explore"
    print "[2] Enter 2 to run"
    print "[3] Enter 3 to look around"
    print "[4] Enter 4 to leave area"
    print "[5] Enter 5 to return to main menu"
    return raw_input("What would you like to do? ")


def main_menu():
    '''Very basic main menu'''

    choice = ''
    while choice != '3':
        choice = main_menu_choice()
        display_title_bar()
        if choice == '1':
            travel_menu()
        elif choice == '2':
            print "You see a person standing next to you"
        elif choice == '3':
            exit(0)
        else:
            print "I don't understand, please try again"


def travel_menu():
    '''Travel Menu'''
    choice = ''
    while choice != '5':
        choice = travel_menu_choice()
        display_title_bar()
        if choice == '1':
            print "You explore the", locations[0], "but find nothing"
        elif choice == '2':
            print "You run and hide"
        elif choice == '3':
            print "You look around and see something"
        elif choice == '4':
            print "You have chosen to leave this area"
        elif choice == '5':
            main_menu()
        else:
            break

main_menu()
