"""
Name: Se Ho Lee
Username: slee626
Student Id: 890218467
Description: A Program that fulfills the functionalities of a mathematical quiz with five
basic arithmetic operation, i.e, addition, subtraction, multiplication, integer division and
modulo operation.
"""
import random
import math

def display_intro():
    title = " A Simple Math Quiz "
    extra = 2
    title_length = len(title)
    border_line = title_length + extra * 2

    print("*" * border_line)
    print("*" * extra + title + extra * "*")
    print("*" * border_line)

def display_menu():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Integer Division")
    print("5. Modulo Operation")
    print("6. Exit")

def display_separator():
    print("-" * 24)

def get_user_input():
    prompt = "Enter your choice: "
    prompt_2 = "Please try again: "
    index = int(input(prompt))

    while index <= 0 or index >= 7:
        print("Invalid menu option.")
        index = int(input(prompt_2))
    return index

def get_user_solution(problem):
    print("Enter your answer")
    outcome = int(input(problem))
    return outcome

def check_solution(user_solution, solution, count):
    true = "Correct."
    false = "Incorrect."
    if user_solution == solution:
        print(true)
        count += 1
    else:
        print(false)
    return count

def menu_option(index, count):
    variable_1 = random.randrange(1,31)
    variable_2 = random.randrange(1,31)
    if index == 1:
        problem = (str(variable_1) + " + " + str(variable_2) + " = ")
        solution = variable_1 + variable_2
    elif index == 2:
        problem = (str(variable_1) + " - " + str(variable_2) + " = ")
        solution = variable_1 - variable_2
    elif index == 3:
        problem = (str(variable_1) + " * " + str(variable_2) + " = ")
        solution = variable_1 * variable_2
    elif index == 4:
        problem = (str(variable_1) + " // " + str(variable_2) + " = ")
        solution = variable_1 // variable_2
    elif index == 5:
        problem = (str(variable_1) + " % " + str(variable_2) + " = ")
        solution = variable_1 % variable_2
    user_solution = get_user_solution(problem)
    count = check_solution(user_solution, solution, count)
    return count

def display_result(total, correct):
    print("You answered " + str(total) + " questions with " + str(correct) + " correct.")
    if total == 0:
        record = 0
    else:
        record = round(correct / total * 100, 2)
    print("Your score is " + str(record) + "%. Thank you.")
        
def main():
    display_intro()
    display_menu()
    display_separator()

    option = get_user_input()
    total = 0
    correct = 0
    while option != 6:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()

    print("Exit the quiz.")
    display_separator()
    display_result(total, correct)

main()
