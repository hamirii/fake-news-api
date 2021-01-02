import pandas as pd
import tensorflow as tf
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from tensorflow.keras.preprocessing.text import one_hot
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords

voc_size = 5000

# Ideally, what we get from the internet should be in the following categories:
# id, headline/title, coverImageUrl, logoImageUrl, url, author, text, category
# Then we create a new "test" dataframe that drops the coverImageUrl, LogoImageUrl, url, category
# After cycling through tests and finding array of fake Articles,
# we need to then match their id's to the original dataframe and extract title, imageUrl, logoImageUrl, url, category
# Create a json file with that information for render

# Test Categories: id, title, author, text
test = pd.read_csv('./test.csv')

test = test.fillna('')

test['total'] = test['title'] + ' ' + test['author']

msg_test = test.copy()

ps = PorterStemmer()

corpus_test = []

for i in range(len(msg_test)):
    review = re.sub('[^a-zA-Z]', ' ', msg_test['total'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word)
              for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus_test.append(review)


onehot_rep_test = [one_hot(words, voc_size) for words in corpus_test]


embedded_docs_test = pad_sequences(onehot_rep_test, padding='pre', maxlen=25)

test_final = np.array(embedded_docs_test)

model = tf.keras.models.load_model('saved_model/my_model')

# Check its architecture
model.summary()

y_prediction = (model.predict(test_final) > 0.5).astype("int32")

final_sub = pd.DataFrame(y_prediction, columns=['label'])

final_sub['id'] = test['id']

# Return array of indices where the 'fake news' articles are located
labelOnes = (np.where(final_sub['label'] == 1))[0]

# Return array of all the articles classified as fake
fakeArray = test.iloc[labelOnes].to_numpy()

# Return ids of the fake articles - this one is not particularly useful
idFakes = [test['id'][i] for i in labelOnes]
