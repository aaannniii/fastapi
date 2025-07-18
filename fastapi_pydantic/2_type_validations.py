from pydantic import BaseModel
from typing import List, Optional, Dict

class Patient(BaseModel):

    # Define the ideal schema for the Patient model
    # Fields defined are by-default are required, unless you set them to Optional or provide a default value
    name: str
    age: int
    weight: str
    married: Optional[bool] = None # Used to check married is not just boolean,
    # but it is Optional boolean. If nothing defined then we will get None in the output.
    # We can give default value as well.
    # We can make allergies and contact_details as Optional as well, if we want to make them optional. Optional[List[str]] or Optional[Dict[str, str]]
    allergies: List[str] # Used to check allergies is not just string, but it is List of strings
    contact_details: Dict[str, str] # Used to check contact_details is not just string, but it is Dict of strings
    test: str = 'test' # Used to check test is not just string, but it is string with default value

patient_info = {'name': 'John Doe', 'age': 30, 'weight': '70kg', 'married': False, 'allergies': ['pollen', 'dust'],
                'contact_details': {'email': 'abc@gmail.com', 'phone': '1234567890'}}

patient1 = Patient(**patient_info)

def insert_patient_info(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight}")
    print(f"Married: {patient.married}")
    print(f"Allergies: {', '.join(patient.allergies)}")
    print(f"Contact Details: {', '.join(patient.contact_details.values())}")
    print('Inserted')

insert_patient_info(patient1)