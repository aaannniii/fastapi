# In Pydantic, If we are using a model as a field in another model, it is called nested models.
# Can organise data in a structured way.
# In this example, we will create a Patient model that has an Address model as a field.
# Reusability: Can be used the same to different pydantic model(class)
# Readability: Easy to read and understand.
# Maintainability: If we need to change the Address model, we can do it in one place and it will reflect in all the models that use it.
# Validation: Nested values are validated automatically, so we can ensure that the data is in the correct format.
# the Address model in other models as well.

from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str = None
    address: Address

address_info = {"street": "main_str", "city": "Springfield", "state": "IL", "zip_code": "62701"}

address1 = Address(**address_info)

patient_info = {
    "name": "John Doe",
    "age": 30,
    "address": address1}

patient1 = Patient(**patient_info)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.zip_code)