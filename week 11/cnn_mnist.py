import numpy as np
from keras.models import Sequential
from keras.datasets import mnist
from keras.utils import np_utils
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Flatten, Dense

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)

x_train = x_train.astype(np.float32) / 255
x_test = x_test.astype(np.float32) / 255

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

x_train = x_train[:, :, :, np.newaxis]
x_test = x_test[:, :, :, np.newaxis]

# print(x_train.shape)

# step 2 : design model
model = Sequential()

model.add(Conv2D(filters=20, input_shape=(28,28,1), kernel_size=(5,5), padding='same', activation='relu')) # Conv2d
model.add(MaxPooling2D(pool_size = (2,2))) # Maxpooling

model.add(Conv2D(filters=50, kernel_size=(5,5), padding='same', activation='relu')) # Conv2d
model.add(MaxPooling2D(pool_size = (2,2))) # Maxpooling

model.add(Flatten())
# 분류
model.add(Dense(units=500, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

model.summary()

# step 3 : training & evaluate
model.compile(optimizer='adam', loss='categorical_crossentropy')
model.fit(x = x_train, y = y_train, batch_size=128, epochs=1, validation_split=0.25)

model.evaluate(x = x_test, y = y_test, batch_size=128)

# step 4 : model predict
results = model.predict(x_test[:100])
print(results)
print(np.argmax(results, axis=1))

model.save('cnn-mnist.h5')