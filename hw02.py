import json
import matplotlib.pyplot as plt
# import os
import csv



'''
# USE BRITISH SPELLING FOR NEIGHBOURHOODS TO MATCH JSON FILE !!!
# filenames = [   
#     'dates.json',
#     'forces.json',
#     'neighbourhoods.json',  
# ]

with open('precip.json', 'r') as f:
    file_counts = json.loads(f.read())
    # print('len(file_counts)=',len(file_counts))

for x in file_counts:
    # print(file_counts['description']['title']['value'])
    print(file_counts['data'])
# for filename in filenames:
#     place_x = filename[]
# print(file_counts)

# for y in file_counts['data']:
#     print

# for obj in file_counts['data']:
#     print(var)

'''
'''
with open('neighbourhoods.json', 'r') as f:
    file_neighbourhoods = json.loads(f.read())
    print('len(file_neighbourhoods)=',len(file_dates))

with open('forces.json', 'r') as f:
    file_forces = json.loads(f.read())
    print('len(file_forces)=',len(file_forces))
'''

# dates = []
# for filename in filenames:
#     with open(filename, 'r') as f:
#         file_dates = json.loads(f.read())
#         dates += file_dates
# print('len(dates)=',len(dates))

'''
# practice data below

# plot 1
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y,label = 'Python')

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x, js_dev_y,label = 'JavaScript')

plt.plot(ages_x, dev_y, color='#444444', linestyle='--', marker='.', label = 'All Devs')

plt.xlabel('x label 1')
plt.ylabel('y label 1')
plt.title('this will be title 1')
# plt.legend(['All Devs', 'Python']) #adding legends requires you to know the order in which things were added in your code
plt.legend() # can run empty if you have labels above
plt.show()

# plot 2
plt.bar(ages_x, js_dev_y)
plt.show()
# plt.legend() #tbd

#print(plt.style.available) # to see available styles
# plt.style.use('seaborn-pastel')

#plt.grid(True) idk
# plt.tight_layout() idk

# plt.savefig('plot.png') -- save plot to computer/download

'''