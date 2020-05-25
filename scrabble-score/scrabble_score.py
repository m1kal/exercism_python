Values = {'aeioulnrst' : 1,
          'dg' : 2,
          'bcmp' : 3,
          'fhvwy' : 4,
          'k' : 5,
          'jx' : 8,
          'qz' : 10}

def letter_score(letter):
    return [Values[key] for key in Values.keys() if letter in key][0]
def score(word):
    return sum(letter_score(letter) for letter in word.lower())
