import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import load_model


(x_train, y_train), (x_test, y_test) = mnist.load_data()

#print(x_train.shape)

x_train = x_train.astype(np.float32) / 255
x_test = x_test.astype(np.float32) / 255

x_train = x_train[:, :, :, np.newaxis]
x_test = x_train[:, :, :, np.newaxis]

#step 2 : load model
m = load_model('cnn-mnist.h5')
results = m.predict(x_test[:1])
print(np.argmax(results, axis=1))

