# Python’s random module
import random

# initially the score is 0
score = 0

for i in range (5):
    # generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # ask the question
    print(f"What is {num1} × {num2}?")

    # get user input
    user_input = int(input("Your answer: "))

    # increase the score
    if (user_input == num1 * num2):
        score+=1

 # display final score
print(f"You scored: {score}")
