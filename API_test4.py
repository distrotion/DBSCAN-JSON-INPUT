from flask import Flask, request, jsonify
import json
import requests


app = Flask(__name__)

@app.route('/test', methods=['POST'])
def my_json():
	
	res = requests.post('https://us-central1-nicetynine-mind-fit.cloudfunctions.net/setMindTestWeekyScore', json={})

	print(res.json())	

	res2 = requests.post('https://dbscan-deploy-nmdlf3uxjq-as.a.run.app/DBSCAN', json=res.json())	

	print(res2.json())					
	return jsonify(res2.json())
	

if __name__ == '__main__':
   app.run(debug = True,port=6000)