import time
import sys
import main
import second_choice


def action():
    weapon_status = 0
    life = True
    choices_made = set()

    while True:
        script = "\nThere are 3 doors a red one, blue one and a green one \n\nwhich one do you choose: "
        decision = input(script).lower()

        choices = {
            'red': first_red,
            "blue": first_blue,
            "green": first_green}

        options = {
            "exit": sys.exit,
            "help": main.help_menu
        }
        if decision in options:
            options[decision]()
        elif decision in choices_made:
            if decision == "blue":
                print('\nalready got sword')
            elif decision == "red":
                print('\nscary monster over there cant go back')
            time.sleep(2)
        elif decision in choices:
            print(f'you picked {decision}')
            weapon_status, life = choices[decision](weapon_status, life=True)
            choices_made.add(decision)
        else:
            print('\nTry again')
            time.sleep(2)
        if not life:
            return


def first_blue(weapon, life=True):
    while True:
        script = '\nWOW YOU FOUND A CHEST\n\nwould you like to open it: '
        wants_weapon = input(script).lower()

        if wants_weapon == "exit":
            sys.exit()
        elif wants_weapon == 'yes':
            weapon = 1
            for i in range(3):
                print('.', end="")
                time.sleep(1)
            print('\nyou found a sword')
            time.sleep(2)
            return weapon, life
        else:
            print('\ndont be dumb')
            time.sleep(2)


def first_red(weapon, life=True):
    if weapon == 0:
        while True:
            script = "\nOhh no, it's a monster - you have no weapon.\n\nWould you like to fight with your fists?: "
            decision = input(script).lower()
            if decision == "exit":
                sys.exit()
            elif decision == 'yes':
                return 0, dead()
            elif decision == 'no':
                print('\nYou ran away')
                time.sleep(2)
                return weapon, True
            else:
                print('\nTry again')
                time.sleep(2)


def first_green(weapon, life=True):
    weapon, life = second_choice.action(weapon, life)
    if not life:
        return weapon, False


def dead():
    while True:
        restart = input('\nYOU DIED \n\ntype r to restart or q to quit: ').lower()

        if restart == 'r':
            return False
        elif restart == "q":
            sys.exit()
        else:
            print("Invalid input, try again")
