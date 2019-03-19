# ASCII frames are heavily inspired by https://www.asciiart.eu/art-and-design/borders
import constants
import os
from typing import List, Dict


def cls():
    # short cls snippet from https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    os.system('cls' if os.name == 'nt' else 'clear')


def print_main_menu() -> None:
    """
    Function takes no arguments
    Responsible only for printing the menu for the user
    Use an even number for the width!
    :return: None
    """
    width: int = 38
    border: str = "||"
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
    width: int = 38
    border = "||"
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


def print_team_stats(team):
    average_height: float = get_average_height(team)
    average_height = str(round(average_height, 2))
    if not len(average_height) % 2:
        average_height += "0"
    width: int = 120
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
                      f" Average height: {average_height}", True, 25)
    print_framed_text(width, border, f"Experienced players: {len(team['exp_players'])}", True)
    print_framed_text(width, border, f"Inexperienced players: {len(team['no_exp_players'])}", True)

    player_names: List = [player["name"] for player in team["exp_players"]]
    player_names.extend([player["name"] for player in team["no_exp_players"]])
    names = ", ".join(player_names)
    print_framed_text(width, border)
    print_framed_text(width, border, "Player names: ")
    print_framed_text(width, border, f"{names}", False, 8)


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


def get_team_option() -> str:
    menu_choice: str = input("Enter an option > ")
    try:
        menu_choice = int(menu_choice)
        if menu_choice < 1 or menu_choice > len(constants.TEAMS):
            raise ValueError
    except ValueError:
        print(f"Valid options are 1 through {len(constants.TEAMS)}", end=' ')
    cls()
    return menu_choice


def get_average_height(team):
    total: int = 0
    for player in team["exp_players"]:
        total += player["height"]
    for player in team["no_exp_players"]:
        total += player["height"]
    return total / (len(team["exp_players"]) + len(team["no_exp_players"]))


def clean_data() -> List[Dict]:
    players = constants.PLAYERS;
    cleaned_data = []
    for player in players:
        player["experience"] = player["experience"] == "YES"
        player["guardians"] = player["guardians"].split(" and ")
        player["height"] = int(player["height"].replace("inches", ""))
        cleaned_data.append(player)
    return cleaned_data


def create_rosters() -> List[Dict]:
    teams = constants.TEAMS
    return [{"name": team, "exp_players": [], "no_exp_players": []} for team in teams]


def sort_into_teams(exp: List, no_exp: List, rosters: List[Dict]) -> List[Dict]:
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
        team_option: str = int(get_team_option())
        print_team_stats(filled_rosters[team_option - 1])


if __name__ == "__main__":
    try:
        start_app()
    except KeyboardInterrupt:
        print("Thank you for using our basketball management system.")
        exit()
