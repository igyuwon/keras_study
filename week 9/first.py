from keras.models import Sequential
from keras.layers.core import Dense, Activation
import numpy as np

x_train = np.random.random((1000,5))
y_train = np.random.random((1000,4))
x_test = np.random.random((1000,5))
y_test = np.random.random((1000,4))
model = Sequential()
#model.add(Dense(units=4, input_dim=5, kernel_initializer='random_uniform'))
model.add(Dense(units=4, input_dim=5, kernel_initializer='random_uniform', activation='relu'))
model.add(Activation('softmax'))
model.summary()
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(x=x_train, y=y_train, batch_size=100,epochs=2,validation_split=0.2)  #전체 1000 실제학습 800 검증용 200
score = model.evaluate(x_test, y_test, batch_size=100)
print(score)
results = model.predict(x_test[:5])
print(results)
print('=' * 40)
print(y_test[:5])

