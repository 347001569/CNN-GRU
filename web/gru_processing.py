from keras.models import Sequential
from keras.utils import np_utils
from keras.layers import GRU,Dense
from keras.optimizers import Adam
import time

from spider.web.dataset import get_datas

def data_pro():
    # data_train (6951,100)
    # data_test (3424,100)
    data_train, data_test, label_train, label_test=get_datas()

    # data pre-processing
    data_train = data_train.reshape(-1, 100, 1)
    data_test = data_test.reshape(-1, 100, 1)
    label_train = np_utils.to_categorical(label_train, num_classes=5)
    label_test = np_utils.to_categorical(label_test, num_classes=5)

    return data_train, data_test, label_train, label_test

def gru_pro():

    model = Sequential()

#gru层
    model.add(GRU(
        units=50,
        input_shape=(100,1),
        activation='relu',

    ))

#全连接层
    model.add(Dense(5,activation='softmax'))

    adam = Adam(0.001)
    model.compile(
        optimizer=adam,
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

def train(model):

    data_train, data_test, label_train, label_test=data_pro()
    start = time.time()
    model.fit(data_train, label_train, epochs=100, batch_size=64)
    cost, accuracy = model.evaluate(data_test, label_test, batch_size=64, verbose=1)
    end = time.time()
    print('test cost:', cost, 'test accuracy:', accuracy)
    print('运行时间：',end-start)

def main():
    model=gru_pro()
    train(model)

if __name__ == '__main__':
    main()