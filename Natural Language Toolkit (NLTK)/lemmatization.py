from nltk.corpus import names
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from pprint import pprint as pp
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# First, import one of the three built-in stemmer algorithms and initialize a stemmer:
porter_stemmer = PorterStemmer()
pp(porter_stemmer.stem('lovely'))
pp(porter_stemmer.stem('machines'))

# Now import a lemmatization algorithm based on Wordnet corpus built-in, and initialize an lemmatizer:
lemmatizer = WordNetLemmatizer()
pp(lemmatizer.lemmatize('lovely'))
pp(lemmatizer.lemmatize('machines'))

# The scikit-learn library provides a utility function of loading the dataset.
groups = fetch_20newsgroups()

# The data object is in the form of key-value dictionary. Its keys are as follows:
pp(groups.keys())

# They range from 0 to 19, representing 20 topics. Let’s now have a look at the first document
pp(groups.data[0])
pp(groups.target[0])
pp(groups.target_names[groups.target[0]])

# It's good to visualize to get a general idea of how the data is structured.
# As you can see, the distribution is (approximately) uniform, so that's one less thing to worry about.
sns.distplot(groups.target)
plt.show()

# The following code displays a histogram of the 500 highest word counts. (Pág 44)
cv = CountVectorizer(stop_words="english", max_features=500)
transformed = cv.fit_transform(groups.data)
pp(cv.get_feature_names())
sns.distplot(np.log(transformed.toarray().sum(axis=0)))
plt.xlabel('Log Count')
plt.ylabel('Frequency')
plt.title('Distribution Plot of 500 Word Counts')
plt.show()

# DATA PREPROCESSING (Pág. 47)
# We have two basic strategies to deal words from the same root: stemming and lemmatization.
# Stemming is the more quick and dirty type approach. It involves chopping and the result of stemming doesn't have to be a valid word.
# Lemmatizing, on the other hand, is slower but more accurate. Performs a dictionary lookup and guarantees to return a valid word.

# Let's reuse the code from the previous section to get the 500 words with highest counts, but this time, we will apply filtering:
def letters_only(astr):
    return astr.isalpha()

cv = CountVectorizer(stop_words="english", max_features=500)
all_names = set(names.words())
lemmatizer = WordNetLemmatizer()
for post in groups.data[0:2]:
    all_words = [word.lower() for word in post.split() if letters_only(word) and word not in all_names]
    cleaned = [lemmatizer.lemmatize(word) for word in all_words]
transformed = cv.fit_transform(cleaned)
pp(cv.get_feature_names())