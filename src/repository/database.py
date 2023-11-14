# interface to Database class

from abc import ABC, abstractmethod

from src.domain.models.ambulance import AmbulanceCall


class Database(ABC):
    @abstractmethod
    def save(self, ambulance_call: AmbulanceCall):
        pass

    @abstractmethod
    def find_by_id(self, ambulance_call_id: str):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def delete(self, ambulance_call_id: str):
        pass

    @abstractmethod
    def update(self, ambulance_call_id: str, ambulance_call: AmbulanceCall):
        pass