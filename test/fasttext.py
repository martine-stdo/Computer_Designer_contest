import fasttext
"""
  训练一个监督模型, 返回一个模型对象

  @param input:           训练数据文件路径
  @param lr:              学习率
  @param dim:             向量维度
  @param ws:              cbow模型时使用
  @param epoch:           次数
  @param minCount:        词频阈值, 小于该值在初始化时会过滤掉
  @param minCountLabel:   类别阈值，类别小于该值初始化时会过滤掉
  @param minn:            构造subword时最小char个数
  @param maxn:            构造subword时最大char个数
  @param neg:             负采样
  @param wordNgrams:      n-gram个数
  @param loss:            损失函数类型, softmax, ns: 负采样, hs: 分层softmax
  @param bucket:          词扩充大小, [A, B]: A语料中包含的词向量, B不在语料中的词向量
  @param thread:          线程个数, 每个线程处理输入数据的一段, 0号线程负责loss输出
  @param lrUpdateRate:    学习率更新
  @param t:               负采样阈值
  @param label:           类别前缀
  @param verbose:         ??
  @param pretrainedVectors: 预训练的词向量文件路径, 如果word出现在文件夹中初始化不再随机
  @return model object
"""
classifier = fasttext.train_supervised(input='../../tmp/train_data.txt', dim=100, epoch=5,
                                       lr=0.1, wordNgrams=2, loss='softmax')
classifier.save_model('../../tmp/classifier.model')


label_to_cate = {'__label__1':'technology', '__label__2':'car', '__label__3':'entertainment',
                 '__label__4':'military', '__label__5':'sports'}

texts = '这 是 中国 制造 宝马 汽车'
labels = classifier.predict(texts)
# print(labels)
print(label_to_cate[labels[0][0]])
