import numpy as np
from keras.models import load_model
from keras.datasets import mnist

(x_train, _),(x_test,_) = mnist.load_data()

x_train = x_train.reshape(x_test.shape[0], 784).astype(np.float32) / 255
x_test = x_test.reshape(x_test.shape[0], 784).astype(np.float32) / 255

m = load_model('first.h5')
results = m.predict(x_test[:2])
print(np.argmax(results, axis = 1))