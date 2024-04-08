#!python3
 
"""
##### Task 1
The bank calculates the amount of interest you earn using the simple interest formula:
interest = principal * rate * #days in the month / 365

Ask the user to enter the amount of their principal, the number of days in the month the rate of interest expressed as a percentage.  Calculate the amount of interest they would be paid.

example:
Enter your amount: 100
Enter the rate: 2.5 = 0.025
Enter the # of days in the month: 30
You earned $0.2 interest. 
(2 points) 
"""
question = "what is the amount of your principal?"
p = input(question)
p = float(p)

question = "what is the number of days?"
d = input(question)
d = float(d)

question = "what is the rate of the interest(pecentage)?"
r = input(question)
r = float(r)


interest = p*r*(d/365)
print(f"The amount of interest earned is {interest}.")