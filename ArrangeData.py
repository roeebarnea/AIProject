import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import scipy.stats

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

def series_30_relativity(WWC):
    for i in range(1, 31):
        s_death = 'new_death_' + str(i) + '_day_ago'
        s_cases = 'new_cases_' + str(i) + '_day_ago'
        WWC[s_death] = WWC[s_death] / WWC['Death_STATS_avg']
        WWC[s_cases] = WWC[s_cases] / WWC['Cases_STATS_avg']

def arrange_30_statistic(WWC):
    p = 'population'
    WWC['Cases_STATS_min'] = WWC['Cases_STATS_min']/ 1000000
    WWC['Cases_STATS_max'] = WWC['Cases_STATS_max'] / 1000000
    WWC['Cases_STATS_avg'] = WWC['Cases_STATS_avg'] / 1000000
    WWC['Cases_STATS_percentile_25'] = WWC['Cases_STATS_percentile_25'] / 1000000
    WWC['Cases_STATS_percentile_50'] = WWC['Cases_STATS_percentile_50'] / 1000000
    WWC['Cases_STATS_percentile_75'] = WWC['Cases_STATS_percentile_75'] / 1000000

    WWC['Death_STATS_min'] = WWC['Death_STATS_min'] / 1000000
    WWC['Death_STATS_max'] = WWC['Death_STATS_max'] / 1000000
    WWC['Death_STATS_avg'] = WWC['Death_STATS_avg'] / 1000000
    WWC['Death_STATS_percentile_25'] = WWC['Death_STATS_percentile_25'] / 1000000
    WWC['Death_STATS_percentile_50'] = WWC['Death_STATS_percentile_50'] / 1000000
    WWC['Death_STATS_percentile_75'] = WWC['Death_STATS_percentile_75'] / 1000000

def classify_columns_by_percintles(WWC, num_of_classes):
    part = (100/num_of_classes)/100
    for col in WWC.columns:
        if (col in ['location', 'date']):
            continue
        # DELETE this------------------
        WWC[col][WWC[col] < 0] = 0
        # ------------------------------
        series = pd.Series(WWC[col])
        percentile_val = []
        for i in range(num_of_classes+1):
            percentile_val.append(series.quantile(i*part))

        for i in range(num_of_classes):
            WWC.loc[(WWC[col] >= percentile_val[i]) & (WWC[col] <= percentile_val[i+1]), col] = i




if __name__ == '__main__':

    # WWC = pd.read_csv('WWC_data.csv')
    # WWC = remove_all_nulls(WWC)
    # series_30_relativity(WWC)
    # arrange_30_statistic(WWC)
    # # print(WWC.total_deaths.describe())
    # print('ARRANGE DATA DONE!')

    WWC = pd.read_csv('WWC_data.csv')
    ISR = WWC.loc[WWC['location'] == 'Israel']
    ISR = remove_all_nulls(ISR)
    series_30_relativity(ISR)
    arrange_30_statistic(ISR)
    classify_columns_by_percintles(ISR, 8)
    # print(WWC.total_deaths.describe())
    print('ARRANGE DATA DONE!')