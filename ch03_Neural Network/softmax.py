import numpy as np


# 오버플로우를 막아주는 c를 설정한 소프트맥스 함수
def softmax(x):
    c = np.max(x)
    temp = np.exp(x-c)
    return temp / np.sum(temp)