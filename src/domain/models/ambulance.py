from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid

@dataclass
class AmbulanceCall:
    location: str
    emergency_type: str
    emergency_details: str
    patient_name: str
    patient_phone: str
    patient_address: str
    call_status: str = 'PENDING'
    ambulance_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    called_at: str = field(default_factory=lambda: datetime.now().isoformat())
    accepted_at: Optional[str] = None
    rejected_at: Optional[str] = None
    arrived_at: Optional[str] = None
    completed_at: Optional[str] = None
    estimated_time_of_arrival: Optional[str] = None
    estimated_time_of_completion: Optional[str] = None

    def to_dict(self):
        """Return a dictionary representation of the object"""
        return {
            'ambulance_id': self.ambulance_id,
            'location': self.location,
            'emergency_type': self.emergency_type,
            'emergency_details': self.emergency_details,
            'patient_name': self.patient_name,
            'patient_phone': self.patient_phone,
            'patient_address': self.patient_address,
            'call_status': self.call_status,
            'called_at': self.called_at,
            'accepted_at': self.accepted_at,
            'rejected_at': self.rejected_at,
            'arrived_at': self.arrived_at,
            'completed_at': self.completed_at,
            'estimated_time_of_arrival': self.estimated_time_of_arrival,
            'estimated_time_of_completion': self.estimated_time_of_completion
        }

    @staticmethod
    def from_dict(ambulance_call: dict):
        """Return an AmbulanceCall object from a dictionary"""
        return AmbulanceCall(
            ambulance_id=ambulance_call.get('ambulance_id', str(uuid.uuid4())),
            location=ambulance_call.get('location'),
            emergency_type=ambulance_call.get('emergency_type'),
            emergency_details=ambulance_call.get('emergency_details'),
            patient_name=ambulance_call.get('patient_name'),
            patient_phone=ambulance_call.get('patient_phone'),
            patient_address=ambulance_call.get('patient_address'),
            call_status=ambulance_call.get('call_status'),
            called_at=ambulance_call.get('called_at'),
            accepted_at=ambulance_call.get('accepted_at'),
            rejected_at=ambulance_call.get('rejected_at'),
            arrived_at=ambulance_call.get('arrived_at'),
            completed_at=ambulance_call.get('completed_at'),
            estimated_time_of_arrival=ambulance_call.get('estimated_time_of_arrival'),
            estimated_time_of_completion=ambulance_call.get('estimated_time_of_completion')
        )