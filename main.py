from fastapi import FastAPI
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

patients = load_data()
print(patients[0]["name"])