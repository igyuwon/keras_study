from keras.models import Sequential
from keras.layers.core import Dense, Activation,Dropout
import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils

model = Sequential()
model.add(Dense(units=10, input_dim=784, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(units=10))
model.add(Dropout(0.25))
model.add(Dense(units=10))
model.summary()