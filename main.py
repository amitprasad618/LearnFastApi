from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

        return data


@app.get("/")
def hello():
    return {'message':'HI Bro'}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/view/{patient_id}')
def viewByID(patient_id: int = Path(..., description='Id of the patient', example=3)):  #... mtlb require hai
    #load all the patient
    data = load_data()

    for patient in data:
        if patient["id"] == patient_id:
            return patient

    raise HTTPException(
        status_code=404,
        detail="Data does not exist in database"
    )

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the bases of id or age'), order: str = Query('asc', description='sort in asc or desc order')):
    valid_field = ['age', 'id']

    if sort_by not in valid_field:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field selected from {valid_field}"
        )
    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400,
            detail="Invalid order selected. Please select order between asc and desc"
        ) 
    data = load_data()

    reverse = True if order == 'desc' else False
    sorted_data = sorted(data, key=lambda x: x.get(sort_by, 0), reverse=reverse)

    return sorted_data
