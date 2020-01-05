
# Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import seaborn as sns
sns.set()
import os



# Aliases
data_dir = '/Users/fabiangunzinger/Library/Mobile Documents/com~apple~CloudDocs/fab/projects/beautiful_data/nyc_airbnb/input/data'


# Load data
file = os.path.join(data_dir, "AB_NYC_2019.csv")
df = pd.read_csv(file)

# Explore data
df.info()
df.neighbourhood.value_counts()


# Set up plot
df_sample = df.sample(n=10000)
plt.figure(1, figsize=(12,6))

# Mercator

m1 = Basemap(projection='merc',
			 llcrnrlat=-60,
			 urcrnlat=65,
			 llcrnrlon=-180,
			 urcrnlon=180,
			 lat_ts=0,
			 resolution='c')

m1.fillcontinents(color='#191919',lake_color='#000000') # dark grey land, black lakes
m1.drawmapboundary(fill_color='#000000')                # black background
m1.drawcountries(linewidth=0.1, color="w")              # thin white line for country borders

# mxy = m1(df_sample['longitude'].tolist(), df_sample['latitude'].tolist())
# m1.scatter(mxy[0], mxy[1], s=3, c="#1292db", lw=0, alpha=1, zorder=5)


# Number of listings

# Average price of listings

# Average number of reviews

