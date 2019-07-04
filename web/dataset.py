from gensim.models import word2vec
import numpy as np
from sklearn.model_selection import train_test_split

model_name = 'item/toutiao.model'

def words_pro(words, model):
    word = words.split(' ')  # 存词的数组
    data = np.zeros((100,), 'float32')
    count = 0
    for w in word:
        if w in model:
            data += model[w]
        else:
            count += 1

    if len(word) == count:
        return data, False
    else:
        data = data / (len(word) - count)
        return data, True

def words_vec(model):
    dict = {'news_car': 0, 'news_entertainment': 1, 'news_game': 2, 'news_sports': 3, 'news_tech': 4}
    labels = []  # 标签
    datas = []  # 数据

    with open('item/sum_news.txt', 'r', encoding='utf-8') as file:
        reads = file.readlines()
        for read in reads:
            index = read.find(' ')
            words = read[index + 1:]
            data, flag = words_pro(words, model)
            if flag is False:  # flag为False 时说明这些词都不在词典中
                continue
            else:
                datas.append(data)

            label = dict[read[:index]]
            labels.append(label)

        data_train, data_test, label_train, label_test = train_test_split(datas, labels, test_size=0.2,
                                                                          random_state=42)
        data_train = np.array(data_train)
        data_test = np.array(data_test)
        label_train = np.array(label_train)
        label_test = np.array(label_test)
        return data_train, data_test, label_train, label_test

def get_datas():
    try:
        # 加载模型
        model = word2vec.Word2Vec.load(model_name)
        return words_vec(model)
    except IOError:
        print('模型不存在')

def main():
    data_train, data_test, label_train, label_test=get_datas()
    print(data_test)

if __name__ == '__main__':
    main()