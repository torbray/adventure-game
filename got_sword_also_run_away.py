import time

first_action = input("\nThere are 3 doors a red one, blue one and a green one \n\nwhich one do you choose: ")

if first_action == 'red':
    print('\nscary monster over there cant go over there')
    time.sleep(2)
    exec(open('got_sword_also_run_away.py').read())

elif first_action == 'blue':
     print('\nalready got sword')
     time.sleep(2)
     exec(open('got_sword_also_run_away.py').read())

elif first_action == 'green':
     print('you picked green')  
     exec(open('first_room/first_green_door.py').read())

else:
    print('\nTry again')
    time.sleep(2)
    exec(open('first_choice.py').read())

import time

