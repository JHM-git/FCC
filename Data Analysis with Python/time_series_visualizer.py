import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col='date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    x = df.index
    y = df['value']
    fig = plt.figure(figsize=(16,9))
    plt.ylabel('Page Views')
    plt.xlabel('Date')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.plot(x, y)




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month]).mean()
    df_bar = df_bar.reset_index(level=1)
    df_bar = df_bar.rename(columns={'date': 'month'})
    df_bar['month'] = pd.to_datetime(df_bar['month'], format='%m').dt.month_name()
    df_bar = df_bar.reset_index()
    df_bar = df_bar.rename(columns={'date': 'year'})

    # Draw bar plot
    labels = df_bar['year'].unique().tolist()
    January = [0] + df_bar[df_bar['month'] == 'January']['value'].values.tolist()
    February = [0] + df_bar[df_bar['month'] == 'February']['value'].values.tolist()
    March = [0] + df_bar[df_bar['month'] == 'March']['value'].values.tolist()
    April = [0] + df_bar[df_bar['month'] == 'April']['value'].values.tolist()
    May = df_bar[df_bar['month'] == 'May']['value'].values.tolist()
    June = df_bar[df_bar['month'] == 'June']['value'].values.tolist()
    July = df_bar[df_bar['month'] == 'July']['value'].values.tolist()
    August = df_bar[df_bar['month'] == 'August']['value'].values.tolist()
    September = df_bar[df_bar['month'] == 'September']['value'].values.tolist()
    October = df_bar[df_bar['month'] == 'October']['value'].values.tolist()
    November = df_bar[df_bar['month'] == 'November']['value'].values.tolist()
    December = df_bar[df_bar['month'] == 'December']['value'].values.tolist()

    x = np.arange(4)
    w = 0.04
    fig, ax = plt.subplots(figsize=(16,9))
    rec1 = ax.bar(x - w*5, January, width=w, label='January')
    rec2 = ax.bar(x - w*4, February, width=w, label='February')
    rec3 = ax.bar(x - w*3, March, width=w, label='March')
    rec4 = ax.bar(x - w*2, April, width=w, label='April')
    rec5 = ax.bar(x - w, May, width=w, label='May')
    rec6 = ax.bar(x, June, width=w, label='June')
    rec7 = ax.bar(x + w, July, width=w, label='July')
    rec8 = ax.bar(x + w*2, August, width=w, label='August')
    rec9 = ax.bar(x + w*3, September, width=w, label='September')
    rec10 = ax.bar(x + w*4, October, width=w, label='October')
    rec11 = ax.bar(x + w*5, November, width=w, label='November')
    rec12 = ax.bar(x + w*6, December, width=w, label='December')

    ax.set_ylabel('Average Page Views')
    ax.set_xlabel('Years')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(16,9))
    ax[0] = sns.boxplot(x='year', y='value', data=df_box, ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    order = df_box['month'][220:].unique().tolist()
    ax[1] = sns.boxplot(x='month', y='value', data=df_box, order=order, ax=ax[1])
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
