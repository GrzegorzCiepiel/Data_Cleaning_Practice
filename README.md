# Data Cleaning Practice with Python

## Introduction

The task is to clean messy data adn than do some simple analyse.
I this project I use python 3.11 and pandas, glob and matplotlib modules.

## Data cleaning

The data is spread into four separate files. First task is to concate it using glob module:

    files = glob.glob('states*.csv')
    list = []
    for file in files:
      data = pd.read_csv(file)
      list.append(data)
    us_census = pd.concat(list)


Next I had to do preliminary analysis using pandas methods:
+ head()
+ describe()
+ columns()
+ dtypes()
+ info()

I removed '$' sign from values in Income column and changed their dtype to float64 ( numeric )
In GenderPop column I split values in two - one having information about women population and one about men population.
Then I fillup empty values in new "Women" column subtracting Men population form Total population.

Then I was able to plot "Woman income spread"
![Women_income_spread](https://github.com/GrzegorzCiepiel/Data_Cleaning_Practice/assets/135313652/a575f509-8a28-42e2-9de5-db87c361e048)
