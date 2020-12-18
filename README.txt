Necessary Libraries:
Tkinter
Nltk
Numpy
Pandas
Pickle

Github link for the project:
https://github.com/Prahitha/IR-Project

Components:
Data collection
Preprocessing
Ranking
Querying
Spell checking (query)
Tkinter UI

Data has been taken from Kaggle (Amazon Fine Food Reviews Dataset)
Preprocessing and ranking has been done in ranking.py
The result from calculating TF-IDF scores has been pickled in tf_idf_scores.pkl
Querying is done in querying.py
For spell checking, I build a basic spell checker which uses the Levenshtein edit distance concept and basic probabilty
Tkinter UI for querying


Setup:
1. Please make sure that you have all the necessary libraries installed
on your local machine

2. Navigate to the folder in which querying.py is present

3. To run the code enter "py querying.py" if using Python3
or "python querying.py" if using Python2

4. Then after a couple of seconds a Tkinter window will popup

5. Fill in the prompts in the respective text boxes
Eg: "dog food" in the query and "5" for the number of results (as desired)

6. Then click on the "Show" button to get the results

7. Click on the "Quit" button when done

