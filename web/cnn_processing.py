from spider.web.dataset import get_datas
import time
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Convolution1D,MaxPooling1D,Flatten
from keras.optimizers import Adam

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

def cnn_pro():
    model=Sequential()

#第一层卷积
    model.add(Convolution1D(
        input_shape=(100,1),
        filters=32,
        kernel_size=5,
        padding='valid',
        activation='relu'

    ))
#第一层池化
    model.add(MaxPooling1D(
        pool_size=2,
        strides=2,
        padding='valid'
    ))

#第二层
    model.add(Convolution1D(64,5,padding='valid',activation='relu'))
    model.add(MaxPooling1D(pool_size=2,padding='valid'))

#全连接层
    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dense(5, activation='softmax'))

#optimizer
    adam=Adam(lr=1e-4)

#model
    model.compile(
        optimizer=adam,
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

def train(model)  :
    data_train, data_test, label_train, label_test = data_pro()
    print('Training---------------------------------')
    start = time.time()
 # training
    model.fit(data_train, label_train, epochs=1000, batch_size=64)
    print('\nTesting---------------------------')
# testing
    loss, accuracy = model.evaluate(data_test, label_test)
    end = time.time()
    print('test loss:', loss)
    print('test accuracy:', accuracy)
    print('运行时间：',end-start)

def main():
    model=cnn_pro()
    train(model)

if __name__ == '__main__':
    main()

