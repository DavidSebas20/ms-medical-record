from pydantic import BaseModel
from typing import List
from app.models import ClinicalRecord

class PatientData(BaseModel):
    patient_id: str
    name: str
    age: int
    allergies: List[str]
    major_diseases: List[str]

class ClinicalHistory(BaseModel):
    patient_data: PatientData
    records: List[ClinicalRecord]