# write your code here
import random
score = 0
result = 0


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def easy_task():
    global result
    first_num = random.randint(2, 9)
    second_num = random.randint(2, 9)
    operand = random.choice(["+", "-", "*"])
    print(first_num, operand, second_num)
    if operand == "+":
        result = add(first_num, second_num)
    elif operand == "-":
        result = subtract(first_num, second_num)
    elif operand == "*":
        result = multiply(first_num, second_num)


def difficult_task():
    global result
    number = random.randint(11, 29)
    print(number)
    result = number ** 2


level_description = {
    "1": "simple operations with numbers 2-9",
    "2": "integral squares of 11-29",
}

i = 0
positive_answer = ("Yes", 'yes', "Y", "y", "YES")
while True:
    level = input(f"""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29\n""")
    if level not in level_description.keys():
        print("Incorrect format")
    else:
        break

while i < 5:
    if level == "1":
        easy_task()
    elif level == "2":
        difficult_task()
    while True:
        user_input = input()
        if not user_input.strip("-").isnumeric():
            print("Incorrect format")
        else:
            break
    if int(user_input) == result:
        print("Right!")
        score += 1
    else:
        print("Wrong!")

    i += 1

save = input(f"Your mark is {score}/5. Would you like to save your result to the file? Enter yes or no.")
if save in positive_answer:
    name = input("What is your name? ")
    f = open("results.txt", "a")
    f.write(f"{name}: {score}/5 in level {level} ({level_description[level]})")
    f.close()
    print("The results are saved in 'results.txt'")
