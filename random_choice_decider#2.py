import random
num_of_guesses = ""

while type(num_of_guesses) != int:
    try:
        num_of_guesses = int(input("Enter in the amount of choices you have: "))
    except ValueError:
        print("You have not put in an integer. Please try again.")

choices_put_by_user = 1

all_choices = []
while choices_put_by_user <= num_of_guesses:
    a_choice = input("Enter in a choice: ")
    all_choices.append(a_choice)
    choices_put_by_user += 1

print(random.choice(all_choices))
