import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Create first line of best fit
    m, b, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"])
    years = pd.Series(range(1880, 2051))
    ax.plot(years, b + m*years,
            'salmon', label='first line of best fit')

    # Create second line of best fit
    df2 = df[df["Year"] >= 2000]
    m2, b2, r_value2, p_value2, std_err2 = linregress(
        df2["Year"], df2["CSIRO Adjusted Sea Level"])
    years2 = pd.Series(range(2000, 2051))
    ax.plot(years2, b2 + m2*years2,
            'wheat', label='second line of best fit')

    # Add labels and title
    ax.set(xlabel="Year", ylabel="Sea Level (inches)", title="Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
