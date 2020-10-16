import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

N = 500
t = np.linspace(-1.8,1.8,num=N)
# w = 3pi/2

fs = 0.75
ts = -0.25
x3 = 3 * np.cos(2 * math.pi * fs * t + math.pi * ts)
plt.figure(2)
plt.xlabel('t/s')
plt.ylabel('X(t)')
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.plot(t,x3)
plt.title(u'X(t)=Acos(ω*t+φ)')
plt.ylim(-4.0,4.0)
plt.show()