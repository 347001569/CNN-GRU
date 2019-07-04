import pkuseg
from gensim.models import word2vec
import gensim
import logging

news_name=[
    'news_tech',
    'news_entertainment',
    'news_game',
    'news_sports',
    'news_car',
]
save_model_file='item/toutiao.model'

def cutwords():# 使用文档级分词必须用全局main
    print('cutting  words')

    stopword=stopwords()
    seg = pkuseg.pkuseg()
    with open('item/sum_news.txt','w',encoding='utf-8') as file2:
        for news in news_name:
            with open('news/%s.txt'%news,'r',encoding='utf-8') as file:
                reads=file.readlines()
                for read in reads: #每条新闻
                    text=seg.cut(read)
                    str = []
                    for t in text: #每条新闻分的每个词
                        flag=False
                        for stop in stopword:
                            if t==stop:
                                flag=True
                                break
                        if  flag==False:
                            str.append(t)
                        else:continue
                    if len(str)<=3:
                        continue
                    else:
                        re=' '.join(str)
                        file2.write( news+' '+re+'\n')

def stopwords():
    str=[]
    with open('item/停用词.txt','r') as file1:
        reads=file1.readlines()
        for read in reads:
            read=read.replace('\n','')
            str.append(read)
    return str

def createDatabase():
    with open('item/sum_news.txt','r',encoding='utf-8') as file1 ,open('item/database.txt','w',encoding='utf-8') as file2:
        reads=file1.readlines()
        for read in reads:
            index=read.find(' ')
            read=read[index+1:].replace('\n',' ')
            file2.write(read)

def word2wec(save_model_file):  # model_file_name为训练语料的路径,save_model为保存模型名
    # 模型训练，生成词向量
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)#生成日志
    sentences = word2vec.Text8Corpus('item/database.txt')  # 加载语料
    model = gensim.models.Word2Vec(sentences)  # 训练skip-gram模型; 默认window=5
    model.save(save_model_file)

#createDatabase()
def main():
    cutwords()
    createDatabase()
    word2wec(save_model_file)
if __name__ == '__main__':
    main()