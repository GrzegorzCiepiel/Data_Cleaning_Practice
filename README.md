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
