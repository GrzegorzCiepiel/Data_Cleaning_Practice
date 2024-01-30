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


There was 6 columns with diffrent race population in every state: 

['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']

All had numeric values but in "object" data types. Firstly I  fixed empty values and drop duplicates.
Then I plot histograms showing percentage share of every population in states.

![hist_White ](https://github.com/GrzegorzCiepiel/Data_Cleaning_Practice/assets/135313652/766f4624-9a29-4715-b63d-653d553d7637)
![hist_Pacific ](https://github.com/GrzegorzCiepiel/Data_Cleaning_Practice/assets/135313652/24a14da3-e407-4096-a47c-57ee594b01bc)
![hist_Native ](https://github.com/GrzegorzCiepiel/Data_Cleaning_Practice/assets/135313652/62410cc2-20eb-41ee-9c79-2b5749b92fc0)
![hist_Hispanic ](https://github.com/GrzegorzCiepiel/Data_Cleaning_Practice/assets/135313652/823e8dc1-271c-4869-b387-44512159eb24)
![hist_Black ](https://github.com/GrzegorzCiepiel/Data_Cleaning_Practice/assets/135313652/b80f3677-d550-4e7a-828b-2e3fd05384dd)
![hist_Asian ](https://github.com/GrzegorzCiepiel/Data_Cleaning_Practice/assets/135313652/dbc01680-07d1-4b21-b63d-41edfdc9ba82)

I used also pandas melt method to agregate all races in one column.





