#coding: utf-8

#import Pandas 
#pip install pandas
import pandas as pd
#Import Numpy
import numpy as np

#Lendo o iris.csv
base = pd.read_csv('../../Dados/iris.csv')

#Imprimindo a quantidade de linhas e a contidade de colunas no arquivo
print('Tolal de linhas: {linhas} \nTotal de colunas: {colunas}'.format(linhas = str(base.shape[0]), colunas =  str(base.shape[1])))

#Gerando os numeros aleatorios para gerar a amostra
amostra = np.random.choice(a = [0, 1], size = 150, replace = True, p = [0.5, 0.5])

print('Contidade total da variavel amostra: {total}'.format(total = len(amostra)))

print('Contidade total de 1 na variavel amostra: {total}'.format(total = len(amostra[amostra == 1])))

print('Contidade total de 0 na variavel amostra: {total}'.format(total = len(amostra[amostra == 0])))
