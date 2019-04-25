"""
网上找到的WMD算法实现代码
"""
news_headline1 = "Elon Musk's Boring Co to build high-speed airport link in Chicago"
news_headline2 = "Elon Musk's Boring Company to build high-speed Chicago airport link"
news_headline3 = "Elon Musk’s Boring Company approved to build high-speed transit between downtown Chicago and O’Hare Airport"
news_headline4 = "Both apple and orange are fruit"

news_headlines = [news_headline1, news_headline2, news_headline3, news_headline4]

# Load Word Embedding Model
import gensim
print('gensim version: %s' % gensim.__version__)
glove_model = gensim.models.KeyedVectors.load_word2vec_format('D:\GoogleNews-vectors-negative300.bin', binary=True)
# Remove stopwords
import spacy
spacy_nlp = spacy.load('en')
headline_tokens = []
for news_headline in news_headlines:
    headline_tokens.append([token.text.lower() for token in spacy_nlp(news_headline) if not token.is_stop])

print(headline_tokens)

subject_headline = news_headlines[0]
subject_token = headline_tokens[0]

print('Headline: ', subject_headline)
print('=' * 50)
print()

for token, headline in zip(headline_tokens, news_headlines):
    print('-' * 50)
    print('Comparing to:', headline)
    print(subject_token, token)
    distance = glove_model.wmdistance(subject_token, token)
    print('distance = %.4f' % distance)