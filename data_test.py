import random
import numpy as np
import pandas as pd

Choice = []
Choice1 = []
Result = []
Week=[]
Skip=[]

for i in range(800):
    Result.append(random.uniform(13.00,14.00))
    Week.append(random.randint(0,2))
    Skip.append(random.randint(0,2)
    for j in range(9):
        Choice1.append(random.randint(0,9))
    Choice.append(Choice1)
    Choice1 = []

#print(Result)

data = []
dic={}
for i,x in enumerate(Choice):
    dic["Choice"] = Choice[i]
    dic["Result"] = Result[i]
    dic["Skip"] = Skip[i]
    dic["Week"] = Week[i]
    data.append(dic)
    dic={}

print(data)

########################################################################################################################################

def Average(lst): 
    return sum(lst) / len(lst) 

output = []
for i,x in enumerate(data):
    #output.append([Average(data[i]["Choice"]) , data[i]["Result"]] )
    output.append([Average(data[i]["Choice"]) , data[i]["Result"] * (data[i]["Week"]+1)] )
    #output.append([Average(data[i]["Choice"]) * (data[i]["Week"]+1) , data[i]["Result"]] )


#print(output)

df = pd.DataFrame(output)
df.to_csv (r'test_set_01.csv', index = False, header=True)
