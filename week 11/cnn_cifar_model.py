import numpy as np
from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import load_model

#step 1 : prepare data for infernce
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

x_train = x_train.astype(np.float32) / 255
x_test = x_test.astype(np.float32) / 255
#step 2 :
model = load_model('cnn-cifar.h5')
results=model.predict(x_test[:1])
print(results)
print(np.argmax(results,axis=1))

