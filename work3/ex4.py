import numpy as np
'''
В университет на факультеты A и B поступило равное количество студентов, 
а на факультет C студентов поступило столько же, сколько на A и B вместе. 
Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
Для студента факультета B эта вероятность равна 0.7, а для студента 
факультета C - 0.9.Студент сдал первую сессию. Какова вероятность, 
что он учится: a). на факультете A б). на факультете B в). на факультете C?
'''

# P студент из факультета А - 0.25, такая же Р, что из В
# P студент из факультета C - 0.5
# событие А - студент сдал сессию,оно зависит от того, какое из В событий произойдет,
# события В1,В2,В3 - факультеты соответственно

# a) P(В1|A) = P(B1) * P(A|B1) / P(A)
# Полная вероятность - какова вероятность, что взятый студент сдаст сессию?
P_A = 0.25 * 0.8 + 0.25 * 0.7 + 0.5 * 0.9
P_B1A = 0.25 * 0.8 / P_A
# b)
P_B2A = 0.25 * 0.7 / P_A
# c)
P_B3A = 0.5 * 0.9 / P_A
print(f'Ответ на 4: a){np.round(P_B1A,5)},b){np.round(P_B2A,5)},c){np.round(P_B3A,5)}')