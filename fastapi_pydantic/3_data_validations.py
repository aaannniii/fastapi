from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Optional, Dict

class Patient(BaseModel):

    # Define the ideal schema for the Patient model
    # Fields defined are by-default are required, unless you set them to Optional or provide a default value
    name: str
    age: int
    weight: str
    linkedin_url: AnyUrl # Used to check linked_url is not just string, but it is valid URL format
    email: EmailStr # Used to check email is valid email format
    married: bool
    allergies: List[str] # Used to check allergies is not just string, but it is List of strings
    contact_details: Dict[str, str] # Used to check contact_details is not just string, but it is Dict of strings

patient_info = {
                    'name': 'John Doe', 'age': 30, 'weight': '70kg',
                    'linkedin_url':'https://www.linkedin.com/',
                    'email': 'ani@gmail.com', 'married': False,
                    'allergies': ['pollen', 'dust'],
                    'contact_details': {'phone': '1234567890'}
}

patient1 = Patient(**patient_info)

def insert_patient_info(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight}")
    print(f"Email: {patient.email}")
    print(f"Married: {patient.married}")
    print(f"LinkedIn URL: {patient.linkedin_url}")
    print(f"Allergies: {', '.join(patient.allergies)}")
    print(f"Contact Details: {', '.join(patient.contact_details.values())}")
    print('Inserted')

insert_patient_info(patient1)