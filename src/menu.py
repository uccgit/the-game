'''
Menu System for game play. There should be a variety of different menus
'''

locations = ["The Field", "The Tavern", "Your House"]



def main_menu():
    '''Very basic main menu'''
    choice = ''
    while choice != '3':
        print "\n[1] Enter 1 to travel."
        print "[2] Enter 2 to explore."
        print "[3] Enter 3 to quit."

        choice = raw_input("\nWhat would you like to do? ")

        if choice == '1':
            travel_menu()
        elif choice == '2':
            print "You see a person standing next to you"
        elif choice == '3':
            print "Thanks for playing"
        else:
            print "I don't understand, please try again"

def travel_menu():
    '''Travel Menu'''
    choice = ''
    while choice != '5':
        print "\n[1] Enter 1 to explore"
        print "[2] Enter 2 to run"
        print "[3] Enter 3 to look around"
        print "[4] Enter 4 to leave area"
        print "[5] Enter 5 to return to main menu"

        choice = raw_input("\nWhat would you like to do? ")

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
