import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('Data.csv')

# Round the 'duration' values to the nearest integer for histogram
df['rounded_duration'] = df['duration'].round()

# Plot the histogram
plt.figure(figsize=(10, 6))  # Set the figure size
plt.hist(df['rounded_duration'], bins=30, edgecolor='black', alpha=0.7)

# Set labels and title
plt.xlabel('Rounded Duration')  # Label for the x-axis
plt.ylabel('Frequency')  # Label for the y-axis
plt.title('Histogram of Durations and Frequency')  # Title of the histogram

# Save the plot as a PNG file
plt.savefig('Histogram.png', dpi=300)  # Save as PNG file with 300 dpi