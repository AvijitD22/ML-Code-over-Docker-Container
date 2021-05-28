#importing required modules
import pandas as pd

# importing dataset
dataset = pd.read_csv("Salary_Data.csv")

# setting row and column to x and y
y = dataset["Salary"]
x = dataset["YearsExperience"]

# import LinearRegression
from sklearn.linear_model import LinearRegression

# Setting up Model
model = LinearRegression()

# converting into numpy array
x = x.values

# reshaping the x column
x = x.reshape(30,1)

# training the model
model.fit(x,y)

<<<<<<< HEAD
#importing joblib to save the trained model
import joblib
=======

# storing the output in output variable 
output = model.predict([[ Exp ]])
>>>>>>> 9f7a978619129231245d6aa8f53079aae752d070

# no need to run this id Trained_Model.py is present in repo
joblib.dump(model , "Trained_Model.pk1")
