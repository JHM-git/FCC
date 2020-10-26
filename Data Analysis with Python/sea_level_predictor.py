import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots(figsize=(16,9))
    plt.scatter(x, y)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    x_fut = x.tolist() + np.arange(2014, 2050).tolist()
    x_fut = np.array(x_fut, dtype=np.float64)
    plt.plot(x_fut, intercept + slope*x_fut, 'g')

    # Create second line of best fit
    slope_fut, intercept_fut, r_value_fut, p_value_fut, std_err_fut = linregress(x[120::], y[120::])
    plt.plot(x_fut[120::], intercept_fut + slope_fut*x_fut[120::], 'r')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
        
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()