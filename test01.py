import numpy as np
import pandas as pd
import uuid 

##
thisdict = [
{
    "Uid" : "tudidjddjdhwu2uusf",
    "Choice" : [1, 2, 3, 4, 5, 5, 2, 3, 3],
    "Result" : 13.158,
    "Week" : 1,
    "Skip" : 0
},
{
    "Uid" : "qwertyuiopyrt",
    "Choice" : [ 1, 2, 3, 4, 5, 5, 2, 3, 3],
    "Result" : 12.158,
    "Week" : 1,
    "Skip" : 0
}
]



id = uuid.uuid1() 
print (id.hex) 

def Average(lst): 
    return sum(lst) / len(lst) 

output = []
for i,x in enumerate(thisdict):
    output.append([Average(thisdict[i]["Choice"]) , thisdict[i]["Result"]])


#print(output)

#df = pd.DataFrame(output)
#df.to_csv (r'test5_XY.csv', index = False, header=True)

#with open('output.json', 'r') as myfile:
#    data=myfile.read()
# parse file
#obj = json.loads(data)
#print(obj) 