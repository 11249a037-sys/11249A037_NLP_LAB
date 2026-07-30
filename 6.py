import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sentence = input("Enter a sentence: ")
#words = nltk.word_tokenize(sentence)
words = word_tokenize(sentence)
pos_tagged = nltk.pos_tag(words)
print("\nwords\tPos\tTag")
print("-" * 30)
for word, tag in pos_tagged:
    print(f"{word}\t\t{tag}")




