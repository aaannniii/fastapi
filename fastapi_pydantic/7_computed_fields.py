from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

# In computed_fields, user doesn't provide any value but we can use other fields to calculate computed_fields.
# Below we will add height and bmi as computed fields.

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float # Weight in kg
    married: bool
    height: float  # Height in meters
    allergies: List[str]
    contact_details: Dict[str, str]

# Here we are using computed_field to calculate bmi based on weight and height and getting values from patient_info.
# We have to keep method name and where we need to print should be same.
# def bmi is the method name and bmi is the property name should be same.
    @computed_field()
    @property
    def bmi(self) -> float :
        bmi = round(self.weight / (self.height ** 2))
        return bmi

patient_info = {'name': 'John Doe', 'age': '30', 'email': 'abc@hdfc.com', 'height': 7.5, 'weight': 70, 'married': False, 'allergies': ['pollen', 'dust'],
                'contact_details': {'phone': '1234567890', 'emergency_contact': '8888888888'}}

patient1 = Patient(**patient_info)

def insert_patient_info(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight}")
    print(f"Email: {patient.email}")
    print(f"Married: {patient.married}")
    print(f"bmi: {patient.bmi}")
    print(f"Allergies: {', '.join(patient.allergies)}")
    print(f"Contact Details: {', '.join(patient.contact_details.values())}")
    print('Inserted')

insert_patient_info(patient1)