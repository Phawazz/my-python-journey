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
predicted_scores = [2.5, 0.0, 2.1, 7.8]

mse = calculate_mse(actual_scores, predicted_scores)
print(f"The mean squared error is {mse}")