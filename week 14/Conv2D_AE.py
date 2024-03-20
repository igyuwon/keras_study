import numpy as np
from keras.datasets import mnist
from keras.models import Sequential, Model
from keras.layers.convolutional import Conv2D, Conv2DTranspose
from keras.layers.core import Dense, Flatten, Reshape
from keras.layers import Input
import cv2

# step 1. prepare dataset
(x_train, _), (x_test, _) = mnist.load_data()
x_train = x_train.astype(np.float32) / 255
x_train = x_train[: , : , : , np.newaxis]
x_test = x_test.astype(np.float32) / 255
x_test = x_test[: , : , : , np.newaxis]

#print(x_train.shape, x_test.shape)

# step 2. design model
model = Sequential()
# encoder
model.add(Conv2D(filters=32, kernel_size=3, padding='same', strides=2,input_shape=(28, 28, 1)))
model.add(Flatten())
model.add(Dense(units=16))
# decoder
model.add(Dense(units=6272))
model.add(Reshape((14, 14, 32)))
model.add(Conv2DTranspose(filters=1, kernel_size=3, padding='same', strides=2))

model.summary()


# step 3. train model
model.compile(loss='mse', optimizer='adam')
model.fit(x=x_train, y=x_train, batch_size=64, epochs=1, validation_split=0.2)

# step 4. predict
results = model.predict(x_test[:1])
print(results[0].shape)
print(x_test[0].shape)
print(np.square(results[0] - x_test[0]).mean())

resimg = np.reshape(results[0],(28,28))
resimg2 = cv2.resize(resimg, (256,256))
cv2.imshow('win1', resimg2)

testimg = np.reshape(x_test[0], (28, 28))
testimg = cv2.resize(testimg, (256, 256))
cv2.imshow('win2', testimg)


cv2.waitKey()
cv2.destroyAllWindows()