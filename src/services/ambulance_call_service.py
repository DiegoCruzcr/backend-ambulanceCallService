from datetime import datetime
import os
from src.clients.matrix_api_client import MatrixApiClient
from src.domain.models.ambulance import AmbulanceCall
from src.repository.ambulance_call_repository import AmbulanceCallRepository


class AmbulanceCallService:
    def __init__(self, ambulance_call_repository: AmbulanceCallRepository):
        self.ambulance_call_repository = ambulance_call_repository

    def call_ambulance(self, ambulance_call: AmbulanceCall):
        matrix_distance = MatrixApiClient(os.getenv('MATRIX_HOMESERVER_URL'),
                                           os.getenv('ACCESS_KEY')).get_calculated_matrix_distance(origin=ambulance_call.location,
                                                                                                    destination='-23.473076903538775%2C-46.68594245685031')

        ambulance_call.accepted_at = str(datetime.now().isoformat())
        ambulance_call.call_status = 'ACCEPTED'
        ambulance_call.estimated_time_of_arrival = matrix_distance['rows'][0]['elements'][0]['duration']['text']
        ambulance_call.estimated_time_of_completion = matrix_distance['rows'][0]['elements'][0]['duration']['text']

        self.ambulance_call_repository.save(ambulance_call)
        return ambulance_call.to_dict()
    
    def get_call(self, call_id):
        return self.ambulance_call_repository.find_by_id(call_id)
