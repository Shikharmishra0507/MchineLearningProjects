# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1in0n9EoGC1H7RleQQw2JWkt7yyuyLCQ9
"""

import pandas as pd
import numpy as np

df=pd.read_csv("train.csv")
df2=pd.read_csv("test.csv")
df.replace(to_replace=['LF'],value='Low Fat')

"""imputing missing datas"""

input=df.drop(['Item_Outlet_Sales'],axis='columns')

#input=input.drop(['Item_Identifier'],axis='columns')
input['Outlet_Size'].fillna(method='bfill',inplace=True)
input['Item_Weight']=input['Item_Weight'].fillna(input['Item_Weight'].mean())

print(input['Outlet_Identifier'].nunique())
print(input['Outlet_Type'].nunique())
print(input['Item_Type'].nunique())

"""one hot encoidng and label encoding"""

from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
le1=LabelEncoder()
le2=LabelEncoder()
le3=LabelEncoder()
le4=LabelEncoder()
le5=LabelEncoder()
le6=LabelEncoder()
le7=LabelEncoder()
input['Item_Identifier']=le7.fit_transform(input['Item_Identifier'])
input['Item_Fat_Content']=le1.fit_transform(input['Item_Fat_Content'])
input['Outlet_Location_Type']=le2.fit_transform(input['Outlet_Location_Type'])
input['Outlet_Size']=le3.fit_transform(input['Outlet_Size'])
input['Outlet_Identifier']=le4.fit_transform(input['Outlet_Identifier'])
input['Outlet_Type']=le5.fit_transform(input['Outlet_Type'])
input['Item_Type']=le6.fit_transform(input['Item_Type'])
ct=make_column_transformer((OneHotEncoder(),['Item_Type','Outlet_Identifier']),remainder='passthrough')
input=ct.fit_transform(input)

input.shape

type(input)

#lip=input
lip=pd.DataFrame(input)
lip.shape

X=lip.iloc[ : , : ].values
y=df['Item_Outlet_Sales'].values
X.shape

from  sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

X.shape

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
regF=RandomForestRegressor(n_estimators=10)
regF.fit(X_train,y_train)
y_pred=regF.predict(X_test)
print(r2_score(y_test,y_pred))

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
regD=DecisionTreeRegressor(random_state=0)
regD.fit(X_train,y_train)
y_pred=regD.predict(X_test)
print(r2_score(y_test,y_pred))

#from sklearn.svm import SVR
#from sklearn.metrics import r2_score
#reg=SVR(kernel='rbf')
#reg.fit(X_train,y_train)
#y_pred=reg.predict(X_test)
#print(r2_score(y_test,y_pred))
#-ve

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
linreg=LinearRegression()
linreg.fit(X_train,y_train)
y_pred=linreg.predict(X_test)
print(r2_score(y_test,y_pred))
#56%