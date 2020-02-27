import re
def is_pangram(sentence):
   return len(set(re.sub(r'[^a-zA-Z]*', '', sentence.lower()))) == 26

