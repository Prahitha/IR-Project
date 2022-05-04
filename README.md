# IR-Project

## Link to the project (zipped file):
https://drive.google.com/file/d/1Ritj6hxiE8nnnjm41yCOdBL8l_r_PMwc/view?usp=sharing

## Necessary Libraries:
Tkinter
Nltk
Numpy
Pandas
Pickle

## Components:
Data collection - Data has been taken from Kaggle (Amazon Fine Food Reviews Dataset)
Preprocessing - Preprocessing and ranking has been done in ranking.py
Ranking - The result from calculating TF-IDF scores has been pickled in tf_idf_scores.pkl
Querying - Querying is done in querying.py
Spell checking (query - For spell checking, I build a basic spell checker which uses the Levenshtein edit distance concept and basic probabilty
Tkinter UI - Tkinter UI for querying

## Setup:
1. Please make sure that you have all the necessary libraries installed on your local machine
2. Navigate to the folder in which querying.py is present
3. To run the code enter "py querying.py" if using Python3 or "python querying.py" if using Python2
4. Then after a couple of seconds a Tkinter window will popup
5. Fill in the prompts in the respective text boxes
Eg: "dog food" in the query and "5" for the number of results (as desired)
6. Then click on the "Show" button to get the results
7. Click on the "Quit" button when done

<img width="932" alt="Screenshot 2022-05-04 at 9 18 04 PM" src="https://user-images.githubusercontent.com/44160152/166720078-f9fc4f25-7778-4b85-92a7-51a10dfd8bc3.png">

For more details on the implementation: Refer to the document [here](https://github.com/Prahitha/IR-Project/blob/main/Documentation.pdf)
