'''
x1과 x2라는 입력을 받아서 linear Classification을 통해서
만약 값이 0.7보다 크면 1을 아니면 0을 출력하는 모델을 만들었습니다.
'''

def AND(x1, x2) :
    w1, w2, theta = 0.5,0.5,0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <=theta:
        return 0
    else:
        return 1