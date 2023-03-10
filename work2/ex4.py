import numpy as np
'''
В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что все мячи белые?
Какова вероятность того, что ровно два мяча белые? Какова вероятность того, что хотя бы один мяч белый?
'''

def comb(k, n):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k))

# P вытащить 2 белых мяча из первого ящика
# вытащить 2 белых мяча из 7, нужно посчитать с помощью сочетаний
P1_all = comb(2,7)/comb(2,10)
# P вытащить 2 белых мяча из второго ящика
# вытащить 2 белых мяча из 9, нужно посчитать с помощью сочетаний
P2_all = comb(2,9)/comb(2,11)
P_all_white = P1_all*P2_all

# следующий вопрос
# две Р ниже это ситуции, когда по одному белому мячу из каждого ящика
P1_1 = comb(1,7)*comb(1,3) / comb(2,10)
P2_1 = comb(1,9)*comb(1,2) / comb(2,11)

# Теперь Р, что из 1ого ящика 2 белых И во втором 0 белых и также со вторым ящиком
P1_all_and_0 = P1_all * (comb(2,2) / comb(2,11))
P2_0_and_all = P2_all * (comb(2,3) / comb(2,10))
P_only_two = P1_all_and_0 + P2_0_and_all + P1_1*P2_1

# третий вопрос
# Р того, что 1 или более мячей белые
P_atleast_1_white = 1 - ((1 / comb(2,10)) * (1 / comb(2,11)))
print(f'Ответ на 4.1:{np.round(P_all_white, 5)}\n'
      f'Ответ на 4.2:{np.round(P_only_two, 5)}\n'
      f'Ответ на 4.3:{np.round(P_atleast_1_white, 5)}')