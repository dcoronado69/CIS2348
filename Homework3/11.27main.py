#This is 11.27 ZyBooks
#David Coronado: People Soft ID: 1971072
def printRoster():
    # get all players jersey numbers
    keys = list(players.keys())

    # sort jersey numbers in ascending order
    keys.sort()

    # print roster
    print("ROSTER")
    for key in keys:
        print("Jersey number: %d, Rating: %d" % (key, players[key]))


# define a dictionary to store players jersey number as keys and rating as values
players = {}

# iterate for loop 5 times
for i in range(5):
    # ask user to enter player (i+1)'s jersey number and read
    jno = int(input("Enter player %d's jersey number:\n" % (i + 1)))

    # ask user to enter player (i+1)'s rating and read
    players[jno] = int(input("Enter player %d's rating:\n" % (i + 1)))

    # print new line
    print("")

printRoster()

# iterate while loop
while True:

    # print menu
    print(
        "\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n")

    # read user option
    option = input("Choose an option:\n")

    # if user option is o call printRoster() function to print roster
    if option == 'o':
        printRoster()

    # if user option is 'a'
    elif option == 'a':
        # read new player's jersey number
        jno = int(input("Enter a new player's jersey number:\n"))

        # read new player's rating
        rating = int(input("Enter the player's rating:\n"))

        # add player details into players dictionary
        players[jno] = rating

    # if user option is 'd'
    elif option == 'd':
        # read a player's jersey number
        jno = int(input("Enter a player's jersey number:\n"))

        # check a player with the given jersey number is present in the dictionary
        if jno in list(players.keys()):
            # delete player
            del players[jno]

    # if user option is 'u'
    elif option == 'u':
        # read a player's jersey number
        jno = int(input("Enter a player's jersey number:\n"))

        # read new player's rating
        rating = int(input("Enter a new rating for player:\n"))

        # update player details into players dictionary
        players[jno] = rating

    elif option == 'r':
        # read a rating
        rating = int(input("Enter a rating:\n"))

        # get all players jersey numbers
        keys = list(players.keys())

        # sort jersey numbers in ascending order
        keys.sort()

        # print players above given rating
        print("\nABOVE %d" % (rating))

        count = 0
        for key in keys:
            # print player's jersey number, and rating
            if (players[key] > rating):
                print("Jersey number: %d, Rating: %d" % (key, players[key]))

                # increment count by 1
                count += 1

        # if no players have above given rating, print error message
        if (count == 0):
            print("No players found above %d rating" % (rating))

    # if user option is q then stop the program
    if option == "q":
        break
