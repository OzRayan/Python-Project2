import constants
import os


NUM_TEAMS = len(constants.TEAMS)


def cls():
    # short cls snippet from https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    os.system('cls' if os.name == 'nt' else 'clear')


def print_main_menu() -> None:
    """
    Function takes no arguments
    Responsible only for printing the menu for the user
    :return: None
    """
    width = 44
    menu = "-- MENU --"
    line_one = "  Enter an option:"
    option_one = "  1) Display Team stats"
    option_two = "  2) Quit"
    border = "||"
    empty_space = width - 2 * len(border)
    print()
    print("=" * width)
    print(border + empty_space * " " + border)
    padding = int((empty_space - len(menu)) / 2)
    print(border + padding * " " + menu + padding * " " + border)
    print(border + empty_space * " " + border)
    print(border + line_one + (empty_space - len(line_one)) * " " + border)
    print(border + option_one + (empty_space - len(option_one)) * " " + border)
    print(border + option_two + (empty_space - len(option_two)) * " " + border)
    print(border + empty_space * " " + border)
    print("=" * width)


def get_main_option() -> str:
    menu_choice = None
    while menu_choice != "1" and menu_choice != "2":
        try:
            menu_choice = input("Enter an option > ")
            if menu_choice != "1" and menu_choice != "2":
                raise ValueError
        except ValueError:
            print("Valid options are 1 and 2.", end=' ')
    return menu_choice


def start_app() -> None:
    print_main_menu()
    main_option = get_main_option()
    if main_option == "2":
        exit()


if __name__ == "__main__":
    try:
        start_app()
    except KeyboardInterrupt:
        print("Thank you for using our basketball management system.")
        exit()


