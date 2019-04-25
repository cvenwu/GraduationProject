from SSFN_V2 import SSF_V1 as ssf

if __name__ == '__main__':
    Sen1 = input("请输入句子1：")
    Sen2 = input("请输入句子2：")
    ssf.init(Sen1, Sen2)
    ssf.calc_simi_element(ssf.Sen1_word, ssf.Sen2_word, ssf.Sen1_word_vec_set, ssf.Sen2_word_vec_set)
    ssf.init_set()
    similarity = ssf.calc_sen_simi()
    print("两个句子的相似度为 : ", similarity)
