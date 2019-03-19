# ASCII frames are heavily inspired by https://www.asciiart.eu/art-and-design/borders
import constants
import os
from typing import List, Dict


def cls() -> None:
    # short cls snippet from https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """
    Simple function to clear the console
    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    # header taken from http://www.asciiworld.com/-Basketball,16-.html
    print(" _               _        _   _           _ _")
    print("| |__   __ _ ___| | _____| |_| |__   __ _| | |")
    print("| '_ \ / _` / __| |/ / _ \ __| '_ \ / _` | | |")
    print("| |_) | (_| \__ \   <  __/ |_| |_) | (_| | | |")
    print("|_.__/ \__,_|___/_|\_\___|\__|_.__/ \__,_|_|_|")


def print_main_menu() -> None:
    """
    Function takes no arguments
    Responsible only for printing the menu for the user
    Use an even number for the width!
    :return: None
    """
    width: int = 38
    border: str = "||"
    cls()
    print_header()
    print()
    print("=" * width)
    print_framed_text(width, border, "")
    print_framed_text(width, border, "-- MENU --", True)
    print_framed_text(width, border, "")
    print_framed_text(width, border, "Enter an option:")
    print_framed_text(width, border, "1) Display Team stats")
    print_framed_text(width, border, "2) Quit")
    print_framed_text(width, border, "")
    print("=" * width)


def print_stats_menu() -> None:
    """
    Function to print the list of teams to choose from
    :return: None
    """
    width: int = 38
    border = "||"
    print_header()
    print()
    print("=" * width)
    print_framed_text(width, border)
    print_framed_text(width, border, "Our Teams:", True)
    print_framed_text(width, border)

    i = 1
    for team in constants.TEAMS:
        print_framed_text(width, border, f"{i}) {team}")
        i += 1
    print_framed_text(width, border)
    print("=" * width)


def print_team_stats(team: Dict):
    """
    Function to print statistics for a given team
    :param team: Dict contains the information for the team displayed
    :return:
    """
    average_height: float = get_average_height(team)
    average_height_str: str = str(round(average_height, 2))
    if not len(average_height_str) % 2:
        average_height_str += "0"
    width: int = 180
    border: str = "| |"
    print(width * "-")
    print(width * "-")
    print_framed_text(width, border)
    team_name = team["name"]
    if len(team_name) % 2:
        team_name = team_name + " "
    print_framed_text(width, border, f"Team stats for: {team_name}", True)
    print_framed_text(width, border, f"{'-' * 30}", True)
    print_framed_text(width, border)
    total_players = len(team["exp_players"]) + len(team["no_exp_players"])
    print_framed_text(width, border, f"Total players: {total_players}    " +
                      f" Average height: {average_height_str}", True, 25)
    print_framed_text(width, border, f"Experienced players: {len(team['exp_players'])}", True)
    print_framed_text(width, border, f"Inexperienced players: {len(team['no_exp_players'])}", True)
    player_names: List = [player["name"] for player in team["exp_players"]]
    player_names.extend([player["name"] for player in team["no_exp_players"]])
    names = ", ".join(player_names)
    print_framed_text(width, border)
    print_framed_text(width, border, "Player names: ")
    print_framed_text(width, border, f"{names}", False, 8)
    print_framed_text(width, border)
    print_framed_text(width, border, "Guardians:")
    guardian_list = get_guardian_list(team)
    print_framed_text(width, border, f"{guardian_list}", False, 8)
    print_framed_text(width, border)
    print("-" * width)
    print("-" * width)
    input("Press ENTER to continue... ")
    cls()
    start_app()


def print_framed_text(width: int = 50, border: str = "", text: str = "",
                      centered: bool = False, indent: int = 4) -> None:
    """
    Function that accepts a width, a string to put on either side as the "frame"
    denoted as border,a boolean on whether the text should be centered, and an optional
    indention in spaces for the text
    Args:
        :param width: width of the frame including borders
        :param border: the border string that prints on either side
        :param text:  optional text to be displayed
        :param centered: bool representing if text should be centered
        :param indent: optional integer for number of spaces of indentation

    Returns:
        :return: None
    """
    padding: int = int(((width - 2 * len(border)) - len(text)) / 2)
    if text == "":
        print(f"{border}{((padding * 2) * ' ')}{border}")
    elif centered:
        print(f"{border}{padding * ' '}{text}{padding * ' '}{border}")
    else:
        right_padding: int = int(width - (indent + len(text) + len(border) * 2))
        print(f"{border}{indent * ' '}{text}{right_padding * ' '}{border}")


