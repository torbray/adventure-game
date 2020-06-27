import time

first_action = input("\nThere are 3 doors a red one, blue one and a green one \n\nwhich one do you choose: ")

if first_action == 'red':
    print('\nscary monster over there cant go back')
    time.sleep(2)
    exec(open('ran_away_first_red.py').read())

elif first_action == 'blue':
     print('you picked blue')
     exec(open('first_room/first_blue_door_ran.py').read())

elif first_action == 'green':
     print('you picked green')  
     exec(open('first_room/first_green_door.py').read())

else:
    print('\nTry again')
    time.sleep(2)
    exec(open('first_choice.py').read())

