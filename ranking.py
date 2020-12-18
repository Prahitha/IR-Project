from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
import numpy as np
import time
import pickle
import pandas

start_processing = time.process_time()

docsize = 100000
df = pandas.read_csv('Reviews.csv', header=None)
df.columns = ['id', 'productID', 'userID', 'username', 'numeratorScore', 'denominatorScore', 'score', 'time', 'summary', 'text']
df = df.iloc[1:]
df = df.drop(['id', 'productID', 'userID', 'username', 'numeratorScore', 'denominatorScore', 'time'], axis=1)
df = df.fillna('summary')

title = df['summary']
titles = title.values.tolist()
titles = titles[:docsize]

review = df['text']
reviews = review.values.tolist()
reviews = reviews[:docsize]

ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

DF= {}
tf_idf = {}
fileno = 1

def preprocessing(review):
	tokenize = word_tokenize(review)
	tokenize = [lemmatizer.lemmatize(word) for word in tokenize]
	tokenize = [word.lower() for word in tokenize if word.isalpha()]
	omitted = stopwords.words('english')

	for word in tokenize:
		if word in omitted:
			tokenize.remove(word)
		ps.stem(word)

	return tokenize


def calculateDF(review, i):
	review = preprocessing(review)
	for word in review:
		try:
			DF[word].add(i)
		except:
			DF[word] = {i}


for review in reviews:
	calculateDF(review, fileno)
	fileno += 1

for i in DF:
	DF[i] = len(DF[i])

total_vocab = [x for x in DF]

# calculate tf_idf
fileno = 1
for review in reviews:
	print(fileno)
	tokens_body = preprocessing(review)
	tokens_title = preprocessing(titles[0])
	counter = Counter(tokens_body + tokens_title)

	for token in np.unique(tokens_body):
		unique_body = len(np.unique(tokens_body))
		unique_title = len(np.unique(tokens_title))
		tf = counter[token]/(unique_body + unique_title)
		df = DF[token]
		idf = np.log(docsize/(df+1))
		tf_idf[fileno, token] = tf*idf

	fileno += 1


try:
	tf_idf_scores = open('tf_idf_scores', 'wb')
	pickle.dump(tf_idf, tf_idf_scores)
	tf_idf_scores.close()

except:
	print("Something went wrong")

end_processing = time.process_time()
print("Time taken to create tf-idf matrix (and pickle it): " + str(end_processing - start_processing))