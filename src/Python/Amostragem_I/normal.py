#coding: utf-8

from scipy.stats import norm

print('Conjunto de objetos em uma cesta, a média é 8 quilos e o devio padrão é 2.\n' +
      'Qual a probabilidade de tirar um objeto que o peso é menor que 6 quilos: \n{prop}\n'
      .format(prop=norm.cdf(6, 8, 2)))

print('Qual a probabilidade de tirar um objeto que o peso é maior que 6 quilos: \n{prop}\n'
     .format(prop=norm.sf(6, 8, 2)))

print('Qual a probabilidade de tirar um objeto que o peso é menor que 6 quilos eou maior que 10 quilos: \n{prop}\n'
     .format(prop = (norm.cdf(6, 8, 2) + norm.sf(10, 8, 2))))

print('Qual a probabilidade de tirar um objeto que o peso é menor que 10 quilos eou maior que 8 quilos: \n{prop}\n'
     .format(prop=(norm.cdf(10, 8, 2) + norm.sf(8, 8, 2))))
