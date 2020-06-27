import time

wants_wepon = input('\nWOW YOU FOUND A CHEST\n\nwould you like to open it: ')

if wants_wepon == 'yes':
    wepon_status = 1
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('you found a sword')
    time.sleep(2)
    exec(open('got_sword_first_choice.py').read())

else:
    print('\ndont be dumb')
    time.sleep(2)
    exec(open('first_blue_door.py').read())
    