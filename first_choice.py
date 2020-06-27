import time

first_action = input("\nThere are 3 doors a red one, blue one and a green one \n\nwhich one do you choose: ")

if first_action == 'red':
    print('you picked red')
    exec(open('first_room/first_red_door.py').read())

elif first_action == 'blue':
     print('you picked blue')
     exec(open('first_room/first_blue_door.py').read())

elif first_action == 'green':
     print('you picked green')  
     exec(open('first_room/first_green_door.py').read())

else:
    print('\nTry again')
    time.sleep(2)
    exec(open('first_choice.py').read())

