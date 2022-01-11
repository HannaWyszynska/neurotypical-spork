#loading the data file and required software libraries
#please load location of the "heart_data" file as df

import pandas as pd
df = pd.read_csv (r'C:\Users\breno\Desktop\heart.csv')

#exploration of data and division into categorical and numerical data

df.describe()

#calculation of correlation
#import seaborn to present correlation as a heat map 
#and as a scatter matrix (from pandas)
df.corr()
corr=df.corr()
print(corr)

import seaborn as sns
cmap = sns.color_palette("vlag", as_cmap=True)
sns.heatmap(corr, vmin=-1.0, vmax=1.0, square=True, cmap=cmap)

from pandas.plotting import scatter_matrix
a = scatter_matrix(df, figsize=(16, 16))

#creation of data frame filters needed for further data analysis

female_filter = df["sex"] == 0
male_filter = df["sex"] == 1

#initial visualisation of results and differences between sexes

sns.scatterplot(data=df[female_filter], x="age", y="trestbps", hue="ca", style = "cp")

sns.scatterplot(data=df[male_filter], x="age", y="trestbps", hue="ca", style = "cp")

#analysis of linear models between age and resting blod pressure divided into different types of chest pain and sex

sns.set_theme(style="darkgrid", palette ="mako")

f = sns.lmplot(data=df[female_filter], x="age", y="thalach", hue="cp",col = "cp", col_wrap=2, height=3)

m = sns.lmplot(data=df[male_filter], x="age", y="thalach", hue="cp",col = "cp", col_wrap=2, height=3)

#analysis of linear models between age and resting blod pressure divided into different types of chest pain, number of blocked arteries and sex

sns.lmplot(data=df, x="age", y="trestbps", hue="sex", row="cp", col = "ca")

#histograms of cholesterol and resting blood pressure levels based on the sex

sns.displot(data=df, x="chol", hue = "sex", stat="density", common_norm=False)

sns.displot(data=df, x="trestbps", hue = "sex", stat="density", common_norm=False)

#linear regression model of the dependency of resting blood pressure based on age, with training and test data

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

heart_X = df[["age"]]
heart_Y = df[["trestbps"]]

#training set was set to 15% of the data available

train_X, test_X, train_y, test_y = train_test_split(heart_X, heart_Y, random_state=46)

regr = linear_model.LinearRegression()
regr.fit(train_X, train_y)

heart_y_pred = regr.predict(test_X)

#ploting of the data

fig, ax = plt.subplots()

ax.scatter(train_X, train_y, color="yellow", marker="o", label="train")
ax.plot(test_X, heart_y_pred, color="green", linewidth=3, label="test")
ax.legend()

#calculation of the characteristics of the model set to 2 decimal points

print("Model gradient: %.2f" % regr.coef_[0])
print("Model intercept: %.2f" % regr.intercept_)
print("Model score: %.2f" % regr.score(test_X, test_y))
print("Mean squared error: %.2f" % mean_squared_error(test_y, heart_y_pred))
print("Coefficient of determination: %.2f" % r2_score(test_y, heart_y_pred))

#linear regression model of the dependency between cholesterol levels in plasma and resting heart rate, with training and test data

chol_X = df[["chol"]]
chol_Y = df[["trestbps"]]

train_X_c, test_X_c, train_Y_c, test_Y_c = train_test_split(chol_X, chol_Y, random_state=46)

regr_c = linear_model.LinearRegression()
regr_c.fit(train_X_c, train_Y_c)

chol_y_pred = regr_c.predict(test_X_c)

fig, ax = plt.subplots()

ax.scatter(train_X_c, train_Y_c, color="green", marker="x", label="train")
ax.plot(test_X_c, chol_y_pred, color="black", linewidth=2, label="test")
ax.legend()

print("Model gradient: %.2f" % regr_c.coef_[0])
print("Model intercept: %.2f" % regr_c.intercept_)
print("Model score: %.2f" % regr_c.score(test_X, test_y))
print("Mean squared error: %.2f" % mean_squared_error(test_y, heart_y_pred))
print("Coefficient of determination: %.2f" % r2_score(test_y, heart_y_pred))

