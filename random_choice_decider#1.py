import random

all_choices = []

an_option = input("If you want to finalize all your choices, type the word 'end' on your keyboard. If not, enter in a choice: ")

while an_option != "end":
    all_choices.append(an_option)
    an_option = input("If you want to finalize all your choices, type the word 'end' on your keyboard. If not, enter in a choice: ")

selected_answer = random.choice(all_choices)

print(selected_answer)
