# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:56:12 2023

@author: 19108
"""

import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        # Make sure the division is valid
        while num2 == 0:
            num2 = random.randint(1, 10)
        answer = num1 / num2

    return f"What is {num1} {operator} {num2}?", answer

def main():
    correct_answers = 0
    total_questions = 5

    print("Welcome to the Math Quiz!")

    for _ in range(total_questions):
        question, answer = generate_question()
        print(question)

        user_answer = input("Your answer: ")

        try:
            user_answer = float(user_answer)
            if user_answer == answer:
                print("Correct!\n")
                correct_answers += 1
            else:
                print(f"Sorry, the correct answer is {answer}\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    print(f"You answered {correct_answers} out of {total_questions} questions correctly.")

if __name__ == "__main__":
    main()
