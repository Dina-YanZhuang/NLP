import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm 

# Load the dataset
df = pd.read_csv('Data.csv')
df['duration'] = np.log(df['duration'])

# Get x,y values as lists
x = df.iloc[:,2:].values
y = df.iloc[:,1:2].values

# Training the model (fitting a line)
reg = linear_model.LinearRegression()
reg.fit(x, y) 
y_pred = reg.predict(x)

# Plot data spots and linear line
plt.scatter(x, y, color = 'g')
plt.plot(x, y_pred, color = 'k')

# Set labels and title
plt.xlabel('Surprisal')  # Label for the x-axis
plt.ylabel('Duration')  # Label for the y-axis
plt.title('Linear Model of Durations and Surprisal')  # Title of the histogram

# Get model coefficients
intercept = reg.intercept_
coefficient = reg.coef_[0]
r_squared = reg.score(x, y)

# Display sklearn results
print("Intercept:", intercept)
print("Coefficient:", coefficient)
print("R-squared:", r_squared)

# Step 5: Use statsmodels for p-values
x_with_constant = sm.add_constant(x)  # Add constant for intercept
sm_model = sm.OLS(y, x_with_constant).fit()
print(sm_model.summary())  # Detailed regression results, including p-value

# Save the plot as a PNG file
plt.savefig('LinearModel.png')