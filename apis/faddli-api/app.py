from fastapi import FastAPI

# fastapi as app
app = FastAPI()
list_response = []

@app.get("/hi")
def Hello():
    return {"msg": "Hello World"}

@app.get("/health")
def healthCheck():
    return {"status": "Everything's Awesome!!!"}

@app.get("/append")  
def healthCheck():
    response = {"status": "Everything's Good!!!"}
    list_response.append(response)
    print(list_response)
    return response

from pydantic import BaseModel

class Employee(BaseModel):
    name: str = 'Faddli'
    age: int = 25

@app.post("/hello")
def helloName(emp: Employee):
    return {"msg": f"halo {emp.name}, Umur kamu {emp.age}"}

class PredictSalary():
    def __init__(self) -> None:
        self.baseSalary = 5000000
        self.ageSalary = 100000
        print(" Model Predict Salary Sudah Jalan")

    def load_model(self):
        self.model = pickle.load('model.pkl')
    
    def predict(self, name, age):
        salary = self.baseSalary + (self.ageSalary * age)

        response = {"Nama":name ,"Age":age ,"Salary Prediction":salary}
        return response

salaryModel = PredictSalary()

@app.post("/predict")
def predict(emp: Employee):
    return salaryModel.predict(emp.name, emp.age)



#run used 
# open terminal and copy (uvicorn app:app --host 0.0.0.0 --port 8001)