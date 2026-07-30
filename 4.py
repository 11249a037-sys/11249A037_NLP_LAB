from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
new_text = "Is very important to be pythonly while you are pythoning with python ALL pythoners have poorly pythoned atlest once"
words = word_tokenize(new_text)
print(words)
for w in words:
    print(ps.stem(w))


