import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math


def d2r(d):
    return d * math.pi / 180
x_val = [x for x in range (360)]
y_sin = [math.sin(d2r(x)) for x in x_val]
y_cos = [math.cos(d2r(x)) for x in x_val]
y_tan = [math. tan(d2r(x)) if not x in [90, 270] else 0 for x in x_val]

plt.axis([0, 360, -1.5, 1.5]) #x축과 y축 범위 지정
plt.plot(x_val, y_sin, 'r')
plt.plot(x_val, y_cos, 'b')
plt.plot(x_val, y_tan, 'g')
plt.legend(loc = 'lower right', fontsize=15, frameon = True, shadow=True)
#plt.legend(loc=(0.2, 0.5), fontsize=15, frameon=True, shadow=True)
plt.grid(True, axis='x')
plt.xticks([0, 100, 200, 300])

plt.show()