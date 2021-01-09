import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import scipy.stats
from numbers import Number

def remove_all_nulls(WWC):
    WWC.drop(['iso_code', 'continent', 'total_cases', 'total_deaths', 'new_deaths_smoothed',
              'new_cases_smoothed_per_million', 'new_deaths_smoothed_per_million', 'icu_patients',
              'icu_patients_per_million', 'hosp_patients', 'hosp_patients_per_million', 'hosp_patients',
              'hosp_patients_per_million', 'weekly_icu_admissions', 'weekly_icu_admissions_per_million',
              'weekly_hosp_admissions', 'weekly_hosp_admissions_per_million', 'new_tests', 'total_tests',
              'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units', 'total_vaccinations',
              'total_vaccinations_per_hundred', 'aged_65_older', 'aged_70_older',
              'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers', 'male_smokers',
              'handwashing_facilities'], axis=1, inplace=True)

    return (WWC.dropna())

def change_negative_to_zero(WWC):
    num = WWC._get_numeric_data()
    num[num < 0] = 0

def change_negative_to_zero2(WWC):
    for col in WWC.columns:
        if (col in ['location', 'date']):
            continue
        WWC[col][WWC[col] < 0] = 0


if __name__ == '__main__':
    WWC = pd.read_csv('WorldWideCountries-26-12-2020.csv')
    remove_all_nulls(WWC)
    change_negative_to_zero2(WWC)


    WWC.to_csv('WWC_clean.csv')
