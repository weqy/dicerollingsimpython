import random # randomizer that we're using
min_val = 1 # minimum number possible
max_val = 6 # maximum number possible

roll_again = "yes" # to loop the rolling through user input

while roll_again == "yes" or roll_again == "y": # if user agrees to roll the dice again
    print("Rolling The Dice...") # cosmetic
    print("The Value is :") # tells user what the number is

    print(random.randint(min_val, max_val)) # generating and printing random number from 1 to 6

    roll_again = input("Roll the Dices Again? (y for yes): ") # asks user to roll the dice again. any input other than y will terminate the loop
