from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

# Model validators are used to validate the fields of the model
# Model validators are class methods. It takes 2 arguments, cls and value.
# Model validator operates in 2 modes: Before mode and After mode
#Type coercion, also known as type conversion, is the automatic or implicit conversion of values from one data type to another in programming languages.
# Before mode is used to validate the value before it is assigned to the field.
# After mode is used to validate the value after it is assigned to the field.
# Default value will be 'after' mode, if not specified. Even if we remove mode='after' it will work as 'after' mode.
# Works on the entire model, not just a single field.
class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency_contact' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients above 60 years of age')
        return model

patient_info = {'name': 'John Doe', 'age': '30', 'email': 'abc@hdfc.com',  'weight': 70, 'married': False, 'allergies': ['pollen', 'dust'],
                'contact_details': {'phone': '1234567890', 'emergency_contact': '8888888888'}}

patient1 = Patient(**patient_info)

def insert_patient_info(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight}")
    print(f"Email: {patient.email}")
    print(f"Married: {patient.married}")
    print(f"Allergies: {', '.join(patient.allergies)}")
    print(f"Contact Details: {', '.join(patient.contact_details.values())}")
    print('Inserted')

insert_patient_info(patient1)