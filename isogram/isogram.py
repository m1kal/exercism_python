import re
def is_isogram(string):
    clean = re.sub('[ -]','',string)
    return len(clean)==len(set(clean.lower()))

