names_string = input("Give me everybody's names, separated by a comma.\n" )
names = names_string.split(", " )
import random

number_of_people = len(names)
random_number = random.randint(0, number_of_people -1)
person_to_pay = names[random_number]

print(f"{person_to_pay} is going to buy the meal today!")