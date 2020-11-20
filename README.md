# Description
Covid-19 data preparation

data source:
https://datacatalog.worldbank.org/dataset/climate-change-knowledge-portal-historical-data

Access date: 16th of November 2020

and:
http://data.worldbank.org

# Requirements
* numpy
* os
* pandas
* datetime
* matplotlib
* world_bank_data

# Final Columns
| Parameter | Description |
| :--- | :--- |
| CountriesAndTerritories | Index - Country name |
| casesPer1000 | cases per 1000 citizens since 1st of September 2020 |
| deathsPer1000 | deaths per 1000 citizens since 1st of September 2020 |
| novemberCasesPercent | percentage of all cases in November |
| novemberDeathsPercent | percentage of all deaths in November |
| casesSinceSeptember | cases since 1st of September 2020 |
| deathsSinceSeptember | deaths since 1st of September 2020 |
| countryterritoryCode | ISO-3166, alpha-3 country code|
| popData2019 | country total population |
| continentExp | continent |
| casesSinceNovember | cases since 1st of November 2020 |
| deathsSinceNovember | deaths since 1st of November 2020 |
| <span>NY.GDP.PCAP.CD</span> | Gross Domestic Product per Capita |
| EN.POP.DNST | Population density |
| SH.MED.BEDS.ZS | Medical beds per 1000 citizens |
| SH.MED.PHYS.ZS | Physicians per 1000 citizens |
| SP.POP.65UP.TO.ZS | percentage of people over 65 |
| SH.STA.TRAF.P5 | traffic incidents casualties per 1000 citizens |
| EN.ATM.PM25.MC.M3 | average PM2.5 polution |