import random

highest_num= input("Type a number,this will be the highest number in the range!! ")

if highest_num.isdigit():
    highest_num= int(highest_num)

    if highest_num<= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, highest_num)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess between the range 0 and the number you entered before: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")