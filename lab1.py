#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import os
import pandas
import datetime
import matplotlib.pyplot as plt
import world_bank_data as wb


# In[2]:


df1 = pandas.read_excel('./COVID-19-geographic-disbtribution-worldwide.xlsx')


# In[3]:


aggregation_functions = {
    'cases': 'sum',
    'deaths': 'sum',
    'countryterritoryCode': 'first',
    'popData2019': 'first',
    'continentExp': 'first',
}

df_new = df1.copy()
#df_new.drop(df_new[(df_new.month < 11) | (df_new.year < 2020)].index, inplace=True)
df_new.drop(df_new[df_new.dateRep < '2020-09-01'].index, inplace=True)
df_new = df_new.groupby(['countriesAndTerritories']).aggregate(aggregation_functions)

df_november = df1.copy()
df_november.drop(df_november[df_november.dateRep < '2020-11-01'].index, inplace=True)
df_november = df_november.groupby(['countriesAndTerritories']).aggregate({
    'cases': 'sum',
    'deaths': 'sum'})


# In[4]:


# calculate cases / deaths for population
df_new['casesSinceNovember'] = df_november['cases']
df_new['deathsSinceNovember'] = df_november['deaths']
df_new['casesPer1000'] = df_new['cases'] / df_new['popData2019'] * 1000
df_new['deathsPer1000'] = df_new['deaths'] / df_new['popData2019'] * 1000
df_new['NovemberCasesPercent'] = df_new['casesSinceNovember'] / df_new['cases']
df_new['NovemberDeathsPercent'] = df_new['deathsSinceNovember'] / df_new['deaths']


# In[5]:


# simple cases/ deaths plot
# df_new[['casesPer1000', 'deathsPer1000']].plot(figsize=(20,10))


# In[6]:


# rearange columns
cols = df_new.columns.tolist()
cols = cols[-4:] + cols[:-4]
df_new = df_new[cols]

# rename columns
df_new.rename(columns={"cases": "casesSinceSeptember", "deaths": "deathsSinceSeptember"}, inplace=True)


# In[7]:


def get_wbd_by_indicator(indicator: str, mvr_value=20):
    new_wbd_data = pandas.DataFrame(wb.get_series(indicator, mrv=mvr_value, id_or_value='id', simplify_index=True))
    new_wbd_data = new_wbd_data.groupby(['Country']).aggregate({indicator: 'last'})
    return new_wbd_data

# fetch new data from api.world.bank.data
df_gdp_pcap = get_wbd_by_indicator('NY.GDP.PCAP.CD')
df_pop_dnst = get_wbd_by_indicator('EN.POP.DNST')
df_med_beds = get_wbd_by_indicator('SH.MED.BEDS.ZS')
df_med_phys = get_wbd_by_indicator('SH.MED.PHYS.ZS')
df_pop_65up = get_wbd_by_indicator('SP.POP.65UP.TO.ZS')
df_sta_traf = get_wbd_by_indicator('SH.STA.TRAF.P5')
df_atm_pm25 = get_wbd_by_indicator('EN.ATM.PM25.MC.M3')


# In[8]:


# join new data to DataFrame
df_new = df_new.join(df_gdp_pcap, how='left', on='countryterritoryCode')
df_new = df_new.join(df_pop_dnst, how='left', on='countryterritoryCode')
df_new = df_new.join(df_med_beds, how='left', on='countryterritoryCode')
df_new = df_new.join(df_med_phys, how='left', on='countryterritoryCode')
df_new = df_new.join(df_pop_65up, how='left', on='countryterritoryCode')
df_new = df_new.join(df_sta_traf, how='left', on='countryterritoryCode')
df_new = df_new.join(df_atm_pm25, how='left', on='countryterritoryCode')


# In[9]:


# clear empty data with NaN
df_new['casesPer1000'].replace(0, numpy.nan, inplace=True)
df_new['deathsPer1000'].replace(0, numpy.nan, inplace=True)
df_new['NovemberCasesPercent'].replace(0, numpy.nan, inplace=True)
df_new['NovemberDeathsPercent'].replace(0, numpy.nan, inplace=True)


# In[10]:


df_new


# In[11]:


df_new.to_csv(r'./crunched_data.csv')

