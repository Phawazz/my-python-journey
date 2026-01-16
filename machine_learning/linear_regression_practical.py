"""
Linear Regression Practice: 
Three simple exercises on visualization, prediction, and evaluation from my ongoing ALX data science program

"""

# Exercise 1: average temperature vs solar panel output

average_temperature = [5, 8, 11, 13, 18, 24, 24, 28, 32, 36]
solar_output = [2.2, 1.8, 2.5, 3.0, 4.5, 5.3, 5.8, 4.2, 2.5, 4.0]
# insert code here

import numpy as np
import matplotlib.pyplot as plt

average_temperature = np.array([5, 8, 11, 13, 18, 24, 24, 28, 32, 36])
solar_output = np.array([2.2, 1.8, 2.5, 3.0, 4.5, 5.3, 5.8, 4.2, 2.5, 4.0])

plt.scatter(average_temperature, solar_output)
plt.title("Average temperature vs Solar panel output")
plt.xlabel("Average temperature (in degrees Celsius)")
plt.ylabel("Solar Output (kWh)")
plt.show()

# Exercise 2: Annual rainfall vs Agricultural yield

annual_rainfall = [800, 1200, 1000, 1500, 1100, 1300, 900, 1400, 950, 1250]
agricultural_yield = [3.2, 4.8, 4.0, 5.5, 4.2, 5.0, 3.5, 5.3, 3.8, 4.9]
# insert code here

import numpy as np
from sklearn.linear_model import LinearRegression

annual_rainfall = np.array([800, 1200, 1000, 1500, 1100, 1300, 900, 1400, 950, 1250]).reshape(-1, 1)
agricultural_yield = np.array([3.2, 4.8, 4.0, 5.5, 4.2, 5.0, 3.5, 5.3, 3.8, 4.9])

lm = LinearRegression()
lm.fit(annual_rainfall, agricultural_yield)

predicted_yield = lm.predict(np.array([[1150]]))
print(f"Predicted agricultural yield for 1150 mm of annual rainfall: {predicted_yield[0]:.2f} tons of hectare")


# Exercise 3: Traffic volume vs Pollution levels
traffic_volume = [1500, 2500, 2000, 3000, 3500, 1800, 4000, 2200, 2800, 3200]
pollution_levels = [35, 50, 45, 60, 65, 38, 70, 48, 55, 62]
# insert code here

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

traffic_volume = np.array([1500, 2500, 2000, 3000, 3500, 1800, 4000, 2200, 2800, 3200]).reshape(-1, 1)
pollution_levels = np.array([35, 50, 45, 60, 65, 38, 70, 48, 55, 62])

model = LinearRegression()
model.fit(traffic_volume, pollution_levels)

predicted_pol_levels = model.predict(traffic_volume)

mse = mean_squared_error(pollution_levels, predicted_pol_levels)
r_squared = r2_score(pollution_levels, predicted_pol_levels)

print(f"Mean Squared Error(MSE): {mse:.2f}")
print(f"R-squared: {r_squared:.2f}")

plt.scatter(traffic_volume, pollution_levels)
plt.plot(traffic_volume, predicted_pol_levels, color = 'red')
plt.xlabel("Traffic Volume")
plt.ylabel("Pollution Levels")
plt.title("Traffic Volume vs Pollution Levels")
plt.show()

# Calculating the pearson's correlation coefficient using scipy
import pandas as pd
from scipy.stats import pearsonr

data = {
    "student_id": range(1, 11),
    "study_hours": [2,3,4,5,6,7,8,9,10,11],
    "sleep_hours": [5,6,6,7,7,8,8,9,9,9],
    "screen_time": [8,7,6,5,4,3,2,2,1,1],
    "attendance": [60,65,70,75,80,85,90,92,95,97],
    "exam_score": [55,58,62,68,72,78,82,88,92,95]
}

dataset = pd.DataFrame(data)

def get_correlation(df, col1, col2):
    """"
    Returns the pearson correlation coefficient between two numeric columns
    
    Parameters:
        df (pd.Daaframe): Input dataframe
        col1 (str): First column name
        col2 (str): Second column name
        
    Returns:
        float: pearson correlation coefficient
    """
    r, _ = pearsonr(df[col1], df[col2])
    return r

# Calling the function...
correlation = get_correlation(dataset, "study_hours", "exam_score")
print(f"Pearson correlation: {correlation:.3f}")

# Histogram of Residuals for traffic vs pollution
import matplotlib.pyplot as plt

residuals = pollution_levels - predicted_pol_levels

plt.figure(figsize=(10, 6))
plt.hist(residuals, bins=20, edgecolor='black')
plt.title('Distribution of residuals')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()
# Histogram of residuals turned out not to be normally distributed, meaning 'Normality', one of the assumptions for linear regression is absent in the data


# Scatter plot of residuals vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(predicted_pol_levels, residuals, edgecolors='black')
plt.title('Residuals vs Predicted values')
plt.xlabel('Predicted pollution levels')
plt.ylabel('Residuals')
plt.axhline(y=0, color='r', linestyle='--')
plt.show()