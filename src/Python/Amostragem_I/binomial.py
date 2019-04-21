#coding: utf-8

from scipy.stats import binom

print('jogar um moeda 5 vezes, qual a probabilidade de dar cara 3 vezes? \n{prop}\n'.format(
    prop=binom.pmf(3, 5, 0.5)))

print('Passar por 4 sinais de 4 tempos, qual a probabilidade de pegar sinal verde?\n' +
      'Nenhuma:  {prop_1}\n1: {prop_2}\n2: {prop_3}\n3: {prop_4}\n4: {prop_5}\n'.format(
          prop_1=binom.pmf(0, 4, 0.25),
          prop_2=binom.pmf(1, 4, 0.25),
          prop_3=binom.pmf(2, 4, 0.25),
          prop_4=binom.pmf(3, 4, 0.25),
          prop_5=binom.pmf(4, 4, 0.25),
      ))

print('E se forem sinais de dois tempos?\n' +
      'Nenhuma:  {prop_1}\n1: {prop_2}\n2: {prop_3}\n3: {prop_4}\n4: {prop_5}\n'.format(
          prop_1=binom.pmf(0, 4, 0.5),
          prop_2=binom.pmf(1, 4, 0.5),
          prop_3=binom.pmf(2, 4, 0.5),
          prop_4=binom.pmf(3, 4, 0.5),
          prop_5=binom.pmf(4, 4, 0.5),
      ))

print('Probabilidade acumulativa.\n{prop}\n'.format(prop=binom.cdf(4, 4, 0.5)))

print('Concurso com 12 questões, qual a probabilidade de acertar 7 questões considerando que cada questão tem 4 alternativas?\n{prop}'
      .format(prop=binom.pmf(7, 12, 0.25)))
