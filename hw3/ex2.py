import numpy as np
'''
В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей,
из которых 5 белых. Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. 
Какова вероятность того, что 3 мяча белые?
'''
def comb(k, n):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k))
'''
Б   НеБ     Б   НеБ
0    2      3    1
1    1      2    2
2    0      1    3
'''
PA = comb(0,5)*comb(2,3) / comb(2,8) * comb(3,5)* comb(1,7) / comb(4,12)
PB = comb(1,5)*comb(1,3) / comb(2,8) * comb(2,5)* comb(2,7) / comb(4,12)
PC = comb(2,5)*comb(0,3) / comb(2,8) * comb(1,5)* comb(3,7) / comb(4,12)
print(f'Ответ к 2: {np.round(PA+PB+PC,5)}')