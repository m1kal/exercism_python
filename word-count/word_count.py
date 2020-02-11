import re;
def count_words(sentence):
    words = {}
    clean = re.sub('[.:!@$%^&]', '', sentence.lower())
    for word in [re.sub('(^\'+)|(\'+$)', '', elem) for elem in re.split('[\s,_]+', clean)]:
        if len(word)>0:
            words[word] = words[word] + 1 if word in words else 1
    return words
