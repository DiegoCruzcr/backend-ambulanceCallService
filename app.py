from datetime import datetime
import json
from flask import Flask, make_response, request
import logging
import os
from src.clients.matrix_api_client import MatrixApiClient
from src.domain.models.ambulance import AmbulanceCall
from src.repository.ambulance_call_repository import AmbulanceCallRepository
from src.repository.mongo_client import MongoClient
from src.services.ambulance_call_service import AmbulanceCallService

app = Flask(__name__)

logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)

@app.route('/call', methods=['POST'])
def call_ambulance():  # put application's code here
    try:

        body = request.json

        logger.info('request body: %s', body)

        ambulance_call = AmbulanceCall.from_dict(body)
        config = {
            'MONGO_URI': os.getenv('MONGO_URI'),
            'MONGO_DB': 'ambulancecalls',
            'MONGO_COLLECTION': 'ambulancecallmanagement'
        }
        print(config)
        database = MongoClient(config)
        logger.info('database: %s, os: %s', database,
                    os.getenv('MONGO_URI'))
        
        ambulance_call_repository = AmbulanceCallRepository(database)

        ambulance_call: dict = AmbulanceCallService(ambulance_call_repository).call_ambulance(ambulance_call)

        r = make_response(json.dumps(ambulance_call), 200)
        r.headers['Content-Type'] = 'application/json'
        r.headers.add("Access-Control-Allow-Origin", "*")
        r.headers.add("Access-Control-Allow-Headers", "*")
        r.headers.add("Access-Control-Allow-Methods", "*")

        return r
    except Exception as e:
        logging.error('error: %s', e)
        return json.dumps({'error': str(e)}), 500
    
@app.route('/call/<call_id>', methods=['GET'])
def get_call(call_id):
    try:
        config = {
            'MONGO_URI': os.getenv('MONGO_URI'),
            'MONGO_DB': 'ambulancecalls',
            'MONGO_COLLECTION': 'ambulancecallmanagement'
        }
        print(config)
        database = MongoClient(config)
        logger.info('database: %s, os: %s', database,
                    os.getenv('MONGO_URI'))
        
        ambulance_call_repository = AmbulanceCallRepository(database)

        ambulance_call: dict = AmbulanceCallService(ambulance_call_repository).get_call(call_id)

        r = make_response(json.dumps(ambulance_call), 200)
        r.headers['Content-Type'] = 'application/json'
        r.headers.add("Access-Control-Allow-Origin", "*")
        r.headers.add("Access-Control-Allow-Headers", "*")
        r.headers.add("Access-Control-Allow-Methods", "*")

        return r
    except Exception as e:
        logging.error('error: %s', e)
        return json.dumps({'error': str(e)}), 500

@app.route('/')
def hello_world():
    return 'Hello, 7777!'