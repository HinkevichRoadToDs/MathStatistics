import numpy as np
'''
Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
'''
def comb(k, n):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k))
n = 144
k = 70
p = 0.5
P = comb(k,n) * p**k *(1-p)**(n-k)
print(f'Ответ к 3):{np.round(P, 5)}')
