#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1 = 0.021
#Enter the number of days: 12
#There will be 25017087 people after 12 days

question = "what is the current population?"
p = input(question)
p = float(p)
question = "what is the rate of growth (decimal)?"
r = input(question)
r = float(r)
question = "what is the number of days?"
d = input(question)
d = float(d)
d = round(d)

t = d/365

fp = p*(1+r)**t
fp = round(fp)

print(f"There will be {fp} people after {d} days.")