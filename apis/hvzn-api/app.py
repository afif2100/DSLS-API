# app.py
from fastapi import FastAPI

# to run the app
# uvicorn app:app --host 0.0.0.0 --port 8001 --reload
# run on windows add : python -m uvicorn app:app --host 0.0.0.0 --port 8001 --reload
# open swagger http://localhost:8001/docs # for api information


# definisi object fastapi as app
app = FastAPI()
list_response = []

@app.get("/hi")
def hello():
    return {"msg": "Hello World, DSLS"}

@app.get("/health")
def health_check():
    return {"status": "healthy bos"}

@app.get("/append")
def health_check():
    resp = {"status": "healthy bos"}
    list_response.append(resp)
    print(list_response)
    return resp


from pydantic import BaseModel

# create input datamodel
class Employee(BaseModel):
    name: str = 'hvzn'
    age: int = 9


@app.post("/hello")
def hello_name(emp: Employee):
    return {"msg": f"Hallo {emp.name}, Umur kamu {emp.age}"}

# membuat kelas predict salary function
class PredictSalary():
    def __init__(self) -> None:
        self.base_salary = 5000000
        self.age_salary = 100000
        print("Model Predict Salary Sudah Loaded")
    
    def load_model(self):
        self.model = pickle.load('model.pkl')
                
    def predict(self, name, age):
        salary = self.base_salary + (self.age_salary * age)
        return {"Nama":name ,"Age":age ,"Salary_Prediction":salary }

# membuat object salary model
salary_model = PredictSalary()

@ app.post("/predict")
def predict(emp: Employee):
    return salary_model.predict(emp.name, emp.age)
