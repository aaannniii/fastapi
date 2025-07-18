from pydantic import BaseModel

class Patient(BaseModel):
    # Define the ideal schema for the Patient model
    name: str
    age: int

def insert_patient_info(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')

def update_patient_info(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Updated')

patient_info = {"name": "John Doe", "age": 30}

# Create an instance of the Patient model using the provided patient_info dictionary
# unpacking the dictionary into the Patient model from patient_info to (**patient_info)
patient1 = Patient(**patient_info)

insert_patient_info(patient1)
update_patient_info(patient1)