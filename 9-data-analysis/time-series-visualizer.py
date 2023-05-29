import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
# print(df.isna().sum())
# print(df.dtypes)
df.index = pd.to_datetime(df.index)
df = df[df["value"].between(
    df["value"].quantile(.025), df["value"].quantile(.975))]
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

# print(df.dtypes)


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    ax = sns.lineplot(df, legend='brief')
    ax.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
           xlabel='Date', ylabel='Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    # print(df_bar.dtypes)
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax = sns.barplot(df_bar, y='value', x='year', hue='month',
                     hue_order=months, errorbar=None)
    ax.set(xlabel='Years', ylabel='Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'], df_box['month'] = df_box['date'].dt.year, df_box['date'].dt.strftime(
        '%b')

    # Draw box plots (using Seaborn)
    df_box['monthnum'] = df.index.month
    df_box = df_box.sort_values('monthnum')

    fig, ax = plt.subplots(1, 2)
    sns.boxplot(df_box, x='year', y='value', ax=ax[0]).set(
        xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')
    sns.boxplot(df_box, x='month', y='value', ax=ax[1]).set(
        xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
