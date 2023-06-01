import numpy as np
from sigmoid_function import sigmoid

# 입력층에서 1층으로의 신호전달
X = np.array([1.0, 0.5]) # 입력
W1 = np.array([[0.1, 0.3, 0.5],
               [0.2, 0.4, 0.6]]) # 가중치 매트릭스
B1 = np.array([0.1, 0.2, 0.3]) # 편향

A1 = np.dot(X, W1) + B1 # 1층에 해당하는 출력값

Z1 = sigmoid(A1)


# 1층에서 2층으로 신호 전달하기

W2 = np.array([[0.1, 0.4],
               [0.2, 0.5],
               [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

# 2층에서 출력층으로의 신호 전달


def identity_func(x):
    return x


W3 = np.array([[0.1, 0.3],
               [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3) + B3
Y = identity_func(A3)


