import numpy as np
from keras.models import Sequential, Model
from keras.layers.core import Dense
from keras.layers import Input
from keras.layers.convolutional import Conv2D, Conv2DTranspose, MaxPooling2D
from keras.layers.rnn import SimpleRNN
from keras.datasets import mnist

(x_train, _), (x_test, _) = mnist.load_data()
x_train = np.reshape(x_train.astype(np.float32) / 256, (-1, 784))
x_test = np.reshape(x_test.astype(np.float32) / 256, (-1, 784))

# 1번 : Input 계층
inputs = Input(shape=(784,))
# 2번 : encoder : Dense 계층
x = Dense(units=128, activation='relu')(inputs)
latent_vector = Dense(units=100, activation='relu')(x)
# 3번 : decoder : Dense 계층
y = Dense(units=128, activation='relu')(inputs)
x_ = Dense(units=784, activation='relu')(y)
model = Model(inputs=inputs, outputs=y)  # 모델 만들기
# 4번 : 모델 컴파일. 손실함수 - mse, 옵티마이저 - adam
# 5번 : 학습 ; epochs=2, batch_size = 128

results = model.predict(x_test[0:1])

print(np.square(results[0] - x_test[0]).mean())

inputs = Input(shape=(784,))
x = Dense(units=100, activation='relu')(inputs)
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