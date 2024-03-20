import matplotlib.pyplot as plt
import random

x_val = [0,1,2,3]
y_val = [random.randint(0,100) for _ in range(4)]
x_label = ['korea', 'english', 'math', 'science']

plt.bar(x_val, y_val, color=['blue', 'yellow', 'green', 'red'], width=[0.5, 0.2, 0.8, 1.0])
plt.xticks(x_val, x_label)
plt.show()