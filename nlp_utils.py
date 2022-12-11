#!/usr/bin/env python
# coding: utf-8

import re
import unicodedata
# import json
import contractions

import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
english_stopwords = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

def lowercase_text(input_text):
    text = input_text.lower()
    return text

def normalize_whitespace(input_text):
    text = re.sub("\s+"," ",input_text)
    return text


def replace_html_tags(input_text):
    return re.sub('<.*?>','',input_text)

def remove_emails(input_text):
    return re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"", input_text)

def remove_urls(input_text):
    return re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '' , input_text)

def normalize_unicode(input_text):
    return unicodedata.normalize('NFKD', input_text).encode('ascii', 'ignore').decode('utf-8', 'ignore')

def replace_abbreviations(x):
#     """
#     This is kind of dogsh*t; consider using the "contractions" package instead
#     """
#     for key in abbreviations:
#         if key in x:
#             x = x.replace(key,abbreviations[key])

    x = contractions.fix(x)

    return x

def get_just_words(doc):
    return re.sub(r'[^\w ]+', "", doc)

def remove_stopwords(doc):
    cleaned_doc = ' '.join([word for word in doc.split() if word not in english_stopwords])
    cleaned_doc = re.sub(r"(\s[.]{1}\s)", '. ', cleaned_doc)
    cleaned_doc = re.sub(r"(\s[,]{1}\s)", ', ', cleaned_doc)
    cleaned_doc = re.sub(r"(\s[!]{1}\s)", '! ', cleaned_doc)
    cleaned_doc = re.sub(r"(\s[?]{1}\s)", '? ', cleaned_doc)
    
    return cleaned_doc

def lemmatize(doc):
    return " ".join([lemmatizer.lemmatize(word) for word in word_tokenize(doc)])


