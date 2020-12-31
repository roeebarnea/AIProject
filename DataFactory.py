import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def add_more_death(WWC):
    WWC['more_death'] = 0
    countries = WWC['location'].unique()
    for c in countries:
        CON = WWC.loc[WWC['location'] == c]
        dates = CON['date']
        is_first = True
        for d in dates:
            if is_first:
                WWC.loc[(WWC['date'] == d) & (WWC['location'] == c), ['more_death']] =0
                is_first = False
                continue
            death_today = WWC.loc[(WWC['date'] == d) & (WWC['location'] == c), ['new_deaths']]
            death_yesterday = WWC.loc[(WWC['date'] == (d - pd.DateOffset(days=1))) & (WWC['location'] == c), ['new_deaths']]

            if (math.isnan(death_today.iat[0,0])):
                continue
            if (math.isnan(death_yesterday.iat[0,0])):
                continue

            if death_today.iat[0,0] > death_yesterday.iat[0,0] :
                WWC.loc[(WWC['date'] == d) & (WWC['location'] == c), ['more_death']] = 1
            else:
                WWC.loc[(WWC['date'] == d) & (WWC['location'] == c), ['more_death']] = -1

def add_more_new_cases(WWC):
    WWC['more_new_cases'] = 0
    countries = WWC['location'].unique()
    for c in countries:
        CON = WWC.loc[WWC['location'] == c]
        dates = CON['date']
        is_first = True
        for d in dates:
            if is_first:
                WWC.loc[(WWC['date'] == d) & (WWC['location'] == c), ['more_new_cases']] =0
                is_first = False
                continue
            new_cases_today = WWC.loc[(WWC['date'] == d) & (WWC['location'] == c), ['new_cases']]
            new_cases_yesterday = WWC.loc[(WWC['date'] == (d - pd.DateOffset(days=1))) & (WWC['location'] == c), ['new_cases']]

            if (math.isnan(new_cases_today.iat[0,0])):
                continue
            if (math.isnan(new_cases_yesterday.iat[0,0])):
                continue

            if new_cases_today.iat[0,0] > new_cases_yesterday.iat[0,0] :
                WWC.loc[(WWC['date'] == d) & (WWC['location'] == c), ['more_new_cases']] = 1
            else:
                WWC.loc[(WWC['date'] == d) & (WWC['location'] == c), ['more_new_cases']] = -1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    WWC = pd.read_csv('WorldWideCountries-26-12-2020.csv')
    ISR = WWC.loc[WWC['location'] == 'Israel']
    features = WWC.columns
    shape = WWC.shape[0]
    WWC['more_death'] = 0
    WWC['date'] = pd.to_datetime(WWC['date'])
    countries = WWC['location'].unique()
    add_more_death(WWC)
    print('bla')




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
