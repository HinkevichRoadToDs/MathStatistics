from ex1 import comb
import numpy as np
'''
В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того,
что 2 приобретенных билета окажутся выигрышными?
'''

# 1 ситуация, когда 2 приобретенных билета выигрышные
# всего способов извлечь 2 билета из 100:
n = comb(2,100)
print(f'Ответ к 4:{np.round(1/n, 5)}')
