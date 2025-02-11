from pydantic import BaseModel
from typing import Optional
from datetime import date

class ClinicalRecord(BaseModel):
    record_id: str
    patient_id: str
    height: float
    weight: float
    heart_rate: int
    blood_pressure: str
    notes: Optional[str]
    date: date