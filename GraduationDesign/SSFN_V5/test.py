

# Word2Vec代码参考：https://github.com/jsksxs360/Word2Vec
# 使用论文中提到的WJ算法计算相似度
from SSFN_V5 import Word2Vec
import time
start_time = time.time()
w2v = Word2Vec.Word2Vec('D:\GoogleNews-vectors-negative300.bin', kind='bin')
end_time = time.time()
print("加载模型花费了{0}".format(end_time - start_time))
start_time2 = time.time()
print('dog|cat: ', w2v.word_similarity('dog', 'cat'))
end_time2 = time.time()
print("计算相似度花费了{0}".format(end_time2 - start_time2))

