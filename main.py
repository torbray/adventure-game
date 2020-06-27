import sys
import time

wepon_status = 0 # 0 = no wepon
user_gender = int(input('\nEnter your Gender 0 for male 1 for female: '))

if user_gender == 1:
    exec(open('dead.py').read())

elif user_gender == 0:
    print('\nWelcome to -tbd-')
else:
    print('\nTry again')
    time.sleep(2)
    exec(open('main.py').read())


exec(open('first_choice.py').read())