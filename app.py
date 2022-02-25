from flask import Flask, jsonify
import json
app = Flask('app')
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello_world2():
  return "ok"

@app.route('/start')
def hello_world():
  with open('startword.json', "r") as json_file:
    json_data = json.load(json_file)
  return jsonify(json_data)

@app.route('/end')
def hello_world1():
  with open('endword.json', "r") as json_file:
    json_data = json.load(json_file)
  return jsonify(json_data)

@app.route('/end1')
def hello_world11():
  with open('endword.json', "r") as json_file:
    json_data = json.load(json_file)
  return jsonify({'테스트':'테스트','테스트':'테스트','테스트':'테스트','테스트':'테스트'})

app.run(host='0.0.0.0', port=8080)