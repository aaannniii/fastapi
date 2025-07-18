# Serialization is used to convert complex data types, such as objects, into a format that can be easily rendered into JSON, XML, or other content types.
# In Pydantic, serialization is done automatically when you convert a model to a dictionary or JSON.
# In Serialization, Pydantic models can be exported as python dictionary or JSON format.
# Pydantic gives us a built-in method with the help of we can export existing method as python dictionary
# Pydantic gives us a built-in method with the help of it we can export existing methods called `dict()` to convert the model to a dictionary.

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
    address: Address
    gender: str = 'Male' # Default. If we use exclude_unset=True, it will not be included in the output if not set.

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

# Convert the existing model object to a dictionary
temp = patient1.model_dump()
print(temp)
print(type(temp))

# With model_dump(), we can also specify/control the fields to be included in the output. we can include or exclude fields.
temp = patient1.model_dump(include=['name', 'address'])
print(temp, end='\n\n')

# With model_dump(), we can also specify/control the fields to be excluded in the output.
temp = patient1.model_dump(exclude={'address':['city']})
print(temp, end='\n\n')

# with exclude_unset=True, we can exclude the fields that are not set in the model.
temp = patient1.model_dump(exclude_unset=True)
print(temp, end='\n\n')

# Convert the existing model object to a JSON string
temp_json = patient1.model_dump_json()
print(temp_json)
print(type(temp_json))

