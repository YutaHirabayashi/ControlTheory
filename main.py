import numpy as np
import matplotlib.pyplot as plt

TIME_UNIT = 1 #s

K = 0.5
T = 10
def first_order_system(u, K, T, y_pre):
    '''u:入力[t]、y_pre:出力[t-1]、K:ゲイン、T:時定数'''
    y = (K*TIME_UNIT*u + T*y_pre)/(T + TIME_UNIT)
    return y

Kp = 0
Kd = 0
Ki = 0.05
def pid_system(e, e_diff, e_sum, Kp, Kd, Ki):
    y = Kp*e + Kd*e_diff + Ki * e_sum
    return y


def main():

    #step input
    u_array = np.array([1 if i > 20 else 0 for i in range(0, 100)])
    
    y_array = []
    y = 0 #initialize
    e = 0
    e_sum = 0
    for u in u_array:
        #pid
        e_pre = e
        e = u - y
        e_diff = e - e_pre
        e_sum += e
        m = pid_system(e, e_diff, e_sum, Kp, Kd, Ki)
        
        #1次遅れ
        y = first_order_system(m, K, T, y)
        y_array.append(y)

    plt.plot(y_array)
    
    plt.plot(np.full(100, 1))
    plt.savefig("Kp_{}_Kd_{}_Ki_{}.png".format(Kp, Kd, Ki))

    return


if __name__ == "__main__":
    main()
    pass