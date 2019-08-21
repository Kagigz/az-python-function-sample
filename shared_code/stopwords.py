
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

def remove_stop_words(text):
    STOPLIST = stopwords.words('english')
    text = ' '.join([word for word in text.split() if word not in STOPLIST])
    return text