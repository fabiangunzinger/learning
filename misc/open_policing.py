import os
import pandas as pd
import matplotlib.pyplot as plt


# Directories
code_dir = os.getcwd()
data_dir = os.path.join(code_dir, '../data')

# Load and inspect
file = os.path.join(data_dir, 'ri_statewide_2019_02_25.csv')
ri = pd.read_csv(file, dtype='str')
print(ri.info())
print(ri.isna().sum())

# Rename columns
ri.rename(columns={'subject_sex': 'gender', 
					'reason_for_stop': 'violation', 
					'arrest_made': 'arrested'}, inplace=True)

# Drop unneeded columns
to_drop = ri.filter(regex="contraband")
ri.drop(to_drop, axis='columns', inplace=True)

# Change date formats
ri['arrested'] = ri.arrested == 'TRUE'
ri['search_conducted'] = ri.search_conducted == 'TRUE'

# Drop rows for which department_id is missing
ri.dropna(subset=['department_id', 'date', 'time', 'zone'], inplace=True)

# Create datetime index
combined = ri.date.str.cat(ri.time, sep=' ')
ri['datetime'] = pd.to_datetime(combined)
ri.set_index(ri.datetime, inplace=True)

# Print month of index (can also print day, hour, ect.)
print(ri.datetime.dt.month)			# Works for all date-time variables
print(ri.index.month)				# For index, no need for .dt accessor

# Count observations per month
print(ri.groupby(ri.index.month).gender.count())



# # Inspect column values
# print(ri.outcome.value_counts())
# print(ri.outcome.value_counts(normalize=True))
# print(ri.gender.value_counts(normalize=True))


# # Do outcomes differ by gender?
# female = ri[ri.gender == 'female']
# male = ri[ri.gender == 'male']
# print(female.outcome.value_counts(normalize=True))
# print(male.outcome.value_counts(normalize=True))

# # Does gender affect outcome from speeding?
# f_speed = ri[(ri.gender == 'female') & (ri.violation == 'Speeding')]
# m_speed = ri[(ri.gender == 'male') & (ri.violation == 'Speeding')]
# print(f_speed.outcome.value_counts(normalize=True))
# print(m_speed.outcome.value_counts(normalize=True))

# # Does gender affect who is being searched
# print(ri.search_conducted.mean())
# print(ri.groupby('gender').search_conducted.mean())

# # Does gender affect who is frisked during search?
# ri['frisk'] = ri.reason_for_search.str.contains('Terry Frisk', na=False)
# searched = ri[ri.search_conducted == True]
# print(searched.frisk.mean())
# print(searched.groupby('gender').frisk.mean())

# # Plot hourly arrest rate
# hourly_arrest_rate = ri.groupby(ri.index.hour).arrested.mean()
# hourly_arrest_rate.plot()
# plt.xlabel('Hour or day')
# plt.ylabel('Arrest rate')
# plt.title('Arrest rate by hour of day')
# plt.show()

# monthly = ri[['arrested', 'search_conducted']].resample('h').mean()
# monthly.plot()
# plt.show()

print(ri.columns)

# Plot arrests by zone
# ri.groupby(ri.zone).arrested.count().sort_values().plot(kind='barh')
# plt.show()
# pd.crosstab(ri.zone, ri.arrested).plot(kind='barh', stacked=True)
# plt.show()
