import numpy as np
import pandas as pd
import json
import os
from flask import Flask, request, jsonify
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler


import firebase_admin
from firebase_admin import db

app = Flask(__name__)

firebase_admin.initialize_app(options={
    'databaseURL': 'https://first-test-api-01-default-rtdb.firebaseio.com',
})
SUPERHEROES = db.reference('superheroes')

 
def Average(lst): 
    return sum(lst) / len(lst)   

@app.route('/create_hero', methods=['POST'])
def create_hero():  

    req = request.json
    hero = SUPERHEROES.push(req)

    return flask.jsonify({'id': hero.key})

@app.route('/setup', methods=['POST'])
def setup():  
    data_setup = request.json

    with open('setup.json', 'w') as outfile:
        json.dump(data_setup, outfile)    
    
    return jsonify({"Status":"OK"})

@app.route('/DBSCAN', methods=['POST'])
def INPUTDATA():
    data = request.json 

    pre_data = []
    for i,x in enumerate(data):
        #pre_data.append([Average(data[i]["Choice"]) , data[i]["Result"]] )
        pre_data.append([Average(data[i]["Choice"]) , data[i]["Result"] * (data[i]["Week"]+1)] )
        #pre_data.append([Average(data[i]["Choice"]) * (data[i]["Week"]+1) , data[i]["Result"]] )


    #print(pre_data)

    df = pd.DataFrame(pre_data)
    df.to_csv (r'data_set_01.csv', index = False, header=True)


    with open('setup.json', 'r') as myfile:
        setup_data=myfile.read()
    # parse file
    obj_setup = json.loads(setup_data)
    print(obj_setup)
    print(obj_setup['esp'])
    print(obj_setup['min_samples'])
#-------------------------------------------------------------------------------------------------------------------------------------------------------
    # #############################################################################
    # Generate sample data
    #centers = [[1, 1], [-1, -1], [1, -1] , [-1, 1]]
    #X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
    #                            random_state=0)

    X = pd.read_csv('data_set_01.csv') 


    X = StandardScaler().fit_transform(X)

    # #############################################################################
    # Compute DBSCAN
    db = DBSCAN(eps=obj_setup['esp'], min_samples=obj_setup['min_samples']).fit(X)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    
    df = pd.DataFrame(labels)
    file = 'labels_p.csv'
    pd.DataFrame(columns=['labels']).to_csv(file, index=False)
    df.to_csv(file, header=None, index=False, mode='a')


    df = pd.DataFrame(X)
    file = 'new_point_p.csv'
    pd.DataFrame(columns=['X','Y']).to_csv(file, index=False)
    df.to_csv(file, header=None, index=False, mode='a')
    
    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)




    print('Estimated number of clusters: %d' % n_clusters_)
    print('Estimated number of noise points: %d' % n_noise_)
    #print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
    #print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
    #print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
    #print("Adjusted Rand Index: %0.3f"
    #      % metrics.adjusted_rand_score(labels_true, labels))
    #print("Adjusted Mutual Information: %0.3f"
    #      % metrics.adjusted_mutual_info_score(labels_true, labels))


    #print("Silhouette Coefficient: %0.3f"
    #      % metrics.silhouette_score(X, labels))

    # #############################################################################
    # Plot result
#-------------------------------------------------------------------------------------------------------------------------------------------------------
    label_p = []
    df=pd.read_csv('labels_p.csv')
    for index, row in df.iterrows():
        d=row.to_dict()
        label_p.append(d)
        #print(d)

    point_p = []
    df=pd.read_csv('new_point_p.csv')
    for index, row in df.iterrows():
        d=row.to_dict()
        point_p.append(d)
        #print(d)

    output =[]
    dic={}
    for i,x in enumerate(point_p):
        dic['label'] = label_p[i]
        dic['point'] = point_p[i]
        dic['UID'] = data[i]['UID']
        output.append(dic)
        dic={}    

    return jsonify(output)


if __name__ == '__main__':
   app.run(debug = True,port=int(os.environ.get('PORT',6001)))

