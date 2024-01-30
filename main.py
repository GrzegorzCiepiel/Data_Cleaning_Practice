import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np
import matplotlib.pyplot as plt
import glob

files = glob.glob('states*.csv')
list = []
for file in files:
    data = pd.read_csv(file)
    list.append(data)
us_census = pd.concat(list)
print(us_census.head())
print(us_census.dtypes)

# INCOME
#us_census.Income = us_census.Income.str.replace('[\$]', '', regex=True)
us_census.Income = us_census.Income.str.lstrip('$')  # found this method easier to use
us_census.Income = pd.to_numeric(us_census.Income)
print(us_census.dtypes)

# GENDER
gender_divide = us_census.GenderPop.str.split('_')
us_census['Men'] = gender_divide.str[0]
us_census['Women'] = gender_divide.str[1]

# us_census['Men'] = us_census['Men'].replace('M', '', regex=True) - the same effect as str.rstrip('M')
us_census['Men'] = us_census['Men'].str.rstrip('M')
us_census['Women'] = us_census['Women'].replace('F', '', regex=True)
us_census['Men'] = pd.to_numeric(us_census['Men'])
us_census['Women'] = pd.to_numeric(us_census['Women'])
#us_census['Women'] = us_census.Women.astype("int64") - tried as an alternative but it doses not work

plt.scatter(us_census['Women'], us_census['Income'], s=25, color="purple")
plt.title('Woman income spread')
plt.xlabel('Woman in million')
plt.ylabel('Income amount')
plt.show()
plt.clf()

us_census['Women'] = us_census['Women'].fillna(us_census['TotalPop'] - us_census['Men'])

plt.scatter(us_census['Women'], us_census['Income'])
plt.title('Woman income spread')
plt.xlabel('Woman in milion')
plt.ylabel('Income amount')
plt.show()
plt.clf()

# RACES
list = ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']
for item in list:
    us_census[item] = us_census[item].replace('[\%]', '', regex=True)
    us_census[item] = pd.to_numeric(us_census[item])
    print(us_census.dtypes)

census = us_census.drop_duplicates(subset=us_census.columns[1:])
census = census.fillna(
    value={'Pacific': 100 - census.Hispanic - census.White - census.Black - census.Native - census.Asian})
print(census)

for race in ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']:
    plt.figure()
    plt.hist(census[race], color='green')
    plt.xlabel("Percentage")
    plt.ylabel("Frequency")
    plt.title("Histogram of the Percentage of {} People per State".format(race))
    plt.savefig(f'hist_{race} .png')
    plt.show()
    plt.clf()

census1 = pd.melt(frame=census, id_vars=['State', 'TotalPop', 'Income', 'Men', 'Women'],
                  value_vars=['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific'], value_name='Percentage',
                  var_name='Race')

alabama_races = ((census1.Race[census1.State == 'Alabama']))
print(alabama_races)
california_races = ((census1.Race[census1.State == 'California']))
alabama_races = alabama_races
print(alabama_races)
print(california_races)