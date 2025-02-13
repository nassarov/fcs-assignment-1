#  1) Exercise 1: Movie Ticket Price Calculator Write a Python program that asks the user for their age and determines the price of a movie ticket based on the following rules:
# - If the user is , the ticket is
# - If the user is , the ticket costs .
# - If the user is , the ticket costs .
# - If the user is , the ticket costs .
# Example:
# Enter your age: 8
# The ticket price is $5.

age = int(input("Enter your age: "))

if age >= 25:
    print("The ticket price is $25")
elif age >= 18:
    print("The ticket price is $15")
elif age >= 8:
    print("The ticket price is $7")
else :
    print("Free ticket for kids under 8")

