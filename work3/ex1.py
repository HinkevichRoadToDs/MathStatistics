import numpy as np
'''
Даны значения зарплат из выборки выпускников:
100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
Посчитать (желательно без использования статистических методов наподобие std, var, mean)
среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.
'''
X = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
n = X.shape[0]
mean = X.sum() / n
var_ddof0 = ((X - mean)**2).sum() / n
var_ddof1 = ((X - mean)**2).sum() / (n-1)
std_ddof1 = np.math.sqrt(var_ddof1)
print(f'Ответ: mean = {mean},\n'
      f'дисперсия смещенная:{var_ddof0},\n'
      f'дисперсия несмещенная:{var_ddof1},\n'
      f'СКО несмещенное:{std_ddof1}')