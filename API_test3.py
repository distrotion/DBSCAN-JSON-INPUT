from flask import Flask, request, jsonify
import json


app = Flask(__name__)

@app.route('/test', methods=['POST'])
def my_json():
	
	input_j = request.json
	input_key_list = [*input_j]

	data_list = []
	for i in range(len(input_key_list)):
		data_list.append(input_j["{}".format(input_key_list[i])])

	print(len(input_key_list))							
	return jsonify(data_list)
	

if __name__ == '__main__':
   app.run(debug = True,port=6000)