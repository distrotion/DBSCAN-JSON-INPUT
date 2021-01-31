import random
import numpy as np
import pandas as pd
import json
from flask import Flask, request, jsonify
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def INPUTDATA():
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

    return jsonify(data)


if __name__ == '__main__':
   app.run(debug = True,port=6005)