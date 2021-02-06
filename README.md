# DISTILLING WORLD HEALTH TRENDS
![alt text](https://case.edu/medicine/globalhealth/sites/case.edu.cghd/files/styles/hero_one_column/public/2019-02/app-world-map.jpg?h=dabe408c&itok=xVpTbRrf)
## Goal:
Our goal was to explore data on life expectancy collected over a series of years, from over 250 countries, and compare and contrast that data by each country's respective public health indicators of which each country shared 345 features such as  by gender and age.
```bash
'Adults (ages 15+) living with HIV'
'Age at first marriage, female'
'Wanted fertility rate (births per woman)'
```
## The Problem
Our problem was to devise an appropriate approach to viewing our data. We were interested in understanding how life life expectancy varied across different countries and also throughout the years present.  Our initial approach involved identifying countries that had the greatest standard deviation, highest mean, lowest mean, and greatest range over the time span.  We wanted to know what kinds of other factors led to or correlated with the life expectancies for those countries.

## Data
Upon initial inspection of the raw data we ascertained that the data fell intersected along three distinct domains:
* Chronological: Spanning the years 1960 through 2015
* Geographical: Incorporating 258 countries that have existed within the above.
* Public Health Factors: Split into 345 subcategories of public health for _each_ country or geopolitical region.
## Analysis
Although we were initially tempted to clean the data and run it through a pd.corr() method or muliplot we decided instead to continue to explore the data by comparing countries and finding significant inidicators.  The indicators we chose were:
standard deviation 
highest mean
lowest mean
greatest range
We believed that these metrics would show us what factors are the most important for changing life expectancy in a country.  
Cambodia - The data showed us an anomaly 
Since there were so many indicators, we decided to reformat the data with key as country name, value as public health feature.
We were also interested in looking at these countires by regions, and we notivced that some country names were grouped by region, or even economic brakcket.
With the amount of data in this file 
Some features we were interested in but did not have time to persue further analysis of included:
- The mean high of life expectancies.
### Model
The model we chose 
### Conclusions
Some obervations:
- There are countries whose data, either completely or for paticular years, as an aggregate of a geographic region or particular designation i.e. 'Arab Countries' and 'IDA & IBRD countries'.

![alt text](https://raw.githubusercontent.com/qitoahc/world_health_nutrition_eda/main/images/Highest_mean.png)
![alt text](https://github.com/qitoahc/world_health_nutrition_eda/blob/main/images/All_countries.png)
