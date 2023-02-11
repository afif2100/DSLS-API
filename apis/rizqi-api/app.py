from fastapi import FastAPI

app = FastAPI()

@app.get('/hi')
def hello():
    return {'msg': 'Hello World'}

@app.get('/health')
def health_check():
    return {'msg': 'Healthy'}

from pydantic import BaseModel

class Employee(BaseModel):
    name: str = 'Rizqi'
    age: int = 22

@app.post('/hello')
def hello_name(emp:Employee):
    return {'msg': f'Hello {emp.name} , Umur kamu {emp.age}'}

class PredictSalary():
    def __init__(self) -> None:
        self.base_salary = 5000000
        self.age_salary = 100000
        print('Model Predict Salary has been loaded')

    def load_model(self):
        self.model = pickle.load('model.pkl')

    def predict(self, name, age):
        salary = self.base_salary + (self.age_salary * age)
        return {'Nama':name, 'Age':age, 'Salary_prediction':salary}

salary_model = PredictSalary()

@app.post('/predict')
def predict(emp: Employee):
    return salary_model.predict(emp.name, emp.age)

# To run the app
# uvicorn app:app --host 0.0.0.0 --port 8081