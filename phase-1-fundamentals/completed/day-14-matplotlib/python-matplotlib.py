"""
[ ] Day 14: Data Visualization with Matplotlib
• Topic: Plotting data (line plots, bar charts).
• Resource: Matplotlib Tutorials (official site).
• Task: Plot a week’s worth of simulated heart rate data.
"""

# Day 14
# Task: Plot a week’s worth of simulated heart rate data

# Imports
import pandas as pd
from matplotlib import pyplot as plt

# Import data set
hr_data = pd.read_csv('./heart_rate_data.csv')

# Plot the data set
plt.plot(hr_data['date'], hr_data['heart_rate'])

# Display the data
plt.show()