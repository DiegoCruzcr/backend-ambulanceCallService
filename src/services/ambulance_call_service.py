from src.domain.models.ambulance import AmbulanceCall
from src.repository.ambulance_call_repository import AmbulanceCallRepository


class AmbulanceCallService:
    def __init__(self, ambulance_call_repository: AmbulanceCallRepository):
        self.ambulance_call_repository = ambulance_call_repository

    def call_ambulance(self, ambulance_call: AmbulanceCall):
        return self.ambulance_call_repository.save(ambulance_call)
