from keras.models import Sequential
from keras.layers.core import Dense, Activation
import numpy as np
from keras.datasets import mnist
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

model = Sequential()
model.add(Dense(units=10, input_dim=784, activation='relu'))
model.add(Activation('softmax'))
model.summary()
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(x=x_train, y=y_train, batch_size=128,epochs=1,validation_split=0.2)  #전체 1000 실제학습 800 검증용 200

score = model.evaluate(x = x_test, y = y_test, batch_size=128)
print(score)
results = model.predict(x_test[:2])
print(y_test[:2])
print(results)