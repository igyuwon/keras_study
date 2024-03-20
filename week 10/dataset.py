from keras.datasets import mnist
import numpy as np
from keras.utils import np_utils

(x_train, y_train),(x_test,y_test) = mnist.load_data()

#print(x_train.shape, x_test.shape)
#print(y_train.shape, y_test.shape)
#print(y_train[0])
#print(y_test[0])
x_train = x_train.reshape(x_train.shape[0], 784).astype(np.float32) / 255
x_test = x_test.reshape(x_test.shape[0], 784).astype(np.float32) / 255

print(y_train.shape, y_train[0])

y_train = np_utils.to_categorical(y_train,10)
y_test = np_utils.to_categorical(y_test,10)

print(y_train.shape, y_train[0])
