from datetime import datetime
import json
import uuid
from flask import Flask, make_response, request
import logging
import os
from src.clients.matrix_api_client import MatrixApiClient
from src.domain.models.ambulance import AmbulanceCall
from src.domain.models.task import Task
from src.repository.ambulance_call_repository import AmbulanceCallRepository
from src.repository.mongo_client import MongoClient
from src.repository.registration_repository import RegistrationRepository
from src.repository.task_repository import TaskRepository
from src.services.ambulance_call_service import AmbulanceCallService
from flask_cors import CORS
from src.services.registration_service import RegistrationService

from src.services.task_service import TaskService

app = Flask(__name__)
CORS(app)

logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)

@app.route('/call', methods=['POST', 'OPTIONS'])
def call_ambulance():  # put application's code here
    try:
        if request.method == 'OPTIONS':
            return '', 200

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
        return r
    except Exception as e:
        logging.error('error: %s', e)
        return json.dumps({'error': str(e)}), 500
    
@app.route('/call/<call_id>', methods=['GET', 'OPTIONS'])
def get_call(call_id):
    try:
        if request.method == 'OPTIONS':
            return '', 200
        
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

        return r
    except Exception as e:
        logging.error('error: %s', e)
        return json.dumps({'error': str(e)}), 500
    
@app.route('/calls', methods=['GET', 'OPTIONS'])
def list_calls():
    try:
        if request.method == 'OPTIONS':
            return '', 200
        
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

        ambulance_call: dict = AmbulanceCallService(ambulance_call_repository).list_calls()

        r = make_response(json.dumps(ambulance_call), 200)
        r.headers['Content-Type'] = 'application/json'

        return r
    except Exception as e:
        logging.error('error: %s', e)
        return json.dumps({'error': str(e)}), 500
    
# ESG mobile backend
@app.route('/esg/task', methods=['POST', 'OPTIONS'])
def create_task():
    try:
        if request.method == 'OPTIONS':
            return '', 200
        
        body = request.json

        logger.info('request body: %s', body)

        task = Task.from_dict(body)
        config = {
            'MONGO_URI': os.getenv('MONGO_URI'),
            'MONGO_DB': 'esg',
            'MONGO_COLLECTION': 'esgenterprisemanagement'
        }
        database = MongoClient(config)
        logger.info('database: %s, os: %s', database,
                    os.getenv('MONGO_URI'))
        
        task_repository = TaskRepository(database)

        task: dict = TaskService(task_repository).create_task(task)

        r = make_response(json.dumps(task), 200)
        r.headers['Content-Type'] = 'application/json'
        return r
    except Exception as e:
        logging.error('error: %s', e)
        return json.dumps({'error': str(e)}), 500

@app.route('/esg/task/<task_id>', methods=['PUT', 'OPTIONS'])
def update_task(task_id):
    try:
        if request.method == 'OPTIONS':
            return '', 200
        
        body = request.json
        body['task_id'] = task_id

        logger.info('request body: %s', body)

        task = Task.from_dict(body)
        config = {
            'MONGO_URI': os.getenv('MONGO_URI'),
            'MONGO_DB': 'esg',
            'MONGO_COLLECTION': 'esgenterprisemanagement'
        }
        database = MongoClient(config)
        logger.info('database: %s, os: %s', database,
                    os.getenv('MONGO_URI'))
        
        task_repository = TaskRepository(database)

        task: dict = TaskService(task_repository).update_task(task_id, task)

        r = make_response(json.dumps(task), 200)
        r.headers['Content-Type'] = 'application/json'
        return r
    except Exception as e:
        logging.error('error: %s', e)
        return json.dumps({'error': str(e)}), 500
    
@app.route('/esg/task/<task_id>', methods=['GET', 'OPTIONS'])
def get_task(task_id):
    try:
        if request.method == 'OPTIONS':
            return '', 200
        
        config = {
            'MONGO_URI': os.getenv('MONGO_URI'),
            'MONGO_DB': 'esg',
            'MONGO_COLLECTION': 'esgenterprisemanagement'
        }
        database = MongoClient(config)
        logger.info('database: %s, os: %s', database,
                    os.getenv('MONGO_URI'))
        
        task_repository = TaskRepository(database)

        task: dict = TaskService(task_repository).get_task_by_id(task_id)

        r = make_response(json.dumps(task), 200)
        r.headers['Content-Type'] = 'application/json'

        return r
    except Exception as e:
        logging.error('error: %s', e)
        return json.dumps({'error': str(e)}), 500

