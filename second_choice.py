import time

second_action = input("\nThere are 2 doors a pink one and a white one \n\nwhich one do you choose: ")

if second_action == 'pink':
    print('you picked pink')
    exec(open('second_room/second_pink_door.py').read())

elif second_action == 'white':
     print('you picked white')  
     exec(open('second_room/second_white_door.py').read())

else:
    print('\nTry again')
    time.sleep(2)
    exec(open('main.py').read())