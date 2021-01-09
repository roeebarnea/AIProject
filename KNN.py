import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import scipy.stats



if __name__ == '__main__':

    WWC = pd.read_csv('WWC_data.csv')
    # print(WWC.info())
    col = WWC.columns
    print(col)
    print(WWC.head)
    # print( WWC.describe())
    WWC.drop(['iso_code', 'continent', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'new_deaths_smoothed',
              'new_cases_smoothed_per_million', 'new_deaths_smoothed_per_million', 'icu_patients',
              'icu_patients_per_million', 'hosp_patients', 'hosp_patients_per_million', 'hosp_patients',
              'hosp_patients_per_million', 'weekly_icu_admissions', 'weekly_icu_admissions_per_million',
              'weekly_hosp_admissions', 'weekly_hosp_admissions_per_million', 'new_tests', 'total_tests',
              'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units', 'total_vaccinations',
              'total_vaccinations_per_hundred', 'population', 'aged_65_older', 'aged_70_older',
              'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers', 'male_smokers',
              'handwashing_facilities'], axis=1, inplace=True)

    WWC = WWC.dropna()

    # print(WWC.total_deaths.describe())
    print('bla')