import random
import numpy as np
import pandas as pd
import json

Choice = []
Choice1 = []
Result = []
Week=[]

for i in range(1000):
    if i%2 == 1:
        Result.append(random.uniform(13.00,14.00))
    elif i%2 == 0:
        Result.append(random.uniform(10.00,11.00))
    Week.append(random.randint(0,5))
    #print(i)
    for j in range(9):
        if i%2 == 1:
            Choice1.append(random.randint(2,5))
        elif i%2 == 0:
            Choice1.append(random.randint(0,3))
    Choice.append(Choice1)
    Choice1 = []

#print(Result)

data = []
dic={}
for i,x in enumerate(Choice):
    dic["Choice"] = Choice[i]
    dic["Result"] = Result[i]
    dic["Week"] = Week[i]
    data.append(dic)
    dic={}

#print(data)

########################################################################################################################################

def Average(lst): 
    return sum(lst) / len(lst) 

pre_data = []
for i,x in enumerate(data):
    #pre_data.append([Average(data[i]["Choice"]) , data[i]["Result"]] )
    pre_data.append([Average(data[i]["Choice"]) , data[i]["Result"] * (data[i]["Week"]+1)] )
    #pre_data.append([Average(data[i]["Choice"]) * (data[i]["Week"]+1) , data[i]["Result"]] )


#print(pre_data)

df = pd.DataFrame(pre_data)
df.to_csv (r'test_set_01.csv', index = False, header=True)

with open('pre_data.json', 'w') as json_file:
    json.dump(data, json_file)