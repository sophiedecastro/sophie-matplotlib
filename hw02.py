import matplotlib.pyplot as plt
import csv

x = [] # year
y = [] # population

# PLOT 1

open_population_file = open('population.csv')
open_population_reader = csv.reader(open_population_file)
open_population_data = list(open_population_reader)

for row in reversed(open_population_data[1:20]):
    a = row[5]
    b = a.strip('YEAR')
    x.append(b)
    y.append(row[9])

fig, ax = plt.subplots()
plt.bar(x,y)
ax.set(xlabel='Year 2000-2018')
ax.set(ylabel='Mid-Year Population Estimate in Thousands')
plt.show()

x = [] # year
y = [] # unemployment number in thousands

'''
# PLOT 2
open_unemployment_file = open('unemployment.csv')
open_unemployment_file = csv.reader(open_unemployment_file)
open_unemployment_data = list(open_unemployment_file)
# print(open_unemployment_data[1][9])

for row in reversed(open_unemployment_data[1:6]):
    a = row[5]
    b = a.strip('YEAR')
    x.append(b)
    y.append(row[9])
print('x=', x, 'y=', y)

fig, ax = plt.subplots()
plt.bar(x,y)
ax.set(xlabel='Year 2015-2019')
ax.set(ylabel='Unemployment number in thousands')
plt.show()

'''
#PLOT 3

x=[]
y=[]
z=[]

open_population_file = open('population.csv')
open_population_reader = csv.reader(open_population_file)
open_population_data = list(open_population_reader)

for row in reversed(open_population_data[1:5]):
    x.append(row[9])
print('x=', x)

open_unemployment_file = open('unemployment.csv')
open_unemployment_file = csv.reader(open_unemployment_file)
open_unemployment_data = list(open_unemployment_file)

for row in reversed(open_unemployment_data[2:6]):
    z.append(row[9])
    a = row[5]
    b = a.strip('YEAR')
    y.append(b)

fig, ax = plt.subplots()
plt.plot (y,z, label = 'Unemployment')
plt.plot (y,x, label = 'Population')
ax.set(xlabel='Year 2015-2018')
ax.set(ylabel='Number of people in Thousands')
plt.legend() 
plt.show()
