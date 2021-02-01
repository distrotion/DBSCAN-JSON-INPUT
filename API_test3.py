from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def my_json():
	
	input_j = request.json


	print(request.json)							
	return jsonify(input_j['-MSUwvmr68HPMSjYSqUL'])
	

if __name__ == '__main__':
   app.run(debug = True,port=6000)