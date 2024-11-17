from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4]])
# A 2D array for input data.
y = np.array([2, 4, 6, 8])
# A 1D array for target values.

model = LinearRegression()
model.fit(X, y)
# Trains the model using the data.

print("Prediction for 5:", model.predict([[10]])[0])
# Makes a prediction for the input value 5.
