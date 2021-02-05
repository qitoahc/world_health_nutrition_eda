
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv').iloc[:,:-1]
print(df.columns)

x = [ '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968',
       '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
       '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
       '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
       '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
       '2014', '2015']

#fig, ax = plt.subplots()
#ax.scatter(x, df.iloc[9, 4:])
#plt.show()


#print(pd.unique(df['Indicator Name']))
#print('\n\n\n\n')
#print(pd.unique(df['Country Name']))

life_expec = df['Indicator Name'] == 'Life expectancy at birth, total (years)'
print(df[life_expec])

fig, ax = plt.subplots()
for row in df[life_expec].index:
    ax.plot(x, df.iloc[row, 4:])

#ax.scatter(x, df.iloc[9, 4:])
plt.show()
