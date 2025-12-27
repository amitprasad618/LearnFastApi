from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give me name of the patient in less than 50 char', examples=['Amit', 'Jyoti'])]
    email: str
    linkdin_url: AnyUrl
    age: int= Field(gt=0, lt=110)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_detail: Dict[str, str]

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Updated")

patient_info = {'name': "Amit", 'email': 'anbd@jjshdi.com', 'linkdin_url': 'https://linkdin.com/jhadjhs', 'age': '30', 'weight': 71.23, 'contact_detail': {'phone': '928498249', 'pin': '6726439'}}

patient1 = Patient(**patient_info) # '**' Take all key–value pairs from the dictionary and pass them as named arguments to the function or class.

update_patient_data(patient1)