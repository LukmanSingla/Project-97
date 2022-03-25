num = 24
guess = 5
while(guess > 0):
    guess = guess-1
    num2 = int(input('Enter the number: '))
    if(num == num2):
        print('You Won')
        print('You took', 5-guess, 'to finish the game')
        break
    else:
        if(guess == 0):
            print('You Lost!')
        else:
            if(num2 < num):
                print("It's greater")
            else:
                print("It's smaller")
            print("Number of guesses left are", guess)
        continue
