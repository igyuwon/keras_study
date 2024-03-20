from keras.layers import Dense, Activation
from keras.layers.rnn import SimpleRNN
from keras.models import Sequential
import numpy as np

fd = open('/Users/igyuwon/PycharmProjects/aiprogramming/11-0.txt','rb')
lines = []

for line in fd:
    tmp = line.strip().lower()
    if len(tmp) == 0:
        continue
    lines.append(tmp)

fd.close()

one_line = ' '.join(lines)

#print(one_line)

chars = set([c for c in one_line])
nb_chars = len(chars)
print(nb_chars)
print(chars)
exit()
index2char = dict((i, c) for i,c in enumerate(chars))
char2index = dict((c, i) for i,c in enumerate(chars))

print(char2index['a'])
exit()

#prepare data
SEQ_LENGTH = 10
STEP = 1
input_chars = []
label_chars = []

for i in range(0,len(one_line)-SEQ_LENGTH, STEP):
    input_chars.append(one_line[i:i+SEQ_LENGTH])
    label_chars.append(one_line[i+SEQ_LENGTH])

x_train = np.array(input_chars)
y_train = np.array(label_chars)

print(x_train.shape)
print(y_train.shape)
print(x_train[0])
print(y_train)
