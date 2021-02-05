from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/test', methods=['GET', 'POST'])
def my_json():
	if request.method == 'POST':
		print(request.json)							
		return jsonify(request.json)
	return '200'

if __name__ == '__main__':
   app.run(debug = True,port=int(os.environ.get('PORT',6001)))