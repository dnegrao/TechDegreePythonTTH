# PLAYERS/TEAMS is to be treated as Constant since it's all CAPS
# import only system from os
from os import system
from os import name
from constants import PLAYERS
from constants import TEAMS
import random
import time

# define empty list of dictionary
cleaned_data_y = []
cleaned_data_n = []
temp_dict = {}
temp_dict_copy = {}
team_1 = []
team_2 = []
team_3 = []
current_players = []

# Height and Experience to be cleaned
# Height as int and Exp as boolean(True/False)

# define our clear function

# Using function created on:
# https://www.geeksforgeeks.org/clear-screen-python/


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def team_selection():
    for team in TEAMS:
        indx = TEAMS.index(team) + 1
        print(f"\n* {team} > {indx} ")
    return input("\nPlease select one of the above .. > ")


def team_display(team_1, team_2, team_3, user_selection):
    if user_selection == 1:
        time.sleep(.3)
        print("\nThis is the Panthers: ")
        print(f"\nTotal team players: {len(team_1)}")
        print(f"\nExperienced players in the team: {int(len(team_1)/2)}")
        print(f"Inexperienced players in the team: {int(len(team_1)/2)}")
        print(f"\nPlayers in the team: \n")
        current_players.clear()
        for item in team_1:
            current_players.append(item["name"])
        my_string = ", ".join(current_players)
        print(my_string)
        enter = input("\nPress Enter to Continue..")
        clear()
    elif user_selection == 2:
        time.sleep(.3)
        print(f"This is the Bandits: ")
        print(f"\nTotal team players: {len(team_2)}")
        print(f"\nExperienced players in the team: {int(len(team_2)/2)}")
        print(f"Inexperienced players in the team: {int(len(team_2)/2)}")
        print(f"\nPlayers in the team: \n")
        current_players.clear()
        for item in team_2:
            current_players.append(item["name"])
        my_string = ", ".join(current_players)
        print(my_string)
        enter = input("\nPress Enter to Continue..")
        clear()
    elif user_selection == 3:
        time.sleep(.3)
        print(f"This is the Warriors: ")
        print(f"\nTotal team players: {len(team_3)}")
        print(f"\nExperienced players in the team: {int(len(team_3)/2)}")
        print(f"Inexperienced players in the team: {int(len(team_3)/2)}")
        print(f"\nPlayers in the team: \n")
        current_players.clear()
        for item in team_3:
            current_players.append(item["name"])
        my_string = ", ".join(current_players)
        print(my_string)
        enter = input("\nPress Enter to Continue..")
        clear()


def clean_data(PLAYERS):
    for players in PLAYERS:
        temp_dict.clear()
        count = 0
        for item in players.items():
            # Adds a new item into the dictionary by passing the key and value
            temp_dict[item[0]] = item[1]
            count += 1
            if count == len(players.items()):
                # Transforms height into an Int
                height = temp_dict["height"]
                height, inches = height.split()
                temp_dict["height"] = int(height)
                # Transforms experience into boolean
                exp = temp_dict["experience"]
                if exp == "YES":
                    temp_dict["experience"] = True
# TODO (should be function)
# Copies the data to a dictionary and appends into cleaned data to either Y or N (should be function)
                    temp_dict_copy = temp_dict.copy()
                    cleaned_data_y.append(temp_dict_copy)
                elif exp == "NO":
                    temp_dict["experience"] = False
# TODO (should be function)
# Copies the data to a dictionary and appends into cleaned data to either Y or N
                    temp_dict_copy = temp_dict.copy()
                    cleaned_data_n.append(temp_dict_copy)


def balance_teams(cleaned_data_y, cleaned_data_n, TEAMS):
    player_num = ((len(cleaned_data_y) + len(cleaned_data_n)) /
                  (len(TEAMS))) / 2
#    players_per_team = len(cleaned_data) / len(TEAMS)
#    print(players_per_team)
    for team in TEAMS:
        if team == "Panthers":
            for i in range(int(player_num)):
                team_1.append(cleaned_data_y.pop())
                team_1.append(cleaned_data_n.pop())
        elif team == "Bandits":
            for i in range(int(player_num)):
                team_2.append(cleaned_data_y.pop())
                team_2.append(cleaned_data_n.pop())
        else:
            for i in range(int(player_num)):
                team_3.append(cleaned_data_y.pop())
                team_3.append(cleaned_data_n.pop())


def main_execution():

    clean_data(PLAYERS)
    balance_teams(cleaned_data_n, cleaned_data_y, TEAMS)

    while True:
        # TODO Menu should be in a function
        print("\nBASKETBALL TEAM STATS TOOL")
        time.sleep(1)
        clear()
        print("\n>>----- Main MENU -----<<")
        print("\nHere are your choices: ")
        print("\n1) Display Team Stats")
        print("2) Quit")

        user_selection = int(input("\nEnter an option > "))
        clear()

        if user_selection == 1:
            time.sleep(.4)
            user_selection = int(team_selection())
            clear()
            team_display(team_1, team_2, team_3, user_selection)
        elif user_selection == 2:
            time.sleep(.4)
            print("\nThank you for using the Basketball Status Tool..")
            time.sleep(.2)
            print("\nGood bye!")
            print("\n")
            break


# TODO - add the main function of the program here
# This will prevent it from executing when simply imported
if __name__ == '__main__':
    main_execution()
