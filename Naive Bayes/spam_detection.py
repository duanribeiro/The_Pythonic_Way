from nltk.corpus import names
from nltk.stem import WordNetLemmatizer
import glob
import os
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# As written in the database_emails 'Summary.txt' file, there are 3,672 ham (legitimate) emails and 1,500 spam emails
# First, import the necessary modules, glob and os, in order to find all the .txt email files,
# and initialize variables keeping text data and labels
emails, labels = [], []
file_path = 'database_emails/ham/'
for filename in glob.glob(os.path.join(file_path, '*.txt')):
    with open(filename, 'r', encoding="ISO-8859-1") as infile:
        emails.append(infile.read())
        labels.append(0)
file_path = 'database_emails/spam/'
for filename in glob.glob(os.path.join(file_path, '*.txt')):
    with open(filename, 'r', encoding="ISO-8859-1") as infile:
        emails.append(infile.read())
        labels.append(1)

# The next step is to preprocess and clean the raw text data
# Number and punctuation removal, human name removal, stop words removal and lemmatization
def letters_only(astr):
    return astr.isalpha()


def clean_text(docs):
    all_names = set(names.words())
    lemmatizer = WordNetLemmatizer()
    cleaned_docs = []
    for doc in docs:
        all_words = [word.lower() for word in doc.split() if letters_only(word) and word not in all_names]
        cleaned_docs.append(' '.join([lemmatizer.lemmatize(word) for word in all_words]))
    return cleaned_docs

cleaned_emails = clean_text(emails)

# The vectorizer turns each row of a document in a term frequency sparse vector
# The sparse vector, aka term_docs, is in the form of: (ROW INDEX, TERM INDEX) FREQUENCY
cv = CountVectorizer(stop_words="english", max_features=50)
term_docs = cv.fit_transform(cleaned_emails)

# We can search what the corresponding terms index are by using the following
feature_names = cv.get_feature_names()

# With the feature matrix 'term_docs' just generated, we can now build and train our naive Bayes model.
# FIRST STEP: Group the data by label
# The label_index looks like, where training sample indices are grouped by class
# {
#     0: [3000, 3001, 3002, 3003, ...... 6670, 6671],
#     1: [0, 1, 2, 3, ...., 2998, 2999]
# }
def get_label_index(labels):
    from collections import defaultdict
    label_index = defaultdict(list)
    for index, label in enumerate(labels):
        label_index[label].append(index)
    return label_index

label_index = get_label_index(labels)

# SECOND STEP: With label_index, we calculate the PRIOR:
def get_prior(label_index):
    """ Compute prior based on training samples
    Args:
        label_index (grouped sample indices by class)
    Returns:
        dictionary, with class label as key, corresponding prior as the value """
    prior = {label: len(index) for label, index in label_index.items()}
    total_count = sum(prior.values())
    for label in prior:
        prior[label] /= float(total_count)
    return prior

prior = get_prior(label_index)

# THIRD STEP: Calculate the LIKELIHOOD as well:
def get_likelihood(term_document_matrix, label_index, smoothing=0):
    """ Compute likelihood based on training samples
    Args:
        term_document_matrix (sparse matrix)
        label_index (grouped sample indices by class)
        smoothing (integer, additive Laplace smoothing)
    Returns:
        dictionary, with class as key, corresponding
        conditional probability P(feature|class) vector as
        value
    """
    likelihood = {}
    for label, index in label_index.items():
        likelihood[label] = term_document_matrix[index, :].sum(axis=0) + smoothing
        likelihood[label] = np.asarray(likelihood[label])[0]
        total_count = likelihood[label].sum()
        likelihood[label] = likelihood[label] / float(total_count)
    return likelihood

likelihood = get_likelihood(term_docs, label_index, smoothing=1) # likelihood[0] is the conditional probability P(feature | ham) vector of length 500 (500 features) for legitimate classes
print(likelihood[0][:5]) # For example, the following are the probabilities for the first five features
print(likelihood[1][:5]) # Similarly, here are the first five elements of the conditional probability P(feature | spam) vector
print(feature_names[:5]) # We can also check the corresponding terms

# LAST STEP: With PRIOR and LIKELIHOOD ready, we can now computer the posterior for the testing/new samples.
# There is a trick in here:
# instead of calculating the multiplication of hundreds of thousands of small value conditional probabilities P(feature | class),
# which may cause overflow error, we calculate the summation of their natural logarithms then convert it back to its natural exponential value
def get_posterior(term_document_matrix, prior, likelihood):
    """ Compute posterior of testing samples, based on prior and likelihood
    Args:
        term_document_matrix (sparse matrix)
        prior (dictionary, with class label as key, corresponding prior as the value)
        likelihood (dictionary, with class label as key, corresponding conditional probability vector as value)
    Returns:
        dictionary, with class label as key, corresponding posterior as value """
    num_docs = term_document_matrix.shape[0]
    posteriors = []
    for i in range(num_docs):
        posterior = {key: np.log(prior_label) for key, prior_label in prior.items()}
    for label, likelihood_label in likelihood.items():
        term_document_vector = term_document_matrix.getrow(i)
        counts = term_document_vector.data
        indices = term_document_vector.indices
    for count, index in zip(counts, indices):
        posterior[label] += np.log(likelihood_label[index]) * count
    min_log_posterior = min(posterior.values())
    for label in posterior:
        try:
            posterior[label] = np.exp(posterior[label] - min_log_posterior)
        except:
            posterior[label] = float('inf')
    sum_posterior = sum(posterior.values())
    for label in posterior:
        if posterior[label] == float('inf'):
            posterior[label] = 1.0
        else:
            posterior[label] /= sum_posterior
            posteriors.append(posterior.copy())
    return posteriors

# The prediction function is finished. Let's take one ham and one spam sample from another email dataset to quickly verify our algorithm:
emails_test = [
    '''Subject: flat screens
    hello, please call or contact regarding the other flat screens requested.
    trisha tlapek - eb 3132 b
    michael sergeev - eb 3132 a
    also the sun blocker that was taken away from eb 3131 a . trisha should two monitors also michael .
    thanks,
    kevin moore''',
    '''Subject: having problems in bed ? we can help !
    cialis allows men to enjoy a fully normal sex life without
    having to plan the sexual act. if we let things terrify us, life will not be worth living
    brevity is the soul of lingerie.    suspicion always haunts the guilty mind .''',]

# Go through the same cleaning and preprocessing steps as in the training stage:
cleaned_test = clean_text(emails_test)
term_docs_test = cv.transform(cleaned_test)
posterior = get_posterior(term_docs_test, prior, likelihood)

# For the first email, 99.5% are legitimate; the second email nearly 100% are spam. Both arepredicted correctly.
# [{0: 0.99546887544929274, 1: 0.0045311245507072767},
# {0: 0.00036156051848121361, 1: 0.99963843948151876}]
print(posterior)