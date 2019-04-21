#coding: utf-8

#import Pandas 
#pip install pandas
import pandas as pd
#Import Numpy
import numpy as np
from math import ceil

populacao = 150
amostra = 15

k = ceil(populacao / amostra)

r = np.random.randint(low = 1, high = k + 1, size = 1)

acumalador = r[0]

sorteados = []

for i in range(amostra):
    print(acumalador)
    sorteados.append(acumalador)
    acumalador += k

#Lendo o iris.csv
base = pd.read_csv('../../Dados/iris.csv')

base_final = base.loc[sorteados]

print(base_final)