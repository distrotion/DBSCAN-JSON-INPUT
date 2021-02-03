from flask import Flask, request, jsonify
import json
import requests
import time


app = Flask(__name__)

@app.route('/test', methods=['POST'])
def my_json():
	for i in range(1000):
		res = requests.post('https://us-central1-nicetynine-mind-fit.cloudfunctions.net/setMindTestWeekyScore', json={})

		print("ROUND: {} -->".format(i),res.json())	

		res2 = requests.post('https://dbscan-deploy-u2heuu2mna-et.a.run.app/DBSCAN', json=res.json())	

		print("RESULT: {} <--".format(i),res2.json())			

		time.sleep(2)		
	return jsonify(res2.json())
	

if __name__ == '__main__':
   app.run(debug = True,port=6000)