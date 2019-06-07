# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 00:32:03 2019

@author: Lordd
"""

from sklearn.naive_bayes import GaussianNB
from sklearn import tree,svm
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
import matplotlib as plt

data = pd.read_csv('500_Person_Gender_Height_Weight_Index.csv')
X = data.iloc[:,1:4]
y = data.iloc[:,0:1]

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X , y , test_size = 0.2 , random_state = 0)

clf = GaussianNB()
clf.fit(X_train,y_train)

predictionsnb = pd.DataFrame(np.array(clf.predict(X_test)))
 
from sklearn.metrics import accuracy_score
accuracy_score(y_test,predictionsnb)

clf1 = tree.DecisionTreeClassifier()
clf1.fit(X_train,y_train)

accuracy_score(y_test,clf1.predict(X_test))

clf2 = svm.SVC()
clf2.fit(X_train , y_train)

accuracy_score(y_test,clf2.predict(X_test))

clf3 = Perceptron()
clf3.fit(X_train,y_train)

accuracy_score(y_test,clf3.predict(X_test))

clf4 = KNeighborsClassifier()
clf4.fit(X_train,y_train)

accuracy_score(y_test,clf4.predict(X_test))

