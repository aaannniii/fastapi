from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Optional, Dict, Annotated

# Field is used to provide additional validation and attach metadata for the fields in the model
# Using Field, we can Custom data validation, can set metadata, can override type coercion, and more
# By using we can attach metadata to the fields in the model and to do that we need Annotated type to be imported.
# Using Field and Annotated we can provide custom validation.

class Patient(BaseModel):

    # Define the ideal schema for the Patient model
    # Fields defined are by-default are required, unless you set them to Optional or provide a default value
    name: Annotated[str, Field(max_length=50, title='Name of the Patient',
                               description='Name should not exceed 50 characters',
                               examples= ['Pydantic', 'FastAPI'])] # Used to check name is not just string, but it is string with max length of 50

    # Used to check age is not just integer, but it is greater than 0 and less than 120
    age: int = Field(gt=0, lt=120)

    #Used Strict type validation for weight, it should be float and greater than 0, values should be strictly float
    weight: Annotated[float, Field(gt=0, strict=True)]

    # Used to check linked_url is not just string, but it is valid URL format
    linkedin_url: AnyUrl

    # Used to check email is valid email format
    email: EmailStr

    # Used to check married is not just boolean, but it is Optional boolean. If nothing defined then we will get None in the output.
    married: Annotated[bool, Field(default=None,
                                   description='Marital status of the patient')]

    # Used to check allergies is not just string, but it is List of strings
    allergies: Annotated[Optional[List[str]], Field(max_length=5)]

    # Used to check contact_details is not just string, but it is Dict of strings
    contact_details: Dict[str, str]

patient_info = {
                    'name': 'John Doe', 'age': 30, 'weight': 70,
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

