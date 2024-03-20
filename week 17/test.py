import numpy as np
from keras.models import Sequential
from keras.datasets import cifar10
from keras.utils import np_utils
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Flatten, Dense, Dropout
from keras.layers import *
from keras.models import Model
from keras.layers import Dense, Activation
from keras.layers.rnn import SimpleRNN
from keras.models import Sequential

inputs = Input(shape=(32, 32, 3))
x = Conv2D(filters=32, kernel_size=5, padding='same', strides=2)(inputs)
model = Model(inputs=inputs, outputs=x)

#print(model.shape)
model.summary()
print(x.shape)