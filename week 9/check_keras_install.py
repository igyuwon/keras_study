import tensorflow as tf
from keras.models import Sequential
from keras.layers.core import Dense

print(tf.__version__)

model = Sequential()
model.add(Dense(5, input_dim = 5))
model.summary()