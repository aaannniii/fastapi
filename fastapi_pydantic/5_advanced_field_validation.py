from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict

# Field validators are used to validate the fields of the model
# Field validators are class methods. It takes 2 arguments, cls and value.
# Field validator operates in 2 modes: Before mode and After mode
#Type coercion, also known as type conversion, is the automatic or implicit conversion of values from one data type to another in programming languages.
# Before mode is used to validate the value before it is assigned to the field.
# After mode is used to validate the value after it is assigned to the field.
# Default value will be 'after' mode, if not specified. Even if we remove mode='after' it will work as 'after' mode.

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        # if not value.endswith('@gmail.com'):
        #     raise ValueError('Email must be a Gmail address')
        # return value

        valid_domain = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domain:
            raise ValueError(f'Email must be from one of the following domains: {", ".join(valid_domain)}')
        return value

    @field_validator('name')
    @classmethod
    def validate_name(cls, value):
        return value.upper()

    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age must be a positive integer')

patient_info = {'name': 'John Doe', 'age': '30', 'email': 'abc@hdfc.com',  'weight': 70, 'married': False, 'allergies': ['pollen', 'dust'],
                'contact_details': {'phone': '1234567890'}}

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