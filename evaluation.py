from nltk.translate.meteor_score import meteor_score
from nltk.stem import snowball
import snowballstemmer
from nltk.corpus import wordnet


Output = str(open("C:\\Users\\91742\\Desktop\\Out.txt", encoding="utf8"))
Reference = str(open("C:\\Users\\91742\\Desktop\\Ref.txt", encoding="utf8"))
print(meteor_score(references=Reference, hypothesis=Output, preprocess=Output.lower(),
                   stemmer=snowballstemmer.stemmer('hindi'), wordnet=wordnet, alpha=float(0.9),
                   beta=float(3), gamma=float(0.5)))
