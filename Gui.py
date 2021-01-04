from tkinter import *


def hanshu1():
    import numpy as np
    import matplotlib.pyplot as plt

    def I2(n):
        return np.power(-2,n)

    n2 = np.arange(-5.0, 5.0, 1)

    plt.subplot(111)      # 2 rows, 3 column, 4plot
    plt.stem(n2, I2(n2), 'g-')
    #设置坐标轴范围
    plt.xlim((-6, 8))   
    plt.ylim((-10,10))
    #设置坐标轴名称
    plt.xlabel('n')
    plt.ylabel('X[n]')
    #设置坐标轴刻度
    ax = plt.gca()                                            # get current axis 获得坐标轴对象
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
    ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
    ax.spines['left'].set_position(('data', 0))
    plt.title(r"$Functional Equation:ω=0,r=-2,X[n]=(-2)^n$")
    plt.show()

def hanshu2():
    import numpy as np
    import matplotlib.pyplot as plt

    def y2(n):
        return np.power(-1/2,n)


    t3 = np.arange(-50, 50, 1)


    plt.subplot(111)      # 2 rows, 3 column, 5plot
    plt.stem(t3, y2(t3), 'g-')
    #设置坐标轴范围
    plt.xlim((-6, 8))
    plt.ylim((-10, 10))
    #设置坐标轴名称
    plt.xlabel('n')
    plt.ylabel('X[n]')
    #设置坐标轴刻度
    ax = plt.gca()                                            # get current axis 获得坐标轴对象
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
    ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
    ax.spines['left'].set_position(('data', 0))
    plt.title(r"$Functional Equation:ω=0,r=-\frac{1}{2},X[n]=(-\frac{1}{2})^n$")
    plt.show()

def hanshu3():
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

def hanshu4():
    import numpy as np
    import matplotlib.pyplot as plt
    plt.cla()


    def f(t):
        return np.exp(-t)

    t1 = np.arange(-5.0, 5.0, 1)


    plt.stem(t1, f(t1), '-b',label='X(t)=e^-t')
   
    plt.legend(loc='best')

    plt.xlim((-5, 5))
    plt.ylim((-1,10))

    plt.xlabel('t/s')
    plt.ylabel('X(t)')
    ax = plt.gca()                                           
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')         
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')         
    ax.spines['bottom'].set_position(('data', 0))   
    ax.spines['left'].set_position(('data', 0))
    plt.title("x(t)")

    plt.show()

root = Tk(className='函数')
root.geometry('400x200')

Label = Label(root)
Label.pack()

Button1 = Button(root)
Button1['text'] = '振幅增大的正弦信号'
Button1['command'] = hanshu1
Button1.pack()

Button2 = Button(root)
Button2['text'] = '振幅减小的正弦信号'
Button2['command'] = hanshu2
Button2.pack()

Button3 = Button(root)
Button3['text'] = '        正弦信号       '
Button3['command'] = hanshu3
Button3.pack()

Button4 = Button(root)
Button4['text'] = '        指数信号       '
Button4['command'] = hanshu4
Button4.pack()

root.mainloop()