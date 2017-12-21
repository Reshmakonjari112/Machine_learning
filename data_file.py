
import pandas as pd
import string

df = pd.read_table('SMSSpamCollection',
                   sep='\t',
                   header=None,
                   names=['label', 'sms_message'])
print df.head() # returns rows & columns
# --------------------------------------------------------------------------------------------------



df['label'] = df.label.map({'ham':0, 'spam':1}) #convert the label column to numerical usin map
print df.shape # number of rows & coumns using shape
print df.head()
# --------------------------------------------------------------------------------------------------



documents = ['Ok lar? Joking wif u oni...',
             'U dun say so early hor... U c already then say ...',
             'I HAVE A DATE ON SUNDAY WITH WILL!!',
             'Lol your always so convincing.']
lower_case_documents = []
for i in documents:
    lower_case_documents.append(i.lower()) # printing all document list in lowercase documents
                                           # as a list with all words in lowercase
print lower_case_documents
# --------------------------------------------------------------------------------------------------


# remove_punctuation_document = []
#
# # words = string.maketrans('', string.punctuation)
# for i in lower_case_documents:
#     remove_punctuation_document.append(i.translate(string.maketrans('', '', string.punctuation)))
# print remove_punctuation_document
# --------------------------------------------------------------------------------------------------

preprocessed_documents = []
for i in lower_case_documents:
    preprocessed_documents.append(i.split(' '))
print preprocessed_documents
# --------------------------------------------------------------------------------------------------


frequency_list = []
import pprint
from collections import Counter

# Using the Counter() method and preprocessed_documents as the input,
# create a dictionary with the keys being each word in each document
# and the corresponding values being the frequncy of occurrence of that word.
for i in preprocessed_documents:
    frequency_count = Counter(i)
    frequency_list.append(frequency_count)
pprint.pprint(frequency_list)
# --------------------------------------------------------------------------------------------------


from sklearn.feature_extraction.text import CountVectorizer

count_vector = CountVectorizer()
print count_vector
count_vector.fit(documents)
print count_vector.get_feature_names()
# --------------------------------------------------------------------------------------------------

doc_array = count_vector.transform(documents).toarray
print doc_array
# --------------------------------------------------------------------------------------------------

frequency_matrix = pd.DataFrame(doc_array, columns=count_vector.get_feature_names())
print frequency_matrix