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
    x = contractions.fix(x)

    return x

def get_just_words(doc):
    return re.sub(r'[^\w ]+', "", doc)

def remove_stopwords(doc):
    cleaned_doc = ' '.join([word for word in doc.split() if word not in english_stopwords])
    cleaned_doc = re.sub(r"(\s[.]\s)", '. ', cleaned_doc)
    cleaned_doc = re.sub(r"(\s[,]\s)", ', ', cleaned_doc)
    cleaned_doc = re.sub(r"(\s[!]\s)", '! ', cleaned_doc)
    cleaned_doc = re.sub(r"(\s[?]\s)", '? ', cleaned_doc)
    
    return cleaned_doc

def lemmatize(doc):
    return " ".join([lemmatizer.lemmatize(word) for word in word_tokenize(doc)])

def remove_footnotes(doc):
    return re.sub(r"\[[\d]{1,3}\]", "", doc)

def clean_text(input_text):
    """
    Infranodus proper uses a separate stage to remove stopwords after normalizing the text
    """
    out_text = lowercase_text(input_text)
    out_text = normalize_whitespace(out_text)
    out_text = replace_html_tags(out_text)
    out_text = remove_emails(out_text)
    out_text = remove_urls(out_text)
    out_text = normalize_unicode(out_text)
    out_text = replace_abbreviations(out_text)
    out_text = get_just_words(out_text)
    out_text = remove_stopwords(out_text)
    out_text = lemmatize(out_text)
    out_text = remove_footnotes(out_text)
    
    return out_text
