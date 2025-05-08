import method
import numpy as np
import matplotlib.pyplot as plt

x = np.array([-5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
y1 = np.array([-0.1923, -0.2118, -0.2353, -0.2642, -0.3, -0.3448, -0.4000, -0.4615, -0.5000, -0.4000, 0, 0.4000, 0.5000, 0.4615, 0.4000, 0.3448, 0.3000, 0.2642, 0.2353, 0.2118, 0.1923])

data = list(zip(x, y1))

predict_x1=-3.75
predict_x2= 0.25

predict_y1_lagrange=method.lagrange_method(data, predict_x1)
predict_y1_linear=method.linear_method(data, predict_x1)
print(f"Predicted y value at x={predict_x1} is {predict_y1_lagrange}")
print(f"Predicted y value at x={predict_x1} is {predict_y1_linear}")

predict_y2_lagrange=method.lagrange_method(data, predict_x2)
predict_y2_linear=method.linear_method(data, predict_x2) 
print(f"Predicted y value at x={predict_x2} is {predict_y2_lagrange}")
print(f"Predicted y value at x={predict_x2} is {predict_y2_linear}")
