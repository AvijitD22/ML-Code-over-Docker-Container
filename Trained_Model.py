# asking for experience
Exp = input("Enter Experience in Years :")

import joblib

# loading trained model in Trained_Model.pk1
model = joblib.load("Trained_Model.pk1")

Salary = model.predict([[ Exp ]])
print(f"Salary is { Salary }")
