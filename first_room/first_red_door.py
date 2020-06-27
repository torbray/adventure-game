import time


if wepon_status == 0:
    red_first_desision = input('\nOhh no its a monstor you have no wepon\n\nwould you like to fight with your fists: ')

    if red_first_desision == 'yes':
        exec(open('dead.py').read())

    elif red_first_desision == 'no':
        print('\nyou ran away')
        time.sleep(2)
        exec(open('ran_away_first_red.py').read())
    
    else:
        print('\nTry again')
    time.sleep(2)
    exec(open('first_room/first_red_door.py').read())


