import matplotlib
import numpy as np
import pandas as pd
import nltk
import string as s
from nltk.corpus import stopwords
import matplotlib

import re
import os

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


def remove_url(data):
    return re.sub(r'\s*(?:https?://)?www\.\S*\.[A-Za-z]{2,5}\s*', ' ', data).strip()


def lower_case(data):
    return data.lower()


def word_tok(data):
    tokens = re.findall("[\w']+", data)
    #     print(tokens)
    return tokens


def remove_stopwords(data):
    stopWords = stopwords.words('english')
    new_list = []
    for i in data:
        if i.lower() not in stopWords:
            new_list.append(i)
    #     print(new_list)
    return new_list


def remove_punctuations(data):
    new_list = []
    for i in data:
        for j in s.punctuation:
            i = i.replace(j, '')
        new_list.append(i)
    return new_list


def remove_number(data):
    no_digit_list = []
    new_list = []

    for i in data:
        for j in s.digits:
            i = i.replace(j, '')
        no_digit_list.append(i)

    for i in no_digit_list:
        if i != '':
            new_list.append(i)
    return new_list


def stemming(data):
    porter_stemmer = nltk.PorterStemmer()
    roots = [porter_stemmer.stem(i) for i in data]
    return roots


def lemmatization(data):
    lemmatizer = nltk.stem.WordNetLemmatizer()
    roots = [lemmatizer.lemmatize(i) for i in data]
    return roots


def remove_extraWords(data):
    extra_words = ['href', 'iii', 'lt', 'gt', 'ii', 'com', 'quot']

    new_list = []
    for i in data:
        if i not in extra_words:
            new_list.append(i)
    return new_list