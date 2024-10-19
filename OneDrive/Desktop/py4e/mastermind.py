import random as rn

gen_no = rn.randrange(1000,10000)

print('Are you the MASTERMIND??')
print('Rule: '
      'You have to guess the 4 digit number'
      )
guess_no = input('Guess the number: ')
while True:
    # Check if the input is a 4-digit number
    if len(guess_no) == 4 and guess_no.isdigit():
        break  
    else:
        print("Invalid input. Please enter exactly 4 digits.")
        break
if guess_no == str(gen_no):
    print('WOAH! You guessed in the first attempt. You are the MASTERMIND')
else:
    tries = 0
    while guess_no != str(gen_no):
        tries += 1
        ryt = 0
        n = str(gen_no)
        nu = str(guess_no)

        correct = ['X']*4
        for i in range(0,4):
            if nu[i] == n[i]:
                correct[i] = nu[i]
                ryt += 1
            else:
                continue
        correct = ''.join(correct)
        print(correct)
        if ryt == 0:
            print('\nNo correct guesses. Try again')
        else:
            print('\nNot the right guess but you guessed', ryt, 'digits right. Keep trying')
        guess_no = input('Enter your guess again: ')

        five_table = [5,10,15,20,25,30]
        for j in five_table:
            if tries == j:
                print('Do you wanna quit?')
                print('\nYes or No')
                print('\n')
                ask = input().strip().lower() 
                if ask == 'no':
                    continue
                else:
                    print('You quit. Hahaha LOSER!!')
                    print('\nThe number was: ', gen_no)
                    break
            break
        if guess_no == str(gen_no):    
            print('You guessed the number in ', tries, 'tries')
            break