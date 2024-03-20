import matplotlib.pyplot as plt

x_val = list(range(0,11))
y_line = [x for x in x_val]
y_sqr = [x * x for x in x_val]
y_line2 = [2 * x + 1 for x in x_val]
plt.axis()
plt.plot(x_val, y_line, 'ro')
plt.plot(x_val, y_sqr, 'b*--')
plt.plot(x_val, y_line2, 'mx-.')
plt.show()