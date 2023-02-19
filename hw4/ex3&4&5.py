from scipy import stats
import numpy as np
'''
Непрерывная случайная величина X распределена нормально и задана плотностью распределения
f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
Найдите:
а). M(X)
б). D(X)
в). std(X) (среднее квадратичное отклонение)
'''
print(f"Ответ на 3: M(X) = -2;D(X) = 16; std = 4")

'''
Рост взрослого населения города X имеет нормальное распределение.
Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
а). больше 182 см
б). больше 190 см
в). от 166 см до 190 см
г). от 166 см до 182 см
д). от 158 см до 190 см
е). не выше 150 см или не ниже 190 см
ё). не выше 150 см или не ниже 198 см
ж). ниже 166 см.
'''
print(f'4a:{np.round(1 - stats.norm.cdf(182, loc =174,scale = 8),4)}')
print(f'4b:{np.round(1 - stats.norm.cdf(190, loc =174,scale = 8),4)}')
print(f'4в:{np.round(stats.norm.cdf(190, loc =174,scale = 8) - stats.norm.cdf(166, loc =174,scale = 8),4)}')
print(f'4г:{np.round(stats.norm.cdf(182, loc =174,scale = 8) - stats.norm.cdf(166, loc =174,scale = 8),4)}')
print(f'4д:{np.round(stats.norm.cdf(190, loc =174,scale = 8) - stats.norm.cdf(158, loc =174,scale = 8),4)}')
print(f'4е:{np.round(stats.norm.cdf(150, loc =174,scale = 8) + (1 -stats.norm.cdf(190, loc =174,scale = 8)),4)}')
print(f'4ё:{np.round(stats.norm.cdf(150, loc =174,scale = 8) + (1 -stats.norm.cdf(198, loc =174,scale = 8)),4)}')
print(f'4ж:{np.round(stats.norm.cdf(166, loc =174,scale = 8),4)}')

'''
На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, 
равный 190 см, от математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?
'''
# приведение к стандартному норм. распределению
z_value = (190 - 178)/ 5
print(f'Ответ на 5: наблюдение отклоняется на {z_value} σ')