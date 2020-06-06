import http.server
import socketserver
import json
import mongoengine
from flask import Flask, request, jsonify
from bson.json_util import dumps
from utils.mongo import MongoJSONEncoder, ObjectIdConverter
from models import Greenhouse, Device, Account

app = Flask(__name__)

db = mongoengine
db.connect('app')

app.json_encoder = MongoJSONEncoder
app.url_map.converters['objectid'] = ObjectIdConverter

@app.route("/accounts", methods = ['GET'])
def get_accounts():
  try:
    results = []

    for account in Account.objects().select_related(max_depth=5):
      results.append(account)

    return jsonify(results)
  except Exception as e:
    return dumps(e)

@app.route("/accounts/<id>", methods = ['GET'])
def get_one_account(id):
  try:
    account = Account.objects(id=id).first()

    return jsonify(account)
  except Exception as e:
    return dumps(e)

@app.route("/accounts", methods = ['Post'])
def post_account():
  try:
    body = request.get_json()

    greenhouse = Greenhouse(name="My Greenhouse").save()

    body['greenhouses'] = []

    body['greenhouses'].append(greenhouse)

    account = Account(**body).save()

    return jsonify(account)
  except Exception as e:
    return dumps(e)

@app.route("/greenhouses", methods = ['GET'])
def get_greenhouses():
  try:
    results = []

    for greenhouse in Greenhouse.objects():
      results.append(greenhouse)

    return jsonify(results)
  except Exception as e:
    return dumps(e)

@app.route("/greenhouses/<id>", methods = ['GET'])
def get_one_greenhouse(id):
  try:
    greenhouse = Greenhouse.objects(id=id).first()

    return jsonify(greenhouse)
  except Exception as e:
    return dumps(e)

@app.route("/greenhouses", methods = ['Post'])
def post_greenhouse():
  try:
    body = request.get_json()
    greenhouse = Greenhouse(**body).save()

    return jsonify(greenhouse)
  except Exception as e:
    return dumps(e)

if __name__ == '__main__':
    app.run(debug=True)