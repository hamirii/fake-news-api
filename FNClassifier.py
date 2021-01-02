import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import one_hot
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


df = pd.read_csv('./train.csv')
test = pd.read_csv('./test.csv')

df = df.fillna('')
test = test.fillna('')

df['total'] = df['title']+' '+df['author']
test['total'] = test['title'] + ' ' + test['author']

X = df.drop('label', axis=1)

y = df['label']

print(X.shape)
print(y.shape)

voc_size = 5000

msg = X.copy()
msg_test = test.copy()

nltk.download('stopwords')
ps = PorterStemmer()
corpus = []

for i in range(len(msg)):
    review = re.sub('[^a-zA-Z]', ' ', msg['total'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word)
              for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)


corpus_test = []

for i in range(len(msg_test)):
    review = re.sub('[^a-zA-Z]', ' ', msg_test['total'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word)
              for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus_test.append(review)

onehot_rep = [one_hot(words, voc_size) for words in corpus]

onehot_rep_test = [one_hot(words, voc_size) for words in corpus_test]

embedded_docs = pad_sequences(onehot_rep, padding='pre', maxlen=25)

embedded_docs_test = pad_sequences(onehot_rep_test, padding='pre', maxlen=25)

model = Sequential()
model.add(Embedding(voc_size, 40, input_length=25))
model.add(Dropout(0.3))
model.add(LSTM(100))
model.add(Dropout(0.3))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy'])
print(model.summary())

X_final = np.array(embedded_docs)
y_final = np.array(y)
test_final = np.array(embedded_docs_test)

X_final.shape, y_final.shape, test_final.shape

model.fit(X_final, y_final, epochs=25, batch_size=64)

model.save('saved_model/my_model')
