import numpy as np
'''
Из колоды в 52 карты извлекаются случайным образом 4 карты.
a) Найти вероятность того, что все карты – крести.
б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
'''
def comb(k, n):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k))
# a) Карт "крести" всего 52 / 4 = 13
# Количество способов достать все 4 карты "крести":
m = comb(4,13) # 715
# Количество всех способов достать любые 4 карты
n = comb(4,52)
print(f'Ответ к 1а):{np.round(comb(4,13) / comb(4,52), 5)}')
# б) P вытащить 1 туз
p0 = comb(1,4)*comb(3,48) / comb(4,52)
# P вытащить 2 туза
p1 = comb(2,4)*comb(2,48) / comb(4,52)
p2 = comb(3,4)*comb(1,48) / comb(4,52)
p3 = comb(4,4)*comb(0,48) / comb(4,52)
# Найду полную вероятность события "вытащить 4 карты и среди них окажется хотя бы 1 туз"
P = p0 + p1 + p2 + p3
# Либо можно рассмотреть противоположную ситуацию: не вытащить ни одного туза
_P = comb(0,4)*comb(4,48) / comb(4,52)
print(f'Ответ к 1б):{np.round((p0 + p1 + p2 + p3), 5)}, через другой способ:{np.round((1-_P), 5)}')