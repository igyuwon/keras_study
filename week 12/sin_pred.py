import math
import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers.rnn import SimpleRNN

def to_red(deg):
    return deg /180 * math.pi

value = []

for deg in range(1440):
    value.append(math.sin(to_red(deg/4)))

#plt.plot(value)
#plt.show()

x_train = []
y_train = []

# step 1 prepare training data
SEQ_LENGTH = 20
FEATURE_LENGTH = 1

for i in range(1440-SEQ_LENGTH):
    x_train.append(value[i:i+SEQ_LENGTH])
    y_train.append(value[i:i + SEQ_LENGTH])

x_train = np.array(x_train)
y_train = np.array(y_train)

#print(x_train.shape, y_train.shape)

# step 2 model design
m = Sequential()
m.add(SimpleRNN(units = 4, input_shape=(SEQ_LENGTH, FEATURE_LENGTH)))
m.add(Dense(units=1))
m.summary()

# step 3 model train
m.compile(loss='mse',optimizer='adam')
m.fit(x = x_train, y = y_train, batch_size=10, epochs=20)

#step 4 model predict
results = m.predict(x_train)

plt.plot(value, 'r')
plt.plot(results,'b')
plt.show()