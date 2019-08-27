# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:38:47 2019

@author: PAT
"""


import os
import sys
from sklearn.datasets import load_iris

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import seaborn  as sb
import matplotlib.pyplot as plt

from pylab import rcParams
rcParams['figure.figsize']=9,8
plt.style.use('seaborn-whitegrid')

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import sklearn
from scipy import stats
from scipy.stats import kurtosis,skew
from pandas.plotting import scatter_matrix

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from scipy.stats import chi2_contingency
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

import plotly.graph_objs as go
import plotly.offline as py

from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import roc_curve,roc_auc_score
from sklearn.linear_model import LogisticRegression

from imblearn.combine import SMOTETomek#combine undersampling and oversampling
from sklearn.ensemble import RandomForestClassifier

