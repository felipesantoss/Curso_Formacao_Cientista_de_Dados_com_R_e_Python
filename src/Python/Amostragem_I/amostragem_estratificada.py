#coding: utf-8

#import Pandas 
#pip install pandas
import pandas as pd
#import Sklearn 
#pip install -U scikit-learn scipy matplotlib
from sklearn.model_selection import train_test_split
#Import Numpy
import numpy as np

#Lendo o iris.csv
base = pd.read_csv('../../Dados/iris.csv')

#Imprimindo a quantidade de linhas e a contidade de colunas no arquivo
print('Tolal de linhas: {linhas} Total de colunas: {colunas}'.format(linhas = str(base.shape[0]), colunas =  str(base.shape[1])))

print('Contador de elementos agrupados por Class:\n{totalClass}'.format(totalClass = base['class'].value_counts()))

x, _, y, _ = train_test_split(base.iloc[:,0:4], base.iloc[:, 4], test_size = 0.5, stratify = base.iloc[:, 4])

print('Total das amostras estatificadas:\n{totalEstatificada}'.format(totalEstatificada = y.value_counts()))


#Lendo o iris.csv
base_infert = pd.read_csv('../../Dados/infert.csv')

print('Contador de elementos agrupados por Education :\n{totalEducation}'.format(totalEducation = base_infert['education'].value_counts()))

x1, _, y1, _ = train_test_split(base_infert.iloc[:, 2:9], base_infert.iloc[:, 1], test_size = 0.6, stratify = base_infert.iloc[:, 1])

print('Total das amostras estatificadas:\n{totalEstatificada}'.format(totalEstatificada = y1.value_counts()))