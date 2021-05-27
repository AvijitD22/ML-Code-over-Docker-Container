Exp = input("Enter Years of Experience :")

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

while True:
    # storing the output in output variable 
    output = model.predict([[ Exp ]])

    # printing the output
    print(output)
