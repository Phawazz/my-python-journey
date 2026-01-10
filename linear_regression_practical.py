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