@app.route('/esg/task', methods=['GET', 'OPTIONS'])
def list_tasks():
    try:
        if request.method == 'OPTIONS':
            return '', 200
        
        config = {
            'MONGO_URI': os.getenv('MONGO_URI'),
            'MONGO_DB': 'esg',
            'MONGO_COLLECTION': 'esgenterprisemanagement'
        }
        database = MongoClient(config)
        logger.info('database: %s, os: %s', database,
                    os.getenv('MONGO_URI'))
        
        task_repository = TaskRepository(database)

        task: dict = TaskService(task_repository).list_tasks()

        r = make_response(json.dumps(task), 200)
        r.headers['Content-Type'] = 'application/json'

        return r
    except Exception as e:
        logging.error('error: %s', e)
        return json.dumps({'error': str(e)}), 500
    
@app.route('/esg/task/<task_id>', methods=['DELETE', 'OPTIONS'])
def delete_task(task_id):
    try:
        if request.method == 'OPTIONS':
            return '', 200
        
        config = {
            'MONGO_URI': os.getenv('MONGO_URI'),
            'MONGO_DB': 'esg',
            'MONGO_COLLECTION': 'esgenterprisemanagement'
        }
        database = MongoClient(config)
        logger.info('database: %s, os: %s', database,
                    os.getenv('MONGO_URI'))
        
        task_repository = TaskRepository(database)

        task: dict = TaskService(task_repository).delete_task(task_id)

        r = make_response(json.dumps(task), 200)
        r.headers['Content-Type'] = 'application/json'

        return r
    except Exception as e:
        logging.error('error: %s', e)
        return json.dumps({'error': str(e)}), 500
    
@app.route('/signUpCompany', methods=['POST', 'OPTIONS'])
def signUpCompany():
    try:
        if request.method == 'OPTIONS':
            return '', 200
        
        body = request.json

        logger.info('request body: %s', body)
        config = {
            'MONGO_URI': os.getenv('MONGO_URI'),
            'MONGO_DB': 'esg',
            'MONGO_COLLECTION': 'companyusermanagement'
        }
        database = MongoClient(config)
        logger.info('database: %s, os: %s', database,
                    os.getenv('MONGO_URI'))

        repository = RegistrationRepository(database)

        RegistrationService(repository).signUpCompany(body)

        return 'Created', 201
    except Exception as e:
        logging.error('error: %s', e)
        return json.dumps({'error': str(e)}), 500
    
@app.route('/signUpUser', methods=['POST', 'OPTIONS'])
def signUpUser():
    try:
        if request.method == 'OPTIONS':
            return '', 200
        
        body = request.json
        body['user_id'] = str(uuid.uuid4())

        logger.info('request body: %s', body)
        config = {
            'MONGO_URI': os.getenv('MONGO_URI'),
            'MONGO_DB': 'esg',
            'MONGO_COLLECTION': 'companyusermanagement'
        }
        database = MongoClient(config)
        logger.info('database: %s, os: %s', database,
                    os.getenv('MONGO_URI'))

        repository = RegistrationRepository(database)

        RegistrationService(repository).signUpUser(body)

        return 'Created', 201
    except Exception as e:
        logging.error('error: %s', e)
        return json.dumps({'error': str(e)}), 500

@app.route('/login', methods=['POST', 'OPTIONS'])
def login():
    try:
        if request.method == 'OPTIONS':
            return '', 200
        
        body = request.json

        logger.info('request body: %s', body)
        config = {
            'MONGO_URI': os.getenv('MONGO_URI'),
            'MONGO_DB': 'esg',
            'MONGO_COLLECTION': 'companyusermanagement'
        }
        database = MongoClient(config)
        logger.info('database: %s, os: %s', database,
                    os.getenv('MONGO_URI'))

        repository = RegistrationRepository(database)

        user = RegistrationService(repository).login(body)
        response = make_response(json.dumps(user), 200)
        response.headers['Content-Type'] = 'application/json'
        if user:
            return response
        else:
            return 'Unauthorized', 401
    except Exception as e:
        logging.error('error: %s', e)
        return json.dumps({'error': str(e)}), 500
    
@app.route('/loginCompany', methods=['POST', 'OPTIONS'])
def loginCompany():
    try:
        if request.method == 'OPTIONS':
            return '', 200
        
        body = request.json

        logger.info('request body: %s', body)
        config = {
            'MONGO_URI': os.getenv('MONGO_URI'),
            'MONGO_DB': 'esg',
            'MONGO_COLLECTION': 'companyusermanagement'
        }
        database = MongoClient(config)
        logger.info('database: %s, os: %s', database,
                    os.getenv('MONGO_URI'))

        repository = RegistrationRepository(database)

        user = RegistrationService(repository).loginCompany(body)
        r = make_response(json.dumps(user), 200)
        r.headers['Content-Type'] = 'application/json'

        if user:
            return r
        else:
            return 'Unauthorized', 401
    except Exception as e:
        logging.error('error: %s', e)
        return json.dumps({'error': str(e)}), 500

@app.route('/')
def hello_world():
    return 'Hello, 7777!'