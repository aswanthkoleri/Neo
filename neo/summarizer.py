from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import nltk
nltk.download('punkt')

def summarizeDoc(summarizerType,content,sentenceCount):
    SUMMARIZERS = {
    'LU': LuhnSummarizer,
    'LS': LsaSummarizer,
    'TR': TextRankSummarizer,
    'LR': LexRankSummarizer
    }
    language='english'
    f = open("doc.txt","a")
    f.write(content)
    f.close()
   
    parser = PlaintextParser.from_file("doc.txt", Tokenizer(language))
    stemmer = Stemmer(language)
    summarizer=SUMMARIZERS[summarizerType](stemmer)
    summarizer.stop_words=get_stop_words('english')
    summarizedContent=""
    for sentence in summarizer(parser.document,sentenceCount):
        summarizedContent+=str(sentence)
    open('doc.txt', 'w').close()
    return summarizedContent