from src.domain.models.ambulance import AmbulanceCall
from src.repository.database import Database


class AmbulanceCallRepository:
    def __init__(self, db: Database):
        self.db = db

    def save(self, ambulance_call: AmbulanceCall):
        return self.db.save(ambulance_call)

    def find_by_id(self, ambulance_call_id: str):
        return self.db.find_by_id(ambulance_call_id)

    def find_all(self):
        return self.db.find_all()

    def delete(self, ambulance_call_id: str):
        return self.db.delete(ambulance_call_id)

    def update(self, ambulance_call_id: str, ambulance_call: AmbulanceCall):
        return self.db.update(ambulance_call_id, ambulance_call)