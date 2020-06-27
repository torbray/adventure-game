import first_choice


def start_menu():
    while True:
        print("Type 'help' for help or 'exit' for exit.")
        print('\nWelcome to the adventure!')
        # decision = input('\nEnter your Gender - 0 for male, 1 for female: ').lower()
        #
        # options = {
        #     "exit": sys.exit,
        #     "help": help_menu
        # }
        # if decision in options:
        #     options[decision]()
        # else:
        #     print('\nWelcome to the adventure!')
        # elif user_gender in {"0", "1"}:
        #     print('\nWelcome to the adventure!')
        # else:
        #     print('\nTry again')
        #     time.sleep(2)
        #     continue

        first_choice.action()


def help_menu():
    print("Help Menu:\n"
          "exit\t\tExit the Game\n"
          "help\t\tBrings up the Help Menu")


if __name__ == "__main__":
    start_menu()
