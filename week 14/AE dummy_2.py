import numpy as np
from keras.datasets import mnist
from keras.models import Model, Sequential
from keras.layers.core import Dense
import cv2
from keras.layers import Input

(x_train, _), (x_test, _) = mnist.load_data()
x_train = x_train.astype(np.float32) / 255
x_test = x_test.astype(np.float32) / 255
x_train = np.reshape(x_train, (-1, 784))
x_test = np.reshape(x_test, (-1, 784))

# print(x_train.shape)
# print(x_test.shape)

model = Sequential()
# encoder
#model.add(Dense(units=128, activation='relu', input_shape=(784,)))
#model.add(Dense(units=64, activation='relu'))
inputs = Input(shape=(784,))
x = Dense(units=128, activation='relu')(inputs)
latent_vector = Dense(units=64, activation='relu')(x)
encoder = Model(inputs=inputs, outputs=latent_vector, name='ENCODER')
encoder.summary()
# decoder
#model.add(Dense(units=128, activation='relu'))
#model.add(Dense(units=784))
d_inputs = Input(shape=(64,))
y = Dense(units=128, activation='relu')(d_inputs)
x_ = Dense(units=784, activation='relu')(y)
decoder = Model(inputs=d_inputs, outputs=x_)
decoder.summary()

#인코더 디코더 결합
model = Model(inputs=inputs, outputs=decoder(encoder(inputs)))
model.summary

# train => 정답과 비교할 손실함수
model.compile(loss='mse', optimizer='adam')
model.fit(x=x_train, y=x_train, batch_size=128, epochs=1, validation_split=0.2)

# predict
results = model.predict(x_test[:1])
print(results[0].shape)
print(x_test[0].shape)
print(np.square(results[0] - x_test[0].mean()))

resimg = np.reshape(results[0], (28,28))
resimg2 = cv2.resize(resimg,(256,256))
cv2.imshow('win1',resimg2)

testimg = np.reshape(x_test[0], (28,28))
testimg = cv2.resize(testimg, (256, 256))
cv2.imshow('win2', testimg)

cv2.waitKey()
cv2.destoryAllWindow()
