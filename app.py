import constants

NUM_TEAMS = len(constants.TEAMS)


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


def start_app() -> None:
    print_main_menu()


if __name__ == "__main__":
    try:
        start_app()
    except KeyboardInterrupt:
        print("Thank you for using our basketball management system.")
        exit()


