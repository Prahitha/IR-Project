from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
from tkinter import *
from tkinter.messagebox import *
import re
import numpy as np
import warnings
import time
import pickle
import pandas

warnings.filterwarnings('ignore')

df = pandas.read_csv('Reviews.csv', header=None)
df.columns = ['id', 'productID', 'userID', 'username', 'numeratorScore', 'denominatorScore', 'score', 'time', 'summary', 'text']
df = df.iloc[1:]
df = df.drop(['id', 'userID', 'username', 'numeratorScore', 'denominatorScore', 'time', 'summary'], axis=1)

pickle_file = open('tf_idf_scores', 'rb')
tf_idf = pickle.load(pickle_file)

ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()
score = pandas.to_numeric(df['score'])
scores = score.values.tolist()

def words(text): 
    return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('sherlock-holmes.txt').read()))

def wordProbability(word, N=sum(WORDS.values())):
    return WORDS[word] / N

def correction(word):
    return max(candidates(word), key=wordProbability)

def candidates(word):
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words):
    return set(w for w in words if w in WORDS)

# levenshtein distance for 1 char edit
def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

# 2 char edits using levenshtein twice
def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def preprocessing(review):
	tokenize = word_tokenize(review)
	tokenize = [lemmatizer.lemmatize(word) for word in tokenize]
	tokenize = [word.lower() for word in tokenize if word.isalpha()]
	omitted = stopwords.words('english')

	for word in tokenize:
		word = correction(word)

	for word in tokenize:
		if word in omitted:
			tokenize.remove(word)
		ps.stem(word)

	return tokenize

def matching_score(query):
	tokens = preprocessing(query)
	query_weights = {}
	for key in tf_idf:
		if key[1] in tokens:
			try:
				query_weights[key[0]] += tf_idf[key]
			except:
				query_weights[key[0]] = tf_idf[key]

	return query_weights

def initiate_search(k, query):
	query_words = query.split(' ')
	final_string = " "
	
	for word in query_words:
		word = word.lower()
		final_string = final_string + ' ' + correction(word)
	
	results = matching_score(final_string)
	results.update((x, y*score[x]) for x, y in results.items())
	results = (sorted(results.items(), key=lambda item: item[1], reverse=True))
	result = results[:k]
	return result

def return_result():
	k = int(query2.get())
	query = str(query1.get())
	start_processing = time.process_time()

	retrieved_result = initiate_search(k, query)
	print(retrieved_result)

	end_processing = time.process_time()
	print("Time taken to return query results: " + str(end_processing - start_processing))

	retrieved = ""
	for key in retrieved_result:
		print(df['text'][key[0]])
		retrieved = retrieved + "Review: " + df['text'][key[0]] + "\n" + "Product ID: " + df['productID'][key[0]] + "\n\n"
		print(df['productID'][key[0]])
		print('\n')
	results_textbox.insert(INSERT, retrieved)

main = Tk()
main.title('Simple Search Engine')
Label(main, text="Enter your query:").grid(row=0)
Label(main, text="Enter the number of results:").grid(row=1)
Label(main, text="Results:").grid(row=2)

query1 = Entry(main)
query2 = Entry(main)
results_textbox = Text(main, bg="antique white")

query1.grid(row=0, column=1)
query2.grid(row=1, column=1)
results_textbox.grid(row=2, column=1, padx="40px")

Button(main, text='Quit', height=2, width=20, bg="coral1", command=main.destroy).grid(row=4, column=0, sticky=W, pady=4)
Button(main, text='Show', height=2, width=20, bg="PaleGreen1", command=return_result).grid(row=4, column=3, sticky=W, pady=4)

mainloop()