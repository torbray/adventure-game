import time
import sys
import main
import first_choice


def action(weapon, life=True):
    while True:
        script = "\nThere are 2 doors a pink one and a white one \n\nwhich one do you choose: "
        decision = input(script).lower()

        choices = {
            'pink': second_pink,
            "white": second_white}

        options = {
            "exit": sys.exit,
            "help": main.help_menu
        }
        if decision in options:
            options[decision]()
        elif decision in choices:
            print(f'you picked {decision}')
            weapon_status, life = choices[decision](weapon, life=True)
        else:
            print('\nTry again')
            time.sleep(2)
        if not life:
            return 0, False


def second_pink(weapon=0, life=True):
    print('\nOhh no its a trap')
    for i in range(3):
        print('.', end="")
        time.sleep(1)
    return 0, first_choice.dead()


def second_white(weapon, life=True):
    print("white")
    return weapon, life
