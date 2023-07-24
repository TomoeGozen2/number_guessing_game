import random


#user guesses number. Computer gives hints if it is too high or low
computer_number = random.randint(0,100)
while True:
    try:
        user_guess = int(input('Enter a number: '))
        if user_guess > computer_number:
            print('To high')
           
        elif user_guess < computer_number:
            print('Too low')
            
        if user_guess == computer_number:
            print('You win')
            break
    except:
        print('Enter a number')


