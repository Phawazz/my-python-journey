def calculate_mse(y_true, y_pred): # calculating mean squared error manually
    
    n = len(y_true)
    sum_error = 0
    
    for i in range(n):
        # Calculate the difference, square it, and add to sum
        error =  y_true[i] - y_pred[i]
        sum_error += (error ** 2)
        
    return sum_error / n
    
# Testing with a dummy data

actual_scores = [65, 70, 78, 90]
predicted_scores = [45, 50, 61, 78]

mse = calculate_mse(actual_scores, predicted_scores)
print(f"The mean squared error is {mse}")


# Gradient descent

import numpy as np

x = np.array([65, 70, 78, 90])
y = np.array([45, 50, 61, 78])

#Hyperparameters: Initial targets
m = 0
c = 0
learning_rate = 0.000001
epochs = 1000

n = len(x)

for i in range(epochs):
    y_pred = m * x + c
    
    d_m = (-2/n) * sum(x * y - y_pred)
    d_c = (-2/n) * sum(y - y_pred)
    
    m = m - learning_rate * d_m
    c = c - learning_rate * d_c
    
    if i % 100 == 0:
        print(f"Epoch {i}: m={m:.4f}, c={c:.4f}")

print(f"\nFinal Model: y = {m:.4f}x + {c:.4f}")

