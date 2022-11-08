# -*- coding: utf-8 -*-
"""Machine Learning w praktyce - problemy regresji w uczeniu nadzorowanym - 07.11.2022.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_iU4MY6zTFjvWrcax6IfsHOyGJZUZNJI
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score, mean_absolute_percentage_error, mean_squared_error
from numpy.lib.function_base import average
import statsmodels.api as sm
import numpy as np
from sklearn.model_selection import cross_val_score

df=pd.read_csv('kc_house_data.csv')

pd.set_option('display.max_columns', None)

df.head()

df.info()

df.describe()

u=df['bedrooms'].unique()

u.sort()

u

plt.figure(figsize=(16,12))
sns.lmplot(x='bedrooms', y='price', data=df)

plt.figure(figsize=(16,12))
sns.boxplot(x='bedrooms', y='price', data=df)

#liczenie korelacji między zmiennymi
count_corr=df.corr()

#heatmapa
sns.heatmap(count_corr)

plt.figure(figsize=(16,12))
sns.lmplot(x='sqft_living15', y='price', data=df)

plt.figure(figsize=(16,12))
sns.boxplot(x='sqft_living15', y='price', data=df)

fig, ax=plt.subplots(figsize=(12,6)) #figsize-definiujemy rozmiar wykresu
ax.plot(df.index, df['price'], label='price')
ax.plot(df.index, df['sqft_living15'], label='sqft_living15')

#podpis osi x
ax.set_xlabel('Metraż')
#podpis osi y
ax.set_ylabel('Cena')
#tytuł wykresu
ax.set_title('Korelacja')
#obrót etykiet na osi x
ax.xaxis.set_tick_params(rotation=90)
#obrót etykiet na osi y
ax.yaxis.set_tick_params(rotation=90)
#legenda
ax.legend()
plt.show()

