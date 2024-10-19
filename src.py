import numpy as np


def vect_to_state(vect: list):
    if vect[0] > vect[1]:
        return 0
    else:
        return 1


def get_forecast(stream: list, q1: list, q2: list, lam1: float, lam2: float):
    x1 = stream[len(stream) - 1]
    x2 = stream[len(stream) - 2]
    if x1 == 0:
        X1_ = [1, 0]
    else:
        X1_ = [0, 1]
    if x2 == 0:
        X2_ = [1, 0]
    else:
        X2_ = [0, 1]

    _xn = [((Q1[0][0] * X1_[0]) + (Q1[0][1] * X1_[1])) * lam1, ((Q1[1][0] * X1_[0]) + (Q1[1][1] * X1_[1])) * lam1]
    __xn = [((Q2[0][0] * X2_[0]) + (Q2[0][1] * X2_[1])) * lam2, ((Q2[1][0] * X2_[0]) + (Q2[1][1] * X2_[1])) * lam2]

    forecast = [_xn[0] + __xn[0], _xn[1] + __xn[1]]

    return forecast


stream = [0] * 200

stream[100] = stream[105] = 1
stream[110] = stream[115] = 1
stream[120] = stream[125] = 1
stream[130] = stream[135] = 1
stream[140] = stream[141] = stream[142] = 1
stream[150] = stream[155] = 1

stream = 2 * stream

F1 = {'0-0': 0, '0-1': 0, '1-0': 0, '1-1': 0}
F2 = {'0-0': 0, '0-1': 0, '1-0': 0, '1-1': 0}

for i in range(0, len(stream) - 1):
    if stream[i] == 0 and stream[i + 1] == 0:
        F1['0-0'] = F1['0-0'] + 1
    if stream[i] == 0 and stream[i + 1] == 1:
        F1['0-1'] = F1['0-1'] + 1
    if stream[i] == 1 and stream[i + 1] == 1:
        F1['1-1'] = F1['1-1'] + 1
    if stream[i] == 1 and stream[i + 1] == 0:
        F1['1-0'] = F1['1-0'] + 1

for i in range(0, len(stream) - 2, 2):
    if stream[i] == 0 and stream[i + 2] == 0:
        F2['0-0'] = F2['0-0'] + 1
    if stream[i] == 0 and stream[i + 2] == 1:
        F2['0-1'] = F2['0-1'] + 1
    if stream[i] == 1 and stream[i + 2] == 1:
        F2['1-1'] = F2['1-1'] + 1
    if stream[i] == 1 and stream[i + 2] == 0:
        F2['1-0'] = F2['1-0'] + 1

for i in range(1, len(stream) - 2, 2):
    if stream[i] == 0 and stream[i + 2] == 0:
        F2['0-0'] = F2['0-0'] + 1
    if stream[i] == 0 and stream[i + 2] == 1:
        F2['0-1'] = F2['0-1'] + 1
    if stream[i] == 1 and stream[i + 2] == 1:
        F2['1-1'] = F2['1-1'] + 1
    if stream[i] == 1 and stream[i + 2] == 0:
        F2['1-0'] = F2['1-0'] + 1

FreqMatrix1 = [[F1['0-0'], F1['0-1']], [F1['1-0'], F1['1-1']]]
FreqMatrix2 = [[F2['0-0'], F2['0-1']], [F2['1-0'], F2['1-1']]]

totalF1col1 = F1['0-0'] + F1['1-0']
totalF1col2 = F1['0-1'] + F1['1-1']

totalF2col1 = F2['0-0'] + F2['1-0']
totalF2col2 = F2['0-1'] + F2['1-1']

Q1 = [[round(F1['0-0'] / totalF1col1, 2), round(F1['0-1'] / totalF1col2, 2)],
      [round(F1['1-0'] / totalF1col1, 2), round(F1['1-1'] / totalF1col2, 2)]]

Q2 = [[round(F2['0-0'] / totalF2col1, 2), round(F2['0-1'] / totalF2col2, 2)],
      [round(F2['1-0'] / totalF2col1, 2), round(F2['1-1'] / totalF2col2, 2)]]

count0 = 0
count1 = 0

for i in range(0, len(stream)):
    if stream[i] == 0:
        count0 = count0 + 1
    if stream[i] == 1:
        count1 = count1 + 1

X_ = [count0 / len(stream), count1 / len(stream)]

Q1_X = [(Q1[0][0] * X_[0]) + (Q1[0][1] * X_[1]), (Q1[1][0] * X_[0]) + (Q1[1][1] * X_[1])]

Q2_X = [(Q2[0][0] * X_[0]) + (Q2[0][1] * X_[1]), (Q2[1][0] * X_[0]) + (Q2[1][1] * X_[1])]

lam1 = round(0.813, 3)
lam2 = round(0.187, 3)

print(Q1)
print(Q2)

print(get_forecast(stream, Q1, Q2, lam1, lam2))
print(vect_to_state(get_forecast(stream, Q1, Q2, lam1, lam2)))