def get_main_option() -> str:
    """
    Function to get a choice from a user and return it
    from the main menu
    :return: str Returns the choice either 1 or 2
    """
    menu_choice: str = None
    while menu_choice != "1" and menu_choice != "2":
        try:
            menu_choice = input("Enter an option > ")
            if menu_choice != "1" and menu_choice != "2":
                raise ValueError
        except ValueError:
            print("Valid options are 1 and 2.", end=' ')
    cls()
    return menu_choice


def get_team_option() -> int:
    """
    Function to return the team number chosen by the user
    :return: int
    """
    while True:
        menu_choice: str = input("Enter an option > ")
        try:
            menu_choice: int = int(menu_choice)
            if menu_choice < 1 or menu_choice > len(constants.TEAMS):
                raise ValueError
        except ValueError:
            print(f"Valid options are 1 through {len(constants.TEAMS)}. ", end=' ')
        else:
            cls()
            return menu_choice


def get_guardian_list(team: Dict) -> str:
    """
    function to get the list of guardians as a string
    This is generated by joining a flattened list of lists
    :param team: Dict team
    :return: str comma separated flattened list of names
    """
    guardians_list: List[List] = [player["guardians"] for player in team["exp_players"]]
    guardians_list.extend([player["guardians"] for player in team["no_exp_players"]])
    guardian_names: str = ", ".join([guardian for guardians in guardians_list for guardian in guardians])
    return guardian_names


def get_average_height(team: Dict) -> float:
    """
    Function to return the average height of all players on a team
    :param team: Dict contains the team
    :return: float
    """
    total: int = 0
    for player in team["exp_players"]:
        total += player["height"]
    for player in team["no_exp_players"]:
        total += player["height"]
    return total / (len(team["exp_players"]) + len(team["no_exp_players"]))


def clean_data() -> List[Dict]:
    """
    Function to clean the data contained in the constants.py
    :return: Dict containing the cleaned dictionary
    """
    players = constants.PLAYERS
    cleaned_data = []
    for player in players:
        new_player = {}
        new_player["name"] = player["name"]
        new_player["experience"] = player["experience"] == "YES"
        new_player["guardians"] = player["guardians"].split(" and ")
        new_player["height"] = int(player["height"].replace("inches", ""))
        cleaned_data.append(new_player)
    return cleaned_data


def create_rosters() -> List[Dict]:
    """
    Function to create a List of dictionaries holding empty team rosters
    :return: List[Dict] a list containing a dictionary with an initial state
    """
    teams = constants.TEAMS
    return [{"name": team, "exp_players": [], "no_exp_players": []} for team in teams]


def sort_into_teams(exp: List[Dict], no_exp: List[Dict], rosters: List[Dict]) -> List[Dict]:
    """
    Function to sort the players into teams such that experienced and inexperienced
    players are evenly distributed among teams
    :param exp: List[Dict] a list containing experienced players
    :param no_exp: List[Dict] a list containing inexperienced players
    :param rosters: List[Dict] the list of teams in their initial state
    :return: List[Dict] the list of teams after assigned players
    """
    num_teams = len(rosters)

    i = 0
    while i < len(exp):
        rosters[i % num_teams]["exp_players"].append(exp[i])
        i += 1

    j = 0
    while j < len(no_exp):
        rosters[j % num_teams]["no_exp_players"].append(no_exp[j])
        j += 1

    return rosters


def start_app() -> None:
    """
    Function to start the application setting off a series of events
    :return: None
    """
    rosters = create_rosters()
    data = clean_data()
    experienced_players = [player for player in data if player["experience"]]
    rookie_players = [player for player in data if not player["experience"]]
    filled_rosters = sort_into_teams(experienced_players, rookie_players, rosters)
    print_main_menu()
    main_option: str = get_main_option()
    if main_option == "2":
        exit()
    else:
        print_stats_menu()
        team_option: int = int(get_team_option())
        print_team_stats(filled_rosters[team_option - 1])


if __name__ == "__main__":
    try:
        start_app()
    except KeyboardInterrupt:
        # This is here to exit gracefully in the event of a keyboard interrupt
        print("Thank you for using our basketball management system.")
        exit()
