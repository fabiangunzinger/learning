# Packages
import pandas as pd
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import plotly.graph_objects as go
import plotly.express as px
import country_converter as coco
import missingno as msno
import os
import re
import glob


# Aliases
idx = pd.IndexSlice 

data_dir = '/Users/fabiangunzinger/Library/Mobile Documents/com~apple~CloudDocs/fab/projects/python_pottering/data/gapminder'
fig_dir = '/Users/fabiangunzinger/Library/Mobile Documents/com~apple~CloudDocs/fab/projects/python_pottering/figures'


# Import Gapminder data and create a single data frame

csvs = glob.glob(os.path.join(data_dir, 'gap*'))

def melted_df(csv):
    '''Converts csvs to melted dataframes with country-year 
    multi-index and extracts value_name from csv name.'''
    valname = re.findall("gap_(.*?).csv", csv)[0]
    df = pd.read_csv(csv)
    df = pd.melt(df, id_vars='country', var_name='year', value_name=valname)
    df.set_index(['country', 'year'], inplace=True)
    return df

dfs = list(map(melted_df, csvs))
data = pd.concat(dfs, axis=1, sort=True)
data.reset_index(inplace=True)

# Add country info

cc = coco.CountryConverter()
cinfo = cc.data
cinfo.columns = map(str.lower, cinfo.columns)
cinfo = cinfo[['oecd', 'euro', 'iso2', 'unregion', 'continent', 'name_short']]
cinfo.euro = cinfo.euro.notnull().astype('int')
cinfo.oecd = cinfo.oecd.notnull().astype('int')

name_short = list(cinfo.name_short)
country = list(data.country.unique())

matches = coco.match(country, name_short)
s = pd.Series(matches, name='name_short')
s.index.name = 'country'
matches = s.reset_index()

data = pd.merge(data, matches, how='left', on='country')
data = pd.merge(data, cinfo, how='left', on='name_short')

data['date'] = pd.to_datetime(data.year)

data.set_index(['country', 'date'], inplace=True)

data.sample()
data.info()



# Look at Missing data patterns

msno.matrix(data)



# '''''''' Beautiful tables '''''''' #


# Create nice table for sample of Swiss data with plotly

ch = data.loc['Switzerland']

fig = go.Figure()

fig.add_trace(
    go.Table(header=dict(values=ch.columns, fill_color='paleturquoise'),
             cells=dict(values=ch.sample(20).T, fill_color='lavender'))
)

fig.show()


# '''''''' Exploratory data analysis '''''''' #


# GPD per capita growth for each continent

df = data.reset_index(level='country')
df = df.groupby('continent').resample('10AS').mean()
df = df.gdppc.unstack(level=0)
df.plot()

# GDP per capita using pivot table

df = data.reset_index(level='country')
df = df.groupby('continent').resample('10AS').mean()
df.pivot_table(index='date', columns='continent',
    values='gdppc', aggfunc=np.mean).plot()

# GDP per capita growth using sns

df = data.reset_index(level='country')
df = df.groupby('continent').resample('10AS').mean().reset_index()

g = sns.relplot(x='date', y='gdppc', data=df, hue='continent')
g.set_axis_labels('', 'GDP per capita')
plt.legend(loc='best', title='Hello')

name = os.path.join(fig_dir, 'first')
plt.savefig(name)


# Distribution of GDP per capita

# Try to only keep data from 1800, 1900, 2000 doesn't work for some reason.
data.loc[idx['Switzerland', ['2000', '2010']], :]



sns.catplot(x='year', y='gdppc', hue='oecd', data=centuries)
sns.relplot(x='gdppc', y='life_expectancy', data=centuries, hue='oecd', style='oecd', col='year')
sns.relplot(x='gdppc', y='life_expectancy', data=centuries, hue='oecd', size='population', sizes=(50,500), col='year')

latest = data.loc[(:,'2018'), :].reset_index()
sns.catplot(x='continent', y='gdppc', hue='oecd', data=latest)


#Plots https://www.kaggle.com/subinium/road-to-viz-expert-2-plotly-seaborn
# https://seaborn.pydata.org/tutorial/categorical.html#categorical-tutorial





		

