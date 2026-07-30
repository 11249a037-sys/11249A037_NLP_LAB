from nltk.stem import PorterStemmer
ps = PorterStemmer()
example_words = ["connect","connecting","connected","connects"]
for w in example_words:
    print(ps.stem(w))