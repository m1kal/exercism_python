class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
    def latest(self):
        return self.scores[-1]
    def personal_best(self):
        return self.personal_top_three()[0]
    def personal_top_three(self):
        return list(reversed(sorted(self.scores)[-3:]))
