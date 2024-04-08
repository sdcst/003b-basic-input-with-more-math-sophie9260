#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  
Write a program that asks the user to enter in the prices of 5 items that they are buying.  
Find the total price, the amount of tax and the overall price.  
Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""
question = "What is the price of the first item you purchased?"
a = input(question)
a = float(a)

question = "What is the price of the second item you purchased?"
b = input(question)
b = float(b)

question = "What is the price of the third item you purchased?"
c = input(question)
c = float(c)

question = "What is the price of the fourth item you purchased?"
d = input(question)
d = float(d)

question = "What is the price of the fifth item you purchased?"
e = input(question)
e = float(e)

st = a+b+c+d+e
st = round(st,2)
print(f"The subtotal is ${st}.")
tx = st*0.12
tx = round(tx,2)
print(f"The taxes total is ${tx}.")
t = st+tx
t = round(t,2)
print(f"The total amount is ${t}")