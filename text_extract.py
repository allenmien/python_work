# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from bs4 import BeautifulSoup
from htmldom import htmldom
from sumy.parsers.plaintext import PlaintextParser
import codecs
LANGUAGE = "chinese"
SENTENCES_COUNT = 3


if __name__ == "__main__":
    url = "http://news.163.com/18/0607/06/DJM7BNEQ00018AOQ.html"
    text = codecs.open('./1.txt', 'r', 'utf-8').read()
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    plain_parser = PlaintextParser.from_string(text,Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    a = parser.document
    b = plain_parser.document
    for sentence in summarizer(b, SENTENCES_COUNT):
        print(sentence)