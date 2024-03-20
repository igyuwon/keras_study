import numpy as np
from keras.models import Sequential
from keras.datasets import cifar10
from keras.utils import np_utils
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Flatten, Dense, Dropout

# step 1 : prepare datasets
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
# print(x_train.shape, y_train.shape)
# print(x_test.shape, y_test.shape)

x_train = x_train.astype(np.float32) / 255
x_test = x_test.astype(np.float32) / 255

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

# print(x_test.shape, y_test.shape)

# step 2 : design model
model = Sequential()
# feature extraction
model.add(Conv2D(filters=32, kernel_size=(3, 3), input_shape=(32,32,3) ,activation='relu', padding='same'))
model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same'))
model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# multi-dimensional data --> one dimen
model.add(Flatten())

# classification
model.add(Dense(units=512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=10, activation='softmax'))

model.summary()

# step 3 : train model & evaluate
model.compile(optimizer='adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

model.fit(x=x_train, y=y_train, epochs=1, batch_size=64, validation_split=0.2)

scores = model.evaluate(x=x_test, y=y_test, batch_size = 64)
print(scores)

#step 4 : model save
model.save('cnn-cifar.h5')
