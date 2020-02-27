import re;
import collections;
def count_words(sentence):
    clean = re.sub('[.:!@$%^&]', '', sentence.lower())
    words = [re.sub('(^\'+)|(\'+$)', '', elem) for elem in re.split('[\s,_]+', clean)]
    return collections.Counter(word for word in words if len(word) > 0)
