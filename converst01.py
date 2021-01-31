import numpy as np
import pandas as pd
import json
import csv



#point = pd.read_csv('new_point.csv') 
#label = pd.read_csv('labels.csv') 

label = []
df=pd.read_csv('labels.csv')
for index, row in df.iterrows():
    d=row.to_dict()
    label.append(d)
    #print(d)

point = []
df=pd.read_csv('new_point.csv')
for index, row in df.iterrows():
    d=row.to_dict()
    point.append(d)
    #print(d)

output =[]
dic={}
for i,x in enumerate(point):
    dic['label'] = label[i]
    dic['point'] = point[i]
    output.append(dic)
    dic={}

print(output)
