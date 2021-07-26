import os
cmd = "curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt"
os.system(cmd)


elements1_20 = open('elements1_20.txt', 'r')
elem_list = elements1_20.readlines()
elements1_20.seek(0)

elem_str = []

first_counter = 0
while first_counter < 20:
    elem_str += elements1_20.readline().lower().strip().split(',')
    first_counter += 1
    if first_counter >= 20:
        break

print("List any 5 of the first 20 elements in the Periodic Table\n")
element_guess = []


def get_names():
    counter = 0
    while counter < 5:
        guess = input("Type in the name of any element!!!: ")
        if guess in element_guess:
            print(guess, "was already entered\t <--no duplicated allowed")
            pass
        elif guess == "":
            print("You didn't type in anything!")
            pass
        else:
            element_guess.append(guess)
            counter += 1
    return element_guess
           
get_names()

correct_guess = []
incorrect_guess = []
correct = 0
incorrect = 0
guess_counter = 0

while guess_counter < 5:
    for guess in element_guess:
        range(len(elem_list))    
        if guess in elem_str:
            correct_guess.append(guess)
            guess_counter += 1
            correct += 1
        else:
            incorrect_guess.append(guess)
            guess_counter += 1
            incorrect += 1

pct_correct = correct * 20

# print output
print(pct_correct, "% correct!")
print("Found: ", correct_guess)
print("Not Found: ", incorrect_guess)