from os import system
from os import name
from constants import PLAYERS
from constants import TEAMS
import time

cleaned_data_y = []
cleaned_data_n = []
temp_dict = {}
temp_dict_copy = {}
team_1 = []
team_2 = []
team_3 = []
current_players = []
current_guard = []
sum_height = 0


# Screen clear function (only for presentation purpose)
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
        print(f"\n{indx}) {team}")
    return input("\nPlease select one of the above .. > ")


def team_print(team, user_selection):
    exp_pl = 0
    ine_pl = 0
    current_players.clear()
    current_guard.clear()
    sum_height = 0

    if user_selection == 1:
        team_selected = "Panthers"
    elif user_selection == 2:
        team_selected = "Bandits"
    elif user_selection == 3:
        team_selected = "Warriors"

    for item in team:
        current_players.append(item["name"])
        current_guard.append(item["guardians"])
        sum_height = sum_height + item["height"]
        if item["experience"] == True:
            exp_pl += 1
        elif item["experience"] == False:
            ine_pl += 1
    avg = int(sum_height) / int(len(team_1))
    avg = float("{:.2f}".format(avg))

    time.sleep(.3)

    print(f"\nYour selection: {team_selected}")
    print(f"\nTotal team players: {len(team)}")
    print(
        f"\nExperienced players in the team: {exp_pl} -> {int((exp_pl/len(team))*100)}%")
    print(
        f"Inexperienced players in the team: {ine_pl} -> {int((ine_pl/len(team))*100)}%")
    print(f"Average height in the team: {avg}")
    print(f"\n---> Players in the team: \n")

    my_string = ", ".join(current_players)
    print(my_string)

    print(f"\n---> Guardians in the team: \n")
    my_string = ", ".join(current_guard)
    print(my_string)
    enter = input("\nPress Enter to Continue..")
    clear()


def team_display(team_1, team_2, team_3, user_selection):
    if user_selection == 1:
        team_print(team_1, user_selection)
    elif user_selection == 2:
        team_print(team_2, user_selection)
    elif user_selection == 3:
        team_print(team_3, user_selection)


def clean_data(PLAYERS):
    for players in PLAYERS:
        temp_dict.clear()
        count = 0
        for item in players.items():
            # Adds a new item into the dictionary by passing the key and value
            temp_dict[item[0]] = item[1]
            count += 1
            if count == len(players.items()):
                # Split Guardians
                if "and" in temp_dict["guardians"]:
                    split_guard = temp_dict["guardians"]
                    split_guard = split_guard.split("and")
                    split_guard = ", ".join(split_guard)
                    temp_dict["guardians"] = split_guard
                # Transforms height into an Int
                height = temp_dict["height"]
                height, inches = height.split()
                temp_dict["height"] = int(height)
                # Transforms experience into boolean
                exp = temp_dict["experience"]
                if exp == "YES":
                    temp_dict["experience"] = True
# Copies the data to a dictionary and appends into cleaned data to either Y or N (should be function)
                    temp_dict_copy = temp_dict.copy()
                    cleaned_data_y.append(temp_dict_copy)
                elif exp == "NO":
                    temp_dict["experience"] = False
# Copies the data to a dictionary and appends into cleaned data to either Y or N
                    temp_dict_copy = temp_dict.copy()
                    cleaned_data_n.append(temp_dict_copy)


def balance_teams(cleaned_data_y, cleaned_data_n, TEAMS):
    player_num = ((len(cleaned_data_y) + len(cleaned_data_n)) /
                  (len(TEAMS))) / 2

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


def error_teams():
    clear()
    print("\n")
    print("\n")
    print("Please use only 1, 2 or 3 for your selection..Try again")
    time.sleep(1)
    clear()


def error_action():
    print("\n")
    print("\nPlease use only 1 or 2 for your selection..Try again")
    time.sleep(1)


def main_execution():

    clean_data(PLAYERS)
    balance_teams(cleaned_data_n, cleaned_data_y, TEAMS)

    clear()

    print("\n----->BASKETBALL")
    time.sleep(.5)
    print("------->>TEAM")
    time.sleep(.5)
    print("------->>>STATS")
    time.sleep(.5)
    print("------->>>>>TOOL")
    time.sleep(1)
    clear()

    while True:
        clear()
        # TODO Menu should be in a function
        print("\n>>----- Main MENU -----<<")
        print("\nHere are your choices: ")
        print("\n1) Display Team Stats")
        print("2) Quit")

        try:
            user_selection = int(input("\nEnter an option > "))
        except ValueError:
            clear()
            error_action()
            continue

        clear()

        if user_selection == 1:
            time.sleep(.4)
            while True:
                try:
                    user_selection = int(team_selection())
                    if user_selection == 1 or user_selection == 2 or user_selection == 3:
                        break
                    else:
                        error_teams()
                        continue
                except ValueError:
                    error_teams()
                    continue
            clear()
            team_display(team_1, team_2, team_3, user_selection)
        elif user_selection == 2:
            time.sleep(.4)
            print("\nThank you for using the Basketball Status Tool..")
            time.sleep(.2)
            print("\nGood bye!")
            print("\n")
            break
        else:
            error_action()
            continue


if __name__ == '__main__':
    main_execution()
