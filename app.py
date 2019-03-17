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


def print_framed_text(width: int = 50, border: str = "", text: str = "",
                      centered: bool = False, indent: int = 4) -> None:
    """
    Function that accepts a width, a string to put on either side as the "frame" denoted as border,
    a boolean on whether the text should be centered, and an optional indention in spaces for the text
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
        print(f"{border}{((padding * 2) *  ' ')}{border}")
    elif centered:
        print(f"{border}{padding * ' '}{text}{padding  * ' '}{border}")
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


def start_app() -> None:
    print_main_menu()
    main_option: str = get_main_option()
    if main_option == "2":
        exit()


if __name__ == "__main__":
    try:
        start_app()
    except KeyboardInterrupt:
        print("Thank you for using our basketball management system.")
        exit()


