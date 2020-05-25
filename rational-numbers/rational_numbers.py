from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer * other.denom == other.numer * self.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + self.denom * other.numer,
                        self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - self.denom * other.numer,
                        self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(pow(self.numer, power), pow(self.denom, power))

    def __rpow__(self, base):
        return pow(base, self.numer/self.denom)

