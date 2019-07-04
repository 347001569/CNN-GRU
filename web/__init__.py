from gensim.models import word2vec
model_name='item/toutiao.model'
model=word2vec.Word2Vec.load(model_name)
import numpy as np
data=[]

d=(model['开'])
c=(model['宝马'])
data.append(d)
data.append(c)
data=np.array(data)
data=data.reshape(2,100)

print(data)