# Import Numpy
import numpy as np
from scipy import stats

jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]

print('Media: {media}'.format(media=np.mean(jogadores)))

print('Moda: {moda}'.format(moda=np.median(jogadores)))

quartis = np.quantile(jogadores, [0, 0.25, 0.5, 0.75, 1])

print('Quartil 25%: {quart1} \nQuartil 50%: {quart2} \nQuartil 75%: {quart3} \nQuartil 100%: {quart4}'.format(
    quart1=quartis[0], quart2=quartis[1], quart3=quartis[2], quart4=quartis[3],))

print('Desvio Padrao {desvio}'.format(desvio = np.std(jogadores, ddof = 1)))

print(stats.describe(jogadores))