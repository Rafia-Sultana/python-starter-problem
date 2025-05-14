def guessing_game():
    input_number = int(input("Enter number: "))
    number = 6
    if number > input_number:
        print("your guess is almost there")
    elif number <  input_number:
        print("your guess is higher")
    else:
        print("Your Guess Is Correct!")
        
guessing_game()