import sys


restart = input('\nYOU DIED \n\ntype r to restart or q to quit: ')

if restart == 'r':
    exec(open('main.py').read())
else:
    sys.exit()

