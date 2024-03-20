import tensorflow as tf
from keras import layers

from keras import datasets

import matplotlib.pyplot as plt

import numpy as np

input_shape = (28, 28, 1)
num_classes = 10

learning_rate = 0.001

inputs = layers.Input(input_shape)
net = layers.Conv2D(32, (3, 3), padding='SAME')(inputs)
net = layers.Activation('relu')(net)
net = layers.Conv2D(32, (3, 3), padding='SAME')(net)
net = layers.Activation('relu')(net)
net = layers.MaxPooling2D(pool_size=(2, 2))(net)
net = layers.Dropout(0.5)(net)

net = layers.Conv2D(64, (3, 3), padding='SAME')(net)
net = layers.Activation('relu')(net)
net = layers.Conv2D(64, (3, 3), padding='SAME')(net)
net = layers.Activation('relu')(net)
net = layers.MaxPooling2D(pool_size=(2, 2))(net)
net = layers.Dropout(0.5)(net)

net = layers.Flatten()(net)
net = layers.Dense(512)(net)
net = layers.Activation('relu')(net)
net = layers.Dropout(0.5)(net)
net = layers.Dense(num_classes)(net)
net = layers.Activation('softmax')(net)

model = tf.keras.Model(inputs=inputs, outputs=net, name='Basic_CNN')

# Model is the full model w/o custom layers
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

(train_x, train_y), (test_x, test_y) = datasets.mnist.load_data()

num_epochs = 1
batch_size = 64

model.fit(train_x, train_y,batch_size=batch_size,shuffle=True)
model.evaluate(test_x, test_y, batch_size = batch_size)

test_image = test_x[0,:,:,0]
test_image.shape

plt.title(test_y[0])
plt.imshow(test_image,'gray')
plt.show()

pred = model.predict(test_image.reshape(1,28,28,1))
print(pred.shapepred)