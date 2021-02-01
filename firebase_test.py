from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import db

app = Flask(__name__)

firebase_admin.initialize_app(options={
    'databaseURL': 'https://first-test-api-01-default-rtdb.firebaseio.com',
})
SUPERHEROES = db.reference('superheroes')


@app.route('/create_hero', methods=['POST'])
def create_hero():
	
    req = request.json
    hero = SUPERHEROES.push(req)
    return flask.jsonify({'id': hero.key})
	


if __name__ == '__main__':
   app.run(debug = True,port=6000)