# Word2Vec代码参考：https://github.com/jsksxs360/Word2Vec
# WJ计算相似度与SSF相似度在命令行上进行输出的比较
from SSFN_V4_02 import Word2Vec
from SSFN_V4_02 import SSF_V2 as ssf
w2v = Word2Vec.Word2Vec('D:\GoogleNews-vectors-negative300.bin', kind='bin')
print('dog|cat: ', w2v.word_similarity('dog', 'cat'))
ssf.init("dog", "cat")
ssf.calc_simi_element(ssf.Sen1_word, ssf.Sen2_word, ssf.Sen1_word_vec_set, ssf.Sen2_word_vec_set)
ssf.init_set()
similarity = ssf.calc_sen_simi()
print("SSF: {0}".format(similarity))
print("WJ: {0}".format(w2v.word_similarity('dog', 'cat')))

